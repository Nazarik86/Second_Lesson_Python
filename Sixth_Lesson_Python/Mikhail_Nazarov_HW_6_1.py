# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
remote_addr = []
request_type = []
requested_resource = []

with open('nginx_logs.txt', encoding='utf-8') as logs_file:
    for line in logs_file:
        remote_addr.append(line.split()[0])
        request_type.append(line.split()[5].replace('"', ''))
        requested_resource.append(line.split()[6])
summary = list(zip(remote_addr, request_type, requested_resource))
print(summary)
