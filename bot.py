# -------- Telepot --------------#
import telepot
from telepot.loop import MessageLoop
# ---------- Other --------------#
from time import sleep

#Set bot token
TOKEN = '732974516:AAHp_tZ8UHTgP0FBuAfejFIchXYufcio3Yw'
bot = telepot.Bot(TOKEN)

#Handeling commands
def handle(msg):
    content_type = telepot.glance(msg)[0]
    if content_type == 'text':
        cmd = msg['text']
        chat_id = msg['chat']['id']
        msg_id = msg['message_id']
        if cmd == "/start":
            output = "Working ..."
            bot.sendMessage(chat_id=chat_id, text=output, reply_to_message_id=msg_id)
        else:
            pass #TODO: Handling other commands
    else:
        pass #TODO: Handling file messages


MessageLoop(bot, handle).run_as_thread()#Handel commands

print("Working ... ")

while True:#Always awake
    sleep(10)