# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

from requests import get


def currency_rates(code):
    currency_code_list = []
    currency_value_list = []
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split('<CharCode>')[1:]:
        currency_code_list.append(el.split('</CharCode>')[0])
    for item in content.split('<Value>')[1:]:
        currency_value_list.append(item.split('</Value>')[0].replace(',', '.'))
    pairs_dict = dict(zip(currency_code_list, currency_value_list))
    return pairs_dict.get(code.upper())
    # for key, val in pairs_dict.items():
    #     if code.upper() == key:
    #         return float(val)


print(currency_rates('USD'))
print(currency_rates('EUR'))
