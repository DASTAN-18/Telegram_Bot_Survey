import telebot
from local_settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


Chat_answer = {}

questions = [
    "Келечекте кайсы мамлекетке баргыныз келет?",
    "Кайсыл спорт туру жагат?",
    "Бош убактынызда эмне кыласыз?",
    "Жаккан тамагыныз эмне,"
]

MY_CHAT_ID = 5278555399


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Саламатсызбы суроо- жоопго кош келипсиз! ")
    Chat_answer[message.chat.id] = Chat_answer.fromkeys(questions)
    bot.send_message(message.chat.id,  questions[0])


@bot.message_handler(func=lambda message: True)
def answer_message(message):
    if message.chat.id in Chat_answer:
        question_key_list = list(Chat_answer[message.chat.id].keys())
        for i in range(len(question_key_list)):
            if Chat_answer[message.chat.id][question_key_list[i]] is None:
                Chat_answer[message.chat.id][question_key_list[i]] = message.text
                print(Chat_answer)
                try:
                    bot.send_message(message.chat.id, question_key_list[i+1])
                except IndexError:
                    bot.send_message(message.chat.id,
                                     " Жооп бергениниз учун рахмат \nЖооптор ботту тузгон адамга жонотулду")
                    bot.send_message(MY_CHAT_ID,
                                     f" Сизге {message.from_user.first_name} {Chat_answer[message.chat.id]} деп жооп жазды ")
                break


bot.infinity_polling()

#             if Chat_answer[key][value] == None :
#             Chat_answer[message.chat.id][questions[0]] = message.text
#             bot.send_message(message.chat.id, f"2-суроо: {questions[1]}")
#
#         elif Chat_answer[message.chat.id][questions[1]] == None :
#             Chat_answer[message.chat.id][questions[1]] = message.text
#             bot.send_message(message.chat.id, f"3-суроо: {questions[2]}")
#
#         elif Chat_answer[message.chat.id][questions[2]] == None :
#             Chat_answer[message.chat.id][questions[2]] = message.text
#             bot.send_message(message.chat.id, " Жооп бергениниз учун рахмат \nЖооптор ботту тузгон адамга жонотулду")
#             bot.send_message(My_chat, f" Сизге {message.from_user.first_name} {Chat_answer[message.chat.id]} деп жооп жазды ")
#             print(Chat_answer)


