Purpose:

Simple Flask application talking to Telegram bot API. Intended to be used as a backend processing order requests recieved from different landing pages - to be then displayed as text messages in a Telegram chanel of an online shop.

How to run as a container:

docker run --privileged --name=happyshop --restart=always -d -p 8080:8080 -e TG_BOT_TOKEN='' -e TG_GROUP_CHAT_ID=''  hvv19890828/happyshop