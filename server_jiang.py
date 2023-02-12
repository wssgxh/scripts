import requests
from key import server_key
KEY = server_key
string = "https://sctapi.ftqq.com/{}.send?title=".format(KEY)


def send_message(message):
    resp = requests.post(string + message).content
    print(resp)


send_message('电脑已经启动')