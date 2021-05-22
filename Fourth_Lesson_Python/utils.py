from requests import get
from decimal import Decimal
from datetime import datetime

# Создаём функцию для вывода курса валюты и даты, вводимых валют
def currency_rates(currency=None):
    if currency:
        # Приводим полученные значения к верхнему регистру
        currency = currency.upper()
        # Присваиваем переменной url значение с какого ресурса получить данные
        url = r"http://www.cbr.ru/scripts/XML_daily.asp"
        # В переменную response при помощи get заносим получаемые значения
        response = get(url)
        # Создаём переменную server_answer и заносим туда полученную дату, разделённую по " "
        server_answer = response.headers.get("Date").split(" ", maxsplit=4)
        # В переменную server_date вносим все полученные значения из server_answer
        server_date = datetime.strptime(f'{server_answer[2]} {server_answer[1]} {server_answer[3]}', '%b %d %Y')
        # Меняем кодировку полученных данных
        content = response.content.decode(encoding=response.encoding)

        # Создаём пустой словарь, для внесения обработанных данных
        rate_dict = {}

        # Сравниваем при помощи цикла наличие вводных данных с CharCode и записываем их в словарь
        for el in content.split('<CharCode>')[1:]:
            # Заносим данные из элемента словаря в переменную char_code
            char_code = el.strip()[:3]
            # Заносим данные из элемента словаря в переменную nominal с корректировкой выходных данных
            nominal = el.split('<Nominal>')[1][0:5].replace('<', '').replace('/', '').replace('N', '').replace('o', '')
            # Заносим данные из элемента словаря в переменную value
            value = el.split('<Value>')[1][:7]
            # Заносим полученные данные в словарь из переменных nominal и value
            rate_dict[char_code] = {'nominal': nominal, 'value': value}

        # При помощи цикла данные в словаре приводим к выводимому результату
        if currency in rate_dict:
            # Создаём переменную result из полученного курса, приводя её вывод к десятичной дроби
            result = Decimal(str(rate_dict.get(currency)['value']).replace(',', '.'))
            # В переменную price_rub заносим результат деления курса валюты на полученное значение номинала
            price_rub = result / Decimal(rate_dict.get(currency)['nominal'])
            # Возвращаем обработанный курс валюты и дату
            return f'{float(price_rub.quantize(Decimal("1.00")))}, {server_date.date()}'


