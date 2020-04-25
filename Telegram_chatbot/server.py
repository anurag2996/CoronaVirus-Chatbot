import requests
import json
from bs4 import BeautifulSoup
import json
import os
import datetime
import time


def make_reply(msg):
    # reply = None
    if msg =="/new":
        reply = information
    else:
        reply = "Check your input"
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
