from deep_translator import GoogleTranslator
import telebot
from telebot import types

TOKEN = "8304931404:AAEMNLKvu3FshCw5Hu1U4AYDH2OA9VBiah4"
bot = telebot.TeleBot(TOKEN)

#suport languages

LANGUAGE ={
    "English": "en"
    "RUssiam" : "ru"
    "O'zbekcha": "uz"
    "Deutsch": "de"
}

#save user lang
user_langs = {} #{"chat_id":"language"}

#start command
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"добро пожаловать в бот переводчик! \n""Напиши мне любой текст, а я попробую узнать какой это язык и переведу \n\n" "используй /translator чтобы запустить функцию.")

@bot.message_handler(commands=["language"])
def choose_lang(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text = lang, callback_data=f"setlang|{code}") for lang , code in LANGUAGE.items() ]
    markup.add(*buttons)
    

    bot.send_message(message.chat.id, "Выберите язык:", reply_markup=markup)

bot.infinity_polling


@bot.message_handler(func=lambda msg:True)
def translate_or_ask(message):
    chat_id= message.chat.id
    text = message.text

    if chat_id in user_langs:
        target_lang = user_langs[chat_id]
        try:
            translator = GoogleTranslator