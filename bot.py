# -*- coding: utf-8 -*-
# -------- Telepot --------------#
import telepot
from telepot.loop import MessageLoop
# ---------- Other --------------#
from time import sleep
#Import from ./helper.py file
from helper import was_here, write
import logging

#Set bot token
TOKEN = '732974516:AAHp_tZ8UHTgP0FBuAfejFIchXYufcio3Yw'
bot = telepot.Bot(TOKEN)

#Logging
log_location =  'logs/bot.log'#Loction of log file.
logging.basicConfig(filename=log_location ,format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

def join_check(user_id, first_name, last_name, username):
    if was_here(user_id) is not True:
        try:
            write(user_id=user_id, first_name=first_name, last_name=last_name, user_name=username)
            return True
        except Exception as identifier:
            return identifier

#Handeling commands
def handle(msg):
    content_type = telepot.glance(msg)[0]
    if content_type == 'text':
        cmd = msg['text']
        #Get information of user
        chat_id = msg['chat']['id']
        user_id = msg['from']['id']
        first_name = str(msg['from']['first_name']).encode("utf-8").decode("utf-8")
        last_name = str(msg['from']['last_name']).encode("utf-8").decode("utf-8")
        username = msg['from']['username']
        join = join_check(user_id=user_id, first_name=first_name, last_name=last_name, username=username)
        if join is True:
            msg_id = msg['message_id']
            if cmd == "/start":
                output = "Working ..."
            elif cmd == '/help':
                output = "Show help message"
            else:
                pass #TODO: Handling other commands
            bot.sendMessage(chat_id=chat_id, text=output, reply_to_message_id=msg_id)
        else:
            print(join)#TODO: Must be append to logging file
    else:
        pass #TODO: Handling file messages


MessageLoop(bot, handle).run_as_thread()#Handel commands

print("Working ... ")

while True:#Always awake
    sleep(10)