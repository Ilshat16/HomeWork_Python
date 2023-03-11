# Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

A = 0
B = 10
n = int(input("Введите количество элементов в массиве: "))

number_list = [randint(A, B) for _ in range(n)]
print(number_list)

x = int(input("Введите любое число: "))
minDiff = 10000
result = 0

for num in number_list:
    if abs(num - x) < minDiff:
        minDiff = abs(num - x)
        result = num

print(f"Ближайшее по величине элемент к {x} является {result}")
