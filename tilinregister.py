import telebot

bot = telebot.TeleBot('6645743177:AAHhtXPh9wwBOu2ANWlydh8N92-EmA6n2mU')

@bot.message_handler(commands=['register', '.', '$', '#'])
def register(message):
    with open('users.txt', 'r+', encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            bot.reply_to(message, 'Usuario ya estás registrado.')
        else:
            archivo.write('{}\n'.format(message.from_user.id))
            bot.reply_to(message, f' Registro Correcto {message.from_user.id} ')

bot.polling()