# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из двух случайных слов, взятых из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
#
# Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(*, number_of_jokes, only_unique=False):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjective = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_of_jokes = []

    for _ in range(number_of_jokes):
        if only_unique:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjective)

            from_nouns_list = nouns.pop()
            from_adverbs_list = adverbs.pop()
            from_adjectives_list = adjective.pop()

        else:
            from_nouns_list = random.choice(nouns)
            from_adverbs_list = random.choice(adjective)
            from_adjectives_list = random.choice(adjective)

        new_joke = f'{from_nouns_list} {from_adverbs_list} {from_adjectives_list}'

        list_of_jokes.append(new_joke)

    return list_of_jokes


print('Не уникальные: ', get_jokes(number_of_jokes=5))
print('Уникальные: ', get_jokes(number_of_jokes=5, only_unique=True))
