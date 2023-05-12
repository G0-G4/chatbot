import json

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token="vk1.a.1zYvFKvwxgBnTlnp7jj5nj3vt3qsWpLLIrTQMKblJrILHn6IJVZW3seodka9ZVb--m9xLgi_uQaPAlaUE-CzqY7tidwjpJ8q7k52d2iU-J1PJVKFfab3FI1--9_ygcmdF2u0ghWlgyFoDkOVr7F1jHMKmgdCjjhP9ZqyGFlz2vMeBoJeidjuafIvicA_OTIf_tNjnAxlEeBqse8EplRbZg")

class User():
    def __init__(self,id,mode,cash):
        self.id = id
        self.mode = mode
        self.cagh = cash
def get_keyboard(buts):
    nb = []
    color = ""
    for i in range(len(buts)):
        nb.append([])
        for k in range(len(buts[i])):
            nb[i].append(None)
    for i in range(len(buts)):
        for k in range(len(buts[i])):
            text = buts[i][k][0]
            color = {'зеленый' : 'positive', 'красный': 'negative', 'синий':'primary'} [buts[i][k][1]]
            nb[i][k] = {"action":{"type":"text","payload":"{\"button\": \""+ "1" +"\"}","label":f"{text}"}, "color":f"{color}"}
    first_keyboard = {"one_time": False, "buttons":nb}
    first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
    first_keyboard = str(first_keyboard.decode('utf-8'))
    return first_keyboard



def sender(user_id, message, key):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0,
        'keyboard': key
    })


start_key = get_keyboard([
    [('Начать','синий')]
])
longpoll = VkLongPoll(session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        sender(user_id, "Здравствуйте! Я Роман -- виртуальный помощник Ренессанс Банка. Отвечу на Ваши вопросы и помогу найти интересующую информацию о банке. Просто нажмите \"Начать\"! ", start_key)


