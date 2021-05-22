# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def odd_nums(n):
    return (odd_num for odd_num in range(1, n, 2))


check = odd_nums(16)

print(list(check))
