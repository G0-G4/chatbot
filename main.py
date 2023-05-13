import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk import vk
from vk import send_message
from model import bot
 
from questions import questions, MAIN_MENU

requests = {}

for event in VkLongPoll(vk).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.lower()
        print(text)

        if not questions.user_exists(user_id):
            questions.create_user(user_id)
            send_message(
                user_id,
                'Я с радостью помогу Вам! Выберите, что Вас интересует:\n • Консультация \n• Лучшие продукты\n • FAQ',
                MAIN_MENU)
            continue
        
        node = questions.move_user(user_id, text)
        if node:
            node.call(user_id)
            for c in node.children:
                print('   ', c.text)
        else:
            send_message(user_id, 'возможно это вам поможет')
            send_message(user_id, bot(text))