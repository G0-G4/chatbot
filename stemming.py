from nltk.tokenize import word_tokenize
from nltk.stem.snowball import RussianStemmer
from nltk.stem import WordNetLemmatizer
import pymorphy2
import difflib
import Levenshtein
from collections import defaultdict

morph = pymorphy2.MorphAnalyzer()
stemmer = RussianStemmer()

def get_words(sentence):
    words = set()
    for w in word_tokenize(sentence):
        words.add(stemmer.stem(w))
    return words


def comapare_sets(s1, s2):
    score = 0
    for w1 in s1:
        for w2 in s2:
            score += Levenshtein.ratio(w1, w2)
    # score /= (len(s1) + len(s2) )
    return score


if __name__ == '__main__':
    questions = [
        ('Как оформить кредит?', 'получение кредита'),
        ('Как мне оформить кредит?', 'получение кредита'),
        ('помогите оформить кредит', 'получение кредита'),
        ('хочу кредит', 'получение кредита'),
        ('как оформлять кредит', 'получение кредита'),
        ('получить кредит', 'получение кредита'),

        ('можно ли досрочно погасить кредит', 'гашение кредита'),
        ('хочу оплатить кредит заранее', 'гашение кредита'),
        ('можно ли заплатить раньше срока', 'гашение кредита'),

        ('хочу кредитку', 'офрмить кредитку'),
        ('как оформить кредитную карту', 'офрмить кредитку'),
        ('кредитная карта', 'офрмить кредитку'),

        ('как изменить персональные данные', 'персональные данные'),
        ('изменились персональные данные', 'персональные данные'),
        ('хочу изменить персональные данные', 'персональные данные'),
        ('обновился паспорт, что делать', 'персональные данные')

    ]

    # d = defaultdict(set)
    # for q, type in questions:
    #     d[type] |= get_words(q)
    # print(d)
    d = {
        'получение кредита': {
            'офромить', 'получить', 'кредит', 'открыть'
        },
        'гашение кредита': {
            'гасить', ' платить', 'кредит', 'закрыть'
        },
        'офрмить кредитку': {
            'карта', 'кредитка', 'офрмить', 'заказать'
        },
        'персональные данные': {
            'данные', 'паспорт', 'изменить', 'персональные'
        }
    }

    def get_recommendations(question):
        words = get_words(question)
        res = []
        for type, s in d.items():
            res.append([type, comapare_sets(words, s)])
        res.sort(key=lambda x: x[1], reverse=True)
        return res

    for q, qtype in questions:
        for type, s in d.items():
            print(q, '->', type)
            print(comapare_sets(get_words(q), s))
        print('----------')

    print(get_recommendations('Роман, мне 21 я поменял паспорт'))


