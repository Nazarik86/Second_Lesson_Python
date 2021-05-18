# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
# Например:
#
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": "Петр Алексеев"
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Сможете ли вы вернуть отсортированный по ключам словарь?


def thesaurus_adv(*full_names_list: str):
    dictionary_reg = {}

    for full_name in full_names_list:
        name, surname = full_name.split()
        surname_dictionary_reg = dictionary_reg.setdefault(surname[0], {})
        name_dictionary_reg = surname_dictionary_reg.setdefault(name[0], [])
        name_dictionary_reg.append(full_name)

    return dictionary_reg


print(
    thesaurus_adv(
        "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"
    )
)
