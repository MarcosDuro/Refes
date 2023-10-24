
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import pytz


bot_token = "6645743177:AAHhtXPh9wwBOu2ANWlydh8N92-EmA6n2mU"
channel_id = "-1001909063865"

bot = telebot.TeleBot(bot_token)

banned_users = [5600021911, 5903761717, 6093575641, 6680116501, 6091067689]
allowed_chats = [-1001892428036, -1001909063865]

registered_users = set()

with open('users.txt', 'r') as archivo:
    for linea in archivo:
        registered_users.add(linea.strip())


@bot.message_handler(commands=['register'])
def register(message):
    if str(message.from_user.id) in registered_users:
        bot.send_message(message.chat.id, '¡Ya estás registrado!')
    else:
        registered_users.add(str(message.from_user.id))
        bot.send_message(message.chat.id, 'Por favor, regístrate para poder usarme, utiliza /register.', parse_mode='HTML')

        with open('users.txt', 'a') as archivo:
            archivo.write(str(message.from_user.id) + '\n')


@bot.message_handler(commands=["start", "help"])
def prueba(message):
    bot.send_chat_action(message.chat.id, "typing")
    text = '''Manda Una Sola Foto Con El Comando /tilinrefe y el texto que deseas poner'''
    bot.reply_to(message, text, parse_mode="html")


@bot.message_handler(commands=["tilinrefe"])
def handle_reference_command(message):
    bot.send_chat_action(message.chat.id, "typing")

    text = "Envía una sola foto con el texto que deseas poner."
    bot.reply_to(message, text, parse_mode="html")


@bot.message_handler(content_types=['photo'])
def handle_reference(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    caption = message.caption

    if chat_id not in allowed_chats:
        bot.reply_to(message, "Lo siento, este chat no está autorizado para usar el bot. Entra a @ScrapperTilinChat para poder usarlo.", parse_mode='html')
        return

    if user_id in banned_users:
        bot.reply_to(message, "Lo siento, no tienes permitido usar el bot. Estás baneado no juegues con el bot tal vez fue tu causa de baneo dile a @BannedEnd que te quite ban", parse_mode='html')
        return

    if str(user_id) not in registered_users:
        bot.send_message(chat_id, 'Por favor, regístrate para poder usar este comando Utiliza /register', parse_mode='HTML')
        return

    if caption and caption.startswith("/tilinrefe"):
        texto_referencia = caption.replace("/tilinrefe", "").strip()
        photo = message.photo[0].file_id

        tz = pytz.timezone('America/Mexico_City')
        hora_actual = datetime.now(tz)
        hora_envio = hora_actual.strftime("%I:%M:%S %p")

        mensaje = f"""  
𝙏𝙞𝙡𝙞𝙣𝙎𝙘𝙧𝙖𝙥𝙥「𝙍𝙚𝙛𝙚𝙧𝙚𝙣𝙘𝙞𝙖」      
- - - - - - - - - - - - - - - - - - - - -    
<b><i>Reference By:</i></b> <b><i>@{username}</i></b>
- - - - - - - - - - - - - - - - - - - - -  
<b><i>Date Send [MX]:</i></b> <b><i>{hora_envio}</i></b>
- - - - - - - - - - - - - - - - - - - - -
<b><i>Message:</i></b> <b><i>{texto_referencia}</i></b>
- - - - - - - - - - - - - - - - - - - - -
"""
        refe = InlineKeyboardMarkup(row_width=2)
        b3 = InlineKeyboardButton("𝐂𝐮𝐞𝐧𝐭𝐚𝐬 𝐆𝐫𝐚𝐭𝐢𝐬", url="https://t.me/+nhTYkHisgng5MDYx")
        refe.add(b3)

        bot.send_photo(channel_id, photo, caption=mensaje, reply_markup=refe, parse_mode="HTML")

        bot.reply_to(message, "<b>Gracias Amor Tu Refe Ya Fue Enviada.</b>", parse_mode='html')
        
bot.polling()  