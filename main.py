# coding=UTF-8

from wxpy import *
import time
from _datetime import datetime
import os


bot = Bot(cache_path=True)
bot.groups(update=True, contact_only=False)
target_group = None
target_person = None

dir_path = os.path.dirname(__file__)
rel_path = "提醒喝奶茶小助手.jpg"
abs_pic_path = os.path.join(dir_path, rel_path)


def print_time_and_msg(msg: str) -> str:
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime(f'[%H:%M:%S:%m] - {msg}')
    return readable_time


def send_group_msg():
    global target_group, abs_pic_path
    target_group = bot.groups().search(u"提醒喝水")[0]
    target_group.update_group(members_details=True)
    target_group.send(abs_pic_path)

    # TODO: Find a way to send pictures
    # TODO: wxpy.exceptions.ResponseError: err_code: 1; err_msg:


def send_to_friend():
    global target_person, abs_pic_path
    target_person = bot.friends().search("鸡腿")[0]
    target_person.send_file(abs_pic_path)
    print_time_and_msg("Sent!")


def interval_send():
    while True:
        send_group_msg()
        print_time_and_msg("Sent!")
        time.sleep(60 * 60)


if __name__ == '__main__':
    send_to_friend()
