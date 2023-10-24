
import telebot

bot = telebot.TeleBot('6645743177:AAHhtXPh9wwBOu2ANWlydh8N92-EmA6n2mU')

registered_users = set()

# Leer los usuarios registrados desde el archivo users.txt
with open('users.txt', 'r') as archivo:
    for linea in archivo:
        registered_users.add(linea.strip())

# Manejador para el comando de registro y otros comandos
@bot.message_handler(commands=['register', '.', '$', '#'])
def register(message):
    if str(message.from_user.id) in registered_users:
        bot.send_message(message.chat.id, '¡Ya estás registrado!')
    else:
        registered_users.add(str(message.from_user.id))
        bot.send_message(message.chat.id, 'Por favor, regístrate para poder usarme, utiliza <b>/register</b>.', parse_mode='HTML')

        # Guardar el usuario recién registrado en el archivo users.txt
        with open('users.txt', 'a') as archivo:
            archivo.write(str(message.from_user.id) + '\n')

bot.polling()