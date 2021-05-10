# 2. Дан список:
#
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

default_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(default_list):
    if default_list[i].isdigit() or default_list[i][1:].isdigit():
        if default_list[i][0] == '+' or default_list[i][0] == '-':
            default_list_sum = default_list[i][0]
            default_list[i] = default_list_sum + default_list[i][1:].zfill(2)
        default_list[i] = default_list[i][1:].zfill(2)
        default_list.insert(i, '"')
        default_list.insert(i + 2, '"')
        i = i + 2
    i = i + 1

print('Вывод ID процесса в начале программы: ', id(default_list))

i = 0
while i < len(default_list):
    if default_list[i].isdigit() or default_list[i][1:].isdigit():
        default_list[i] = default_list[i - 1] + default_list[i] + default_list[i + 1]
        default_list.pop(i + 1)
        default_list.pop(i - 1)
    i += 1

output_default_list = ' '.join(default_list)

print(output_default_list)
print('Вывод ID процесса в конце программы: ', id(default_list))
