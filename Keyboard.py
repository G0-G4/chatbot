import json

class Keyboard:
 
    def __init__(self, button: list, one_time=False, inline=False):
        self.one_time = one_time
        self.inline = inline
 
        self.keyboard = {
            "one_time": self.one_time,
            "inline": self.inline,
            "buttons": button
        }
 
    def add_keyboard(self):
        obj = json.dumps(self.keyboard, ensure_ascii=False).encode("utf-8")
        return obj.decode("utf-8")
 
    def get_empty_keyboard(self):
        self.keyboard["buttons"] = []
        return self.add_keyboard()