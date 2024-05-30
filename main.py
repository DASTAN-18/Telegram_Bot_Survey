import telebot
from local_settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
My_chat = 5278555399
questions = ["Келечекте кайсы мамлекетке баргыныз келет?", "Кайсыл спорт туру жагат?", " Бош убактынызда эмне кыласыз?"]
Chat_answer = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Саламатсызбы суроо- жоопго кош келипсиз! ")
    Chat_answer[message.chat.id] = Chat_answer.fromkeys(questions)
    bot.send_message(message.chat.id, f"1-суроо: {questions[0]}")

@bot.message_handler(func=lambda message:True)
def answer_message(message):
    if message.chat.id in Chat_answer:
        if Chat_answer[message.chat.id][questions[0]] == None :
            Chat_answer[message.chat.id][questions[0]] = message.text
            bot.send_message(message.chat.id, f"2-суроо: {questions[1]}")

        elif Chat_answer[message.chat.id][questions[1]] == None :
            Chat_answer[message.chat.id][questions[1]] = message.text
            bot.send_message(message.chat.id, f"3-суроо: {questions[2]}")

        elif Chat_answer[message.chat.id][questions[2]] == None :
            Chat_answer[message.chat.id][questions[2]] = message.text
            bot.send_message(message.chat.id, " Жооп бергениниз учун рахмат \nЖооптор ботту тузгон адамга жонотулду")
            bot.send_message(My_chat, f" Сизге {message.from_user.first_name} {Chat_answer[message.chat.id]} деп жооп жазды ")
            print(Chat_answer)


bot.infinity_polling()