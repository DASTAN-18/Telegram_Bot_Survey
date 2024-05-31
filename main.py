import telebot
from local_settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
MY_CHAT_ID = 5278555399
questions = ["Келечекте кайсы мамлекетке баргыныз келет?", "Кайсыл спорт туру жагат?", " Бош убактынызда эмне кыласыз?"]
chat_answers = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Саламатсызбы суроо- жоопго кош келипсиз! ")
    # chat_answers[message.chat.id] = chat_answers.fromkeys(questions)
    chat_answers[message.chat.id] = {}
    bot.send_message(message.chat.id, f"1-суроо: {questions[0]}")


@bot.message_handler(func=lambda message: True)
def answer_message(message):
    if message.chat.id in chat_answers:
        if questions[0] not in chat_answers[message.chat.id]:
            chat_answers[message.chat.id][questions[0]] = message.text
            bot.send_message(message.chat.id, f"2-суроо: {questions[1]}")

        elif questions[1] not in chat_answers[message.chat.id]:
            chat_answers[message.chat.id][questions[1]] = message.text
            bot.send_message(message.chat.id, f"3-суроо: {questions[2]}")

        elif questions[2] not in chat_answers[message.chat.id]:
            chat_answers[message.chat.id][questions[2]] = message.text
            bot.send_message(message.chat.id, " Жооп бергениниз учун рахмат \nЖооптор ботту тузгон адамга жонотулду")
            bot.send_message(MY_CHAT_ID, f" Сизге {message.from_user.first_name} {chat_answers[message.chat.id]} деп жооп жазды ")


bot.infinity_polling()
