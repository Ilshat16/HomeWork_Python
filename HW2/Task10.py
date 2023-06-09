# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1

from random import randint

n = int(input("Число монет: "))
count_side_1 = 0
count_side_2 = 0

for _ in range(n):
    coin = randint(0, 1)
    print(coin)
    if coin == 1:
        count_side_1 += 1
    else:
        count_side_2 += 1
print()
if count_side_1 > count_side_2:
    print(count_side_2)
else:
    print(count_side_1)