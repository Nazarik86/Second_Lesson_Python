# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

import requests
from datetime import datetime

# Вводим код валют для вывода
currency_int = "USD", "EUR", "GMO", "Usd", "eUr"


def currency_rates(code_currency: str):

    # Приводим к единому регистру, независимо от входящего регистра кода валют
    code_currency = code_currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    # Если код валюты встречается, то обрабатываем, если нет, то None
    if response.text.find(code_currency) == -1:
        return None, None
    # Принимаем значение курса запрошенной валюты и дату
    current_rate = response.text.split(f'<CharCode>{code_currency}</CharCode>')
    # Принимаем дату
    date_rate = current_rate[0].split('<ValCurs Date="')
    date_rate = date_rate[1][:10]  # Здесь у нас уже есть дата
    # Преобразуем дату в формат datetime
    date_rate = datetime.strptime(date_rate, '%d.%m.%Y')
    # Обрабатываем курс валюты
    current_rate = current_rate[1].split('<Value>')
    current_rate = current_rate[1].split('</Value>')[0]
    # Переводим курс валюты в числовой тип, меняя разделитель дробной части
    current_rate = current_rate.replace(",", ".")
    return float(current_rate), date_rate.date()
    # проверка использования для вывода чисел формата Decimal
    # return decimal.Decimal(current_rate)


# Выводим результат работы функции и проверяем на правильность полученных вводных данных
for code_curr in currency_int:
    my_rate, my_date = currency_rates(code_curr)
    if my_rate is None:  # если пришло None, то пропускаем
        continue

    print(f'На {my_date} курс {code_curr}: {my_rate} руб.')
