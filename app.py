#!/usr/bin/env python

SERVER = 'irc.twitch.tv'

import lurklib
import time
import random
import datetime
from chatterbot import ChatBot

bot = ChatBot(
    "marbleracechat",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    database="./database.json"
)
class HelloBot(lurklib.Client):
    def on_connect(self):
        """ Join #bots upon connecting. """
        self.join_('#marbleracing')

    def on_chanmsg(self, from_, channel, message):
        """ Event handler for channel messages. """        
        if message.startswith('!') or from_[0] == 'marbleracing' or from_[0] == 'nightbot':
            pass
        else:    
            print('> ' + message)
			time.sleep(random.randint(1,5))
			self.privmsg(channel, '!marble BibleThump')
			print('marbled')
        
if __name__ == '__main__':
    HELLOBOT = HelloBot(server=SERVER, nick=(''), password='someouathhere')
    
HELLOBOT.mainloop()