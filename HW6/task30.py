# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""
    array = []
    for i in range(quantity):
        array.append(first + i * diff)
    return array


a1 = int(input("Первое число: "))
n = int(input("Количество чисел: "))
d = int(input("Разность: "))
array = arithmetic_progression(a1, d, n)
print(array)
