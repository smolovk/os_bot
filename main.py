import telebot
import os
import numpy as np
import cv2

bot = telebot.TeleBot("1355354595:AAGouNLuE0MvvJ_3tfLMAL2IGxHodRnOAYQ", parse_mode=None)

 
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def create_img(text, filename):
    # определяете шрифт
    font = ImageFont.truetype('Montserrat/Montserrat-Regular.ttf', 14)

    # определяете положение текста на картинке
    text_position = (5, 70)

    # цвет текста, RGB
    text_color = (0,0,0)

    # загружаете фоновое изображение
    img = Image.open('blank.jpg')

    # определяете объект для рисования
    draw = ImageDraw.Draw(img)

    # добавляем текст
    draw.text(text_position, text, text_color, font)

    # сохраняем новое изображение
    img.save(filename)
    print("success")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello")

@bot.message_handler(func=lambda message: True)
def get_text(message):
    text = message.text

    textArr = text.split("\n")
    output = []

    for i in range(len(textArr)):
        ii = 1 + i
        if ii % 4 == 0:
            outputS = []
            outputS.append(textArr[i-3])
            outputS.append(textArr[i-2])
            outputS.append(textArr[i-1])
            outputS.append(textArr[i])

            output.append(outputS)
        else:
            pass

    print(output)

    paths = []
    num = 0
    for one in range(len(output)):
        create_img("\n".join(output[one]), "img_" + str(num) + ".jpg")
        paths.append("img_" + str(num) + ".jpg")
        num += 1
    
    for path in paths:
        print("sent " + path)
        bot.send_photo(message.chat.id, open(path, 'rb'));
    


bot.polling()