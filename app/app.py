#!/usr/bin/python3

import os
from waitress import serve
from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__)

boToken = os.environ['TG_BOT_TOKEN']
chatID  = os.environ['TG_GROUP_CHAT_ID']

# Bot route
@app.route('/happyshop_process_form', methods=['POST'])
def happyshop_process_form():
    # Extract form data
    product = request.form.get('product')
    name = request.form.get('name')
    phone = request.form.get('phone')
    city = request.form.get('city')
    delivery = request.form.get('delivery')
    call = request.form.get('call')
    amount = request.form.get('amount')

    # Construct the message
    botMessage = f"Product: {product}\nName: {name}\nPhone: {phone}\nCity: {city}\nDelivery: {delivery}\nCall: {call}\nAmount: {amount}"

    # Send message to Telegram
    sendMessageURL = f"https://api.telegram.org/bot{boToken}/sendMessage?chat_id={chatID}&text={botMessage}"    
    requests.get(sendMessageURL)

    return render_template("thank_you_page.html", name=name, phone=phone, city=city, delivery=delivery, call=call, amount=amount, product=product)

# Health route
@app.route("/happyshop_health")
def health():
    response = make_response(jsonify({"Response": "200"}), 200)
    response.headers["Content-Type"] = "application/json"
    return response

#--------Main-------------------#
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
#-------------------------------#
