# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
#
#     просто запуск скрипта — выводить все записи;
#     запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
#     запуск скрипта с двумя числами — выводить записи,
#     начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
import math
import sys

LINE_LENGTH = 7
show_from_line = 1
show_to_line = math.inf


def show_sales(show_from_line=1, show_to_line=math.inf):
    if show_from_line < 2:
        show_from_position = 0
    else:
        show_from_position = (show_from_line - 1) * LINE_LENGTH
    show_to_position = show_to_line * LINE_LENGTH

    with open('bakery.csv', encoding='utf-8') as f:
        f.seek(show_from_position)
        line = f.readline()
        while line:
            print(line.strip())
            if show_to_position < f.tell():
                break
            line = f.readline()


if __name__ == '__main__':
    arguments = (int(arg) for arg in sys.argv[1:])

    show_sales(*arguments)
