# coding=UTF-8

from wxpy import *
import time
from _datetime import datetime

bot = Bot(cache_path=True)

bot.groups(update=True, contact_only=False)
target_group = bot.groups().search(u"提醒喝水")[0]
target_group.update_group(members_details=True)

reminder_msg = f"提醒喝奶茶小助手.jpg"

while True:
    now_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S:%M')
    target_group.send(reminder_msg)
    print(f"{now_time} - Sent!")
    time.sleep(60 * 60)

