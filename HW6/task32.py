# Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума)

def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num) """
    ind_list = []
    for i in range(len(num_lst)):
        if num_lst[i] >= min_num and num_lst[i] <= max_num:
            ind_list.append(i)
    return ind_list


print("Массив чисел:")
# num_lst = list(map(int, input().split()))
# n1 = int(input("Первое число: "))
# n2 = int(input("Второе число: "))
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n1 = 3
n2 = 6
print("Индексы элементов в заданном диапазоне:", is_in_mass(num_lst, n1, n2))
