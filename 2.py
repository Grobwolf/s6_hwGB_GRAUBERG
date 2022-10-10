# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# БЫЛО:

fib1 = fib2 = 1
n = int(input())
fib_list = []
for i in range(2, n+3):
    fib1, fib2 = fib2, fib1 - fib2
    fib_list.append(fib2)
sfib_list = fib_list.copy()
i = 0
i2 = -1
while i < len(fib_list) / 2:
    sfib_list[i], sfib_list[i2] = sfib_list[i2], sfib_list[i]
    i += 1
    i2 -= 1
for i in range(1, len(fib_list)):
    if fib_list[i] < 0:
        fib_list[i] *= -1
    sfib_list.append(fib_list[i])
print(sfib_list)


# СТАЛО:
from functools import reduce

n = int(input())+1
fib_list = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])
r_fib_list = fib_list.copy()
for i in range(0, len(fib_list), 2):
    r_fib_list[i] *= -1
i = 0
i2 = -1
while i < len(fib_list) / 2:
    r_fib_list[i], r_fib_list[i2] = r_fib_list[i2], r_fib_list[i]
    i += 1
    i2 -= 1
r_fib_list.pop()
fib = r_fib_list + fib_list
print(fib)
