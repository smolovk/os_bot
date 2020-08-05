from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import chalk
import telebot

bot = telebot.TeleBot("1303574038:AAFXtPPeRwatYsxpp6qsLgqmQPp7jyAZFBs", parse_mode="HTML")

green = "[" + chalk.green("+") + "]"
yellow = "[" + chalk.yellow("+") + "]"
red = "[" + chalk.red("+") + "]"

print(green + "Working...")

def create_img(text, filename):
    try:
        # определяете шрифт
        font = ImageFont.truetype('Montserrat/Montserrat-Regular.ttf', 52)

        # определяете положение текста на картинке
        text_position = (15, 380)

        # цвет текста, RGB
        text_color = (0, 0, 0)

        # загружаете фоновое изображение
        img = Image.open('blank.jpg')

        # определяете объект для рисования
        draw = ImageDraw.Draw(img)

        # добавляем текст
        draw.text(text_position, text, text_color, font)

        # сохраняем новое изображение
        img.save(filename)
        print(chalk.green("Images saved successfully, sending... \n"))
    except imgErr:
        print(red + imgErr)
        print(chalk.red("Error while sending images!!!, reloading"))
    

def send_photo(message, paths):
    for path in paths:
        print(chalk.cyan("sent " + path))
        bot.send_photo(message.chat.id, open(path, 'rb'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Отправь мне любой стих, а я отправлю его тебе в виде фотографий!🖋")

@bot.message_handler(func=lambda message: True)
def get_text(message):
    text = message.text

    textArr = text.split("\n")
    output = []

    isFour = False

    for i in range(len(textArr)):
        if textArr[i-1] == "\n" or textArr[i-1] == "":
            textArr.pop(i-1)

    if len(textArr) % 4 != 0:
        while len(textArr) % 4 != 0:
            textArr.append("")
    else:
        pass

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

    print(yellow + "Got: " + str(textArr) + "\n")
    print(green + "Output: " + str(output) + "\n")
    paths = []
    num = 0
    for one in range(len(output)):
        create_img("\n".join(output[one]), "img_" + str(num) + ".jpg")
        paths.append("img_" + str(num) + ".jpg")
        num += 1

    send_photo(message, paths)
    

bot.polling()