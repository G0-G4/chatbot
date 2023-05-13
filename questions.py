from QuestionTree import QuestionTree, Node
from vk import(
    send_message,
    buttons_menu,
    faq_menu_button,
    main_menu_button,
    vk
)
from Keyboard import Keyboard
import re

def accept_all(s1, s2):
    return True

def accept_phone(s1, s2=None):
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    return bool(re.match(validate_phone_number_pattern, s1)) # Returns Match object

# Extract phone number from a string
extract_phone_number_pattern = "\\+?[1-9][0-9]{7,14}"
re.findall(extract_phone_number_pattern, 'You can reach me out at +12223334444 and +56667778888')


def send_message_to_consultant(fake_id, *args, **kwargs):
    print(kwargs)
    if 'message' in kwargs:
        message = kwargs['message']
    else:
        message = kwargs['text']
    vk.get_api().messages.send(
        user_id = 300297538,
        message = message,
        random_id = 0
        )

MAIN_MENU = Keyboard([buttons_menu("Консультация", "синий"),buttons_menu("Лучшие продукты","синий"),faq_menu_button])

menu = Node('основное меню')

menu.add_function(
        send_message,
        ["Я с радостью помогу Вам! Выберите, что Вас интересует:\n • Консультация \n• Лучшие продукты\n • FAQ",
        MAIN_MENU]
)

products = menu.add_children(Node('Лучшие продукты'))
products.add_function(
    send_message,
    ["Наши продукты бла бла",
        Keyboard([
            main_menu_button,
            buttons_menu("кредиты", "синий"),
            buttons_menu("карты", "синий")])]
)
products.add_children(menu)

# credits = products.add_children(Node("кредиты"))
# credits.add_function(
#     send_message,
#     ['кредиты', Keyboard([main_menu_button])]
# )
# credits.add_children(menu)

# cards = products.add_children(Node("карты"))
# cards.add_function(
#     send_message,
#     ['карты', Keyboard([main_menu_button])]
# )
# cards.add_children(menu)


faq = menu.add_children(Node('FAQ'))
faq.add_function(
    send_message,
    ["часто задаваемые вопросы и ответы",
    Keyboard([main_menu_button])]
)
faq.add_children(menu)

consult = menu.add_children(Node('консультация'))
consult.add_function(
         send_message,
         ["Если Вы хотите консультацию в чате или звонок оператора – выберите соответствующий пункт меню.\n Но я могу помочь Вам с ответами на самые популярные вопросы, просто откройте раздел FAQ.",
        Keyboard([buttons_menu("Чат с консультантом", "синий"), buttons_menu("Перезвоните мне", "синий"),
        main_menu_button])]
)

consult.add_children(menu)

chat = consult.add_children(Node('чат с консультантом'))
chat.add_function(
         send_message,
         ["Я направил Ваш запрос консультанту – ожидайте его сообщения.\n А пока можете задать ему вопрос или описать свою ситуацию.",
        Keyboard([main_menu_button])]
)
chat.add_children(menu)

chat.add_function(send_message_to_consultant, kwargs={'message': 'Клиент ждет Вашего ответа в чате'})

call = consult.add_children(Node('перезвоните мне'))
call.add_function(
         send_message,
         ["Пожалуйста, уточните, как можно к Вам обращаться.",
        Keyboard([main_menu_button])]
)

call.add_children(menu)

name = call.add_children(Node('имя', accepter = accept_all))
name.add_function(
    send_message,
         ["Пожалуйста, укажите свой номер телефона.",
        Keyboard([main_menu_button])]
)
name.add_function(
    send_message_to_consultant
)

end = name.add_children(Node('end', accepter = accept_phone))
end.add_function(
    send_message,
    ['ожидайте звонка', Keyboard([main_menu_button])])
end.add_function(
    send_message_to_consultant
)
end.add_children(menu)

questions = QuestionTree(menu)

# if __name__ == '__main__':
    # tree.show()
    # print(accept_phone(''))