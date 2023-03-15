# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных

def print_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
        print(book)


def input_data():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите данные: ') + '\n')


def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        search_list = []
        while len(search_list) != 1:
            search = input('Введите имя: ')
            search_list = list(filter(lambda x: search in x, book))
            if len(search_list) > 1:
                print('Вашему запросу подходит несколько вариантов:')
                search_list = list(map(lambda x: print(x), search_list))
                print('Дополните запрос')
            if len(search_list) == 0:
                print('По вашему запросу ничего не найдено')
        return search_list[0]


def change_data():
    file = open('data.txt', 'r', encoding='utf-8')
    new_file = open('new_data.txt', 'w', encoding='utf-8')
    book = file.read().split('\n')
    book.pop()
    search = find_data()
    for name in book:
        if search in name:
            new_file.write(input('Введите нове данные данные: ') + '\n')
        else:
            new_file.write(name + '\n')
    file.close()
    new_file.close()
    file = open('data.txt', 'w', encoding='utf-8')
    new_file = open('new_data.txt', 'r', encoding='utf-8')
    book = new_file.read().split('\n')
    book.pop()
    book = list(map(lambda name: file.write(name + '\n'), book))
    file.close()
    new_file.close()
    print("Данные перезаписаны")


def delete_data():
    file = open('data.txt', 'r', encoding='utf-8')
    new_file = open('new_data.txt', 'w', encoding='utf-8')
    book = file.read().split('\n')
    book.pop()
    search = find_data()
    for name in book:
        if search in name:
            continue
        else:
            new_file.write(name + '\n')
    file.close()
    new_file.close()
    file = open('data.txt', 'w', encoding='utf-8')
    new_file = open('new_data.txt', 'r', encoding='utf-8')
    book = new_file.read().split('\n')
    book.pop()
    book = list(map(lambda name: file.write(name + '\n'), book))
    file.close()
    new_file.close()
    print("Данные удалены")


while True:
    mode = input('Меню справочника:\n\
1 - Вывод данных\n\
2 - Ввод данных\n\
3 - Поиск данных \n\
4 - Изменение данных \n\
5 - Удаление данных \n\
0 - Выход \n\
Выберите режим работы справочника: ')
    if mode == '1':
        print(print_data())
    elif mode == '2':
        input_data()
    elif mode == '3':
        print(find_data())
    elif mode == '4':
        change_data()
    elif mode == '5':
        delete_data()
    elif mode == '0':
        break
    else:
        print('No mode')
