# 2. Дан список:
#
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

# С ковычками так и не разобрался, в выведенном списке, но после просмотра варианта решения,
# понял что изначально не так начал делать. Смысла нет копипастить и поэтому сдам как есть в сыром варианте.
# С выводами промежуточных значений.

default_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

i = 0

for i in range(len(default_list)):
    if default_list[i].isdigit() or default_list[i][1:].isdigit():
        number = int(default_list[i])
        if default_list[i][0] == '+' or default_list[i][0] == '-':
            default_list_sum = default_list[i][0]
            default_list[i] = default_list_sum + default_list[i][1:].zfill(2)
            print('Вывод с +/-: ', default_list[i])
            new_list.append(default_list[i])
        elif number > 0:
            print('default_list[i]: ', default_list[i])
            print('number: ', number)
            print('zfill: ', default_list[i].zfill(2))
            print((type(number)))
            new_list.append(default_list[i].zfill(2))
    else:
        new_list.append(default_list[i])

print('new_list: ', new_list)
new_list_sum = []

for i in range(len(new_list)):
    if new_list[i].isdigit() or new_list[i][1:].isdigit():
        new_sum = new_list[i]
        new_list_sum = ' '.join(f'"{new_sum}"' for new_sum in new_list[i])
        # new_list_sum.insert(i, '"')
        # new_list_sum.insert(i + 2, '"')
        print('new_sum: ', new_sum)
        print('new_list_sum', new_list_sum)
