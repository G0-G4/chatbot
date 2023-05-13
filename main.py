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
            # отправить сообщение
            send_message(user_id, 'возможно это вам поможет')
            send_message(user_id, bot(text))
 
        # if text == "чат с консультантом":
        #     send_message(user_id,
        #                  "Я направил Ваш запрос консультанту – ожидайте его сообщения.\n А пока можете задать ему вопрос или описать свою ситуацию.",
        #                  Keyboard([main_menu_button]))
        #     # тут отправляем от бота сообщение модератору
        #     vk.get_api().messages.send(user_id=300297538, message='Клиент ждет Вашего ответа в чате', random_id=0)