#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
from bs4 import BeautifulSoup
import requests
import telebot

API_TOKEN = '5051387618:AAEFB8Pb79B3UVNqmWaOZXVtLKUqqq4GSEI'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['seke'])
def send_welcome(message):
    url = "https://www.tgju.org/coin"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    pricelist=[]
    pricelist1=[]
    elem = soup.find(class_='market-details-price')
    pricelist.append( elem.text.split(':')[1].replace("\n",""))

    url = "https://www.tgju.org/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    elem1 = soup.find_all('td',{'data-market-row','price_dollar_rl'})
    bot.reply_to(message,pricelist[0])

@bot.message_handler(commands=['dolar'])
def send_welcome(message):
    try:
        url = "https://www.tgju.org/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        elem1 = soup.find_all(class_='info-price')
        dolar = elem1[5].text
        teter = elem1[8].text


        

        bot.reply_to(message,dolar)
    except:
        bot.reply_to(message,"404 not found")


@bot.message_handler(commands=['teter'])
def send_welcome(message):
    try:
        url = "https://www.tgju.org/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        elem1 = soup.find_all(class_='info-price')
        dolar = elem1[5].text
        teter = elem1[7].text


        

        bot.reply_to(message,teter)
    except:
        bot.reply_to(message,"404 not found")
        




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
