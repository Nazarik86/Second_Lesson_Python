# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
#
# [57.8, 46.51, 97, ...]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# * Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
#
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

# Изначально начинал делать по другому и застопорился,
# сделал так же как объяснили на разборе задания, только работал с другим списком и по своему переназвал переменные.

prices_list = [10.50, 52.99, 65.25, 24.55, 36.75, 150.99, 62.85, 78.49, 42.25, 92.35, 100]
new_price_list = []

for price in prices_list:
    price_string = str(price)
    price_list_from_price = price_string.split('.')

    if len(price_list_from_price) == 1:
        rub, kop = *price_list_from_price, 0

    elif len(price_list_from_price) == 2:
        rub, kop = price_list_from_price

    else:
        print(f'You\' ve screwed up with {price_string}!')
        continue

    int_rub, int_kop = int(rub), int(kop)
    format_price = f'{int_rub} руб, {int_kop:02d} коп'
    new_price_list.append(format_price)

print(' '.join(new_price_list))

list_before_id = id(prices_list)

prices_list.sort()
print(prices_list)

list_after_id = id(prices_list)

if list_before_id == list_after_id:
    print('Это тот же самый объект!')

new_sorted_list = list(reversed(prices_list))
print(new_sorted_list)

if list_after_id != id(new_sorted_list):
    print('Это новый объект!')

print('Цены пяти самых дорогих товаров: ', *sorted(prices_list, reverse=True)[:5])
