from QuestionTree import QuestionTree, Node
from vk import(
    send_message,
    buttons_menu,
    faq_menu_button,
    main_menu_button,
    vk
)
from Keyboard import  Keyboard
from vk import Text, OpenLink

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


menu = Node('Основное меню')

menu.add_function(
        send_message,
        ["Я с радостью помогу Вам! Выберите, что Вас интересует:\n • Консультация \n• Лучшие продукты\n • FAQ",
        MAIN_MENU]
)

products = menu.add_children(Node('FAQ'))
products.add_function(
    send_message,
    ["Я собрал самые популярные вопросы в одном разделе, и чтобы Вам было проще, разделил их на категории:\n • Персональные данные\n • Кредиты\n • Карты\n • Вклады\n • Инвестиции\n • Онлайн-сервисы\n",
        Keyboard([main_menu_button,[OpenLink("Подробнее", "https://rencredit.ru/support/faq/")],buttons_menu("Кредиты", "синий"),buttons_menu("Персональные данные", "синий")])]
)
products.add_children(menu)


credits = products.add_children(Node('Кредиты'))
credits.add_function(
    send_message,
    ["Пожалуйста, выберите интересующую Вас тему в меню. \nЕсли Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button,buttons_menu("Оформление кредита", "синий"),buttons_menu("Оплата кредита", "синий"),buttons_menu("Досрочное погашение", "синий"),buttons_menu("Кредитная история", "синий"),buttons_menu("Страховая по кредитам", "синий"),buttons_menu("Закрытие", "синий"),buttons_menu("Просроченная задолженность", "синий"),buttons_menu("Услуга «SMS - оповещение»", "синий")])]
)
credits.add_children(menu)

making_credits = credits.add_children(Node('Оформление кредита'))
making_credits.add_function(
    send_message,
    ["• Подать заявку на кредит наличными можно на сайте, в Мобильном банке, офисе, а также по телефону 8 (800) 200-09-81 (звонок бесплатный).\n • Для оформления кредита на товар обратитесь напрямую в магазин или оформите заявку на сайте партнера.\n",
         Keyboard([main_menu_button,[OpenLink("Написать обращение", "https://rencredit.ru/support/appeals/")]])]
)
making_credits.add_children(menu)
making_credits.add_children(credits)

pay_credits = credits.add_children(Node('Оплата кредита'))
pay_credits.add_function(
    send_message,
    ["Пожалуйста, выберите интересующий Вас вопрос: • Где я могу оплатить?\n • Как узнать сумму погашения и закрыть кредит досрочно?\n • Как списать сумму больше, чем по графику?\n • Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button])]
)
pay_credits.add_children(menu)
pay_credits.add_children(credits)

early_credits = credits.add_children(Node('Досрочное погашение'))
early_credits.add_function(
    send_message,
    ["Пожалуйста, выберите интересующий Вас вопрос: \n • Как узнать сумму погашения и закрыть кредит досрочно?\n • Как оформить заявку на частичное досрочное погашение? \n • Как рассчитать сумму для полного досрочного погашения?\n •Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button])]
)
early_credits.add_children(menu)
early_credits.add_children(credits)


history_credits = credits.add_children(Node('Кредитная история'))
history_credits.add_function(
    send_message,
    ["Как скорректировать кредитную историю?\n Кредитную историю можно скорректировать, если просроченная задолженность по договору возникла не по вине клиента (ошибка платёжной системы/банка и др). Если это ваш случай, опишите ситуацию на сайте, мы свяжемся с Вами в течение 24-х часов и проинформируем о дальнейших действиях.\n Или напишите нам на e-mail (zaprosKKI@rencredit.ru), в письме укажите:\n • ФИО полностью.\n  • Дата рождения.\n  • Номер договора или паспортные данные.\n  • Краткое описание проблемы.\n  • приложите отчет БКИ (при наличие). \n Ваш вопрос будет принят и обработан в течение 3-х рабочих дней.\n",
        Keyboard([main_menu_button])]
)
history_credits.add_children(menu)
history_credits.add_children(credits)

insurance_credits = credits.add_children(Node('Страховая по кредитам'))
insurance_credits.add_function(
    send_message,
    ["Страхование является дополнительной услугой, оказываемой страховой организацией. Страхование осуществляется исключительно на добровольной основе (по желанию Клиента и с его согласия) и не является обязательным условием выдачи Банком Кредита. Клиент вправе самостоятельно застраховать свою жизнь и/или здоровье и/или иные риски и интересы в страховых компаниях, указанных выше, или в любой иной страховой организации, осуществляющей страхование данного вида, по своему выбору. Нежелание заключить договор страхования не может послужить причиной отказа Банка в предоставлении Клиенту Кредита или ухудшить условия Кредитного договора Клиента.\n Пожалуйста, выберите интересующий Вас вопрос в меню. \n Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button])]
)
insurance_credits.add_children(menu)
insurance_credits.add_children(credits)

closure_credits = credits.add_children(Node('Закрытие'))
closure_credits.add_function(
    send_message,
    ["Пожалуйста, выберите интересующий Вас вопрос: Какие бывают справки?\n • Как получить справку/выписку/график? \n • Как получить справку о закрытии?\n • Как закрыть счет после погашения кредита? \n • Когда обновится информация о закрытии кредита в БКИ? \n • Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button])]
)
closure_credits.add_children(menu)
closure_credits.add_children(credits)

overdue_credits = credits.add_children(Node('Просроченная задолженность'))
overdue_credits.add_function(
    send_message,
    ["Пожалуйста, выберите интересующий Вас вопрос: \n • Как узнать сумму просроченной задолженности?\n •На каком основании банк передает информацию в БКИ?\n • В какое БКИ банк передает информацию?\n • Как закрыть счет после погашения кредита?\n • Когда обновится информация о закрытии кредита в БКИ?\n •Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button])]
)
overdue_credits.add_children(menu)
overdue_credits.add_children(credits)

sms_credits = credits.add_children(Node('Услуга «SMS - оповещение»'))
sms_credits.add_function(
    send_message,
    ["Пожалуйста, выберите интересующую Вас тему: \n • Об услуге «SMS-оповещение» \n • Как подключить и сколько стоит услуга «SMS-оповещение»?\n Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню.\n",
        Keyboard([main_menu_button])]
)
sms_credits.add_children(menu)
sms_credits.add_children(credits)



personals = products.add_children(Node('Персональные данные'))
personals.add_function(
    send_message,
    ["Пожалуйста, выберите интересующий Вас вопрос: \n • Как изменить персональные данные ? \n • Как прекратить обработку персональных данных? \n •  Если Вы хотите консультацию в чате или звонок оператора - выберите соответствующий пункт меню..\n",
        Keyboard([main_menu_button])]
)
personals.add_children(menu)



faq = menu.add_children(Node('FAQ'))
faq.add_function(
    send_message,
    ["часто задаваемые вопросы и ответы",
    Keyboard([main_menu_button])]
)
faq.add_children(menu)

consult = menu.add_children(Node('Консультация'))
consult.add_function(
         send_message,
         ["Если Вы хотите консультацию в чате или звонок оператора – выберите соответствующий пункт меню.\n Но я могу помочь Вам с ответами на самые популярные вопросы, просто откройте раздел FAQ.",
        Keyboard([buttons_menu("Чат с консультантом", "синий"), buttons_menu("Перезвоните мне", "синий"),
        main_menu_button])]
)

consult.add_children(menu)

chat = consult.add_children(Node('Чат с консультантом'))
chat.add_function(
         send_message,
         ["Я направил Ваш запрос консультанту – ожидайте его сообщения.\n А пока можете задать ему вопрос или описать свою ситуацию.",
        Keyboard([main_menu_button])]
)
chat.add_children(menu)

chat.add_function(send_message_to_consultant, kwargs={'message': 'Клиент ждет Вашего ответа в чате'})

call = consult.add_children(Node('Перезвоните мне'))
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