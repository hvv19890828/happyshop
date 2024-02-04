from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/process_form', methods=['POST'])
def process_form():
    token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"

    # Extract form data
    name = request.form['name']
    phone = request.form['phone']
    city = request.form['city']
    number = request.form['number']
    choose = request.form['choose']
    emount = request.form['emount']

    # Construct the message
    message = f"Name: {name}\nPhone: {phone}\nCity: {city}\nNumber: {number}\nChoose: {choose}\nEmount: {emount}"

    # Send message to Telegram
    api_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    # Use requests library for more advanced handling
    # Make sure to install it: `pip install requests`

    # Example using requests:
    # import requests
    # requests.get(api_url)

    return redirect("/thank_you_page.html")

if __name__ == '__main__':
    app.run(debug=True)
