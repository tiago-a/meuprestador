import sys
import time
import telepot
from convo import convo

def handle(msg):
	
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	
	BOTmsg = convo(msg['text'])
	print(BOTmsg)
	bot.sendMessage(chat_id, BOTmsg)

bot = telepot.Bot('313888754:AAFaP3AIcT04R4gTANAj5gfWQeivJemYy90')
bot.sendMessage(275172889, "Ola bem vindo ao meuPrestador!\n\nSou um BOT e estou aqui para ajudar voce em sua busca por um prestador, por favor digite o servico que precisa e eu farei o resto. :)")
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)