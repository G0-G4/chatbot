import os
import random
import json
import urllib.request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
import pickle

filename = "example.json"

with open(filename, 'r', encoding='UTF-8') as file:
    data = json.load(file)

X = []
y = []

for name in data:
    for phrase in data[name]['examples']:
        X.append(phrase)
        y.append(name)
    for phrase in data[name]['responses']:
        X.append(phrase)
        y.append(name)

vectorizer = CountVectorizer()
vectorizer.fit(X)
X_vec = vectorizer.transform(X)

'''model_mlp = MLPClassifier()
model_mlp.fit(X_vec, y)
pickle.dump(model_mlp, open('chatbot_model.h5', 'wb'))'''

model_mlp = pickle.load(open('chatbot_model.h5', 'rb'))

def get_intent(text):
    text_vec = vectorizer.transform([text])
    return model_mlp.predict(text_vec)[0] 

def get_response(intent):
    return random.choice(data[intent]['responses'])

def bot(text):
    intent = get_intent(text)
    answer = get_response(intent)
    return answer

if __name__ == '__main__':
    text = ""
    while text != "Выход":
        text = input('< ')
        print('>', bot(text))