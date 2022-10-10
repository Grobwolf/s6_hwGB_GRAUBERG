# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
#
# Пример:
#
# Для n = 6 -> 14.072
# ***********
# БЫЛО:

n = int(input())
coll = []
result = 1
for i in range(1, n+1):
    result = (1+1/i)**i
    coll.append(result)
summ = 0
for i in range(0, n):
    summ += coll[i]
print(round(summ, 3))

# СТАЛО:

n = int(input())
coll = [(1 + 1 / i)**i for i in range(1, n+1)]
print(round(sum(coll), 3))
