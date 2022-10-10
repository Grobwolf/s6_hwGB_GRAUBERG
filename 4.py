# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# БЫЛО:

numbers = list(map(int, input().split()))
result = []
i = 0
i2 = -1
while i < len(numbers)/2:
    result.append(numbers[i] * numbers[i2])
    i += 1
    i2 -= 1
print(numbers, "=>", result)


# СТАЛО:

numbers = list(map(int, input().split()))
i = 0
i2 = -1
result = (lambda x, y: x * y)
res = []
while i < len(numbers)/2:
    res.append(result(numbers[i], numbers[i2]))
    i += 1
    i2 -= 1
print(numbers, "=>", res)
