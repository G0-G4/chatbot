from collections import defaultdict

class Node:
    def __init__(self, text, accept_all = False) -> None:
        self.children = []
        self.text = text.strip().lower()
        # self.function = function
        # self.args = args
        self.accept_all = accept_all
        self.functions = []

    def add_function(self, function, args = [], kwargs = {}):
        self.functions.append([function, args, kwargs])


    def call(self, user_id):
        for f, a, kw in self.functions:
            f(user_id, *a, **kw)
        # self.function(user_id, *self.args)

    def add_children(self, node):
        self.children.append(node)
        return node
    
    def paths(self):
        return list(map(lambda x: x.text, self.children))
    
    def accept(self, message):
        if self.accept_all:
            return True
        return self.text == message
    
    def show(self, depth=0):
        print('*' * depth*2 + self.text)
        for c in self.children:
            c.show(depth + 1)
    
class QuestionTree:

    def create_rules(self):
        pass

    def __init__(self, tree):
        self.user_pos = dict()
        self.user_info = dict()
        self.tree = tree

    def create_user(self, user):
        self.user_pos[user] = self.tree
        self.user_info[user] = defaultdict(dict)
    
    def user_exists(self, user):
        return user in self.user_pos
    
    def move_user(self, user, message):
        current = self.user_pos[user]
        for node in current.children:
            if node.accept(message):
                self.user_pos[user] = node
                return node

if __name__ == '__main__':
    tree = Node('начало')
    menu = tree.add_children(Node('основное меню'))
    consult = menu.add_children(Node('консультация'))
    menu.add_children(Node('лучшие продукты'))

    consult.add_children(Node('чат с консультантом','чат с консультантом'))
    consult.add_children(Node('перезвонить'))

    user = 1
    user2 = 2
    rules = QuestionTree(tree)
    rules.create_user(user)
    rules.create_user(user2)
    rules.move_user(user, 'основное меню')
    rules.move_user(user, 'консультация')
    rules.move_user(user2, 'консультация')


