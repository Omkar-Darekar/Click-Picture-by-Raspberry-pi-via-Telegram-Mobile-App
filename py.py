import capture as cap
import telepot
import sys
from telepot.loop import MessageLoop

def fun(msg):
	cmd = msg['text']
	cot , cht , chi =telepot.glance(msg) 
	if cmd == "pic" or cmd == "Pic"or cmd == "/Pic" or cmd == "/pic" or cmd == "PIC" or cmd == "/PIC":
		cap.captured()
		bot.sendPhoto(chi,open("./img/img.jpg","rb"))

tok="937000027:AAEc99RK5kYYsyW6rf15SuCo8iuo8Z5fSMD" #note --> Your Telgram Token
bot=telepot.Bot(tok)
MessageLoop(bot,fun).run_as_thread()
print("started")
while True:
	pass
