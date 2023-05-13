import vk_api
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get('token')
print(token)
vk = vk_api.VkApi(token = token)

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