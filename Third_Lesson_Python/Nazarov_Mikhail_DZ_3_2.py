# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы.
# Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(from_english: str):
    translation_rezult_dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }

    translation_rezult = translation_rezult_dictionary.get(from_english.lower())

    if translation_rezult is None:
        return None

    if from_english.istitle():
        return translation_rezult.capitalize()

    return translation_rezult

lower_case = num_translate_adv('seven')
capitalize_case = num_translate_adv('Eight')
none_case = num_translate_adv('eleven')

print(lower_case)
print(capitalize_case)
print(none_case)