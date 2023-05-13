import vk_api
from typing import Optional

vk = vk_api.VkApi(token="vk1.a.1zYvFKvwxgBnTlnp7jj5nj3vt3qsWpLLIrTQMKblJrILHn6IJVZW3seodka9ZVb--m9xLgi_uQaPAlaUE-CzqY7tidwjpJ8q7k52d2iU-J1PJVKFfab3FI1--9_ygcmdF2u0ghWlgyFoDkOVr7F1jHMKmgdCjjhP9ZqyGFlz2vMeBoJeidjuafIvicA_OTIf_tNjnAxlEeBqse8EplRbZg")

class ButtonColor:
 
    NEGATIVE = "negative"
    POSITIVE = "positive"
    PRIMARY = "primary"
    SECONDARY = "secondary"

class Text:
 
    def __new__(cls, label: Optional[str], color: Optional[str]="secondary", payload: Optional[str]=None):
        return {
            "action": {
                "type": "text",
                "label": label,
                "payload": payload
            },
            "color": color
        }


class OpenLink:
    def __new__(cls, label: Optional[str], link: Optional[str], payload: Optional[str] = None):
        return {
            "action": {
                "type": "open_link",
                "label": label,
                "link": link,
                "payload": payload
            }
        }
def send_message(user_id, message, keyboard=None, *args, **kwargs):
    values = {
        "user_id": user_id,
        "message": message,
        "random_id": 0,
    }
 
    if keyboard is not None:
        values["keyboard"] = keyboard.add_keyboard()
    vk.method("messages.send", values)
 
 
main_menu_button = [Text("Основное меню", "secondary")]
faq_menu_button = [Text("FAQ", "positive")]
 
def buttons_menu(text, color):
    if color == "белый":
        return [Text(text, "secondary")]
    if color == "красный":
        return [Text(text, "negative")]
    if color == "зеленый":
        return [Text(text, "positive")]
    return [Text(text,"primary")]