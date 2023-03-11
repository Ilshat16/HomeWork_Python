# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"

s = int(input())

if s < 6 and s > 0:
    print("Неверное S")
else:
    jurPS = int(s / 6)
    jurK = jurPS * 4
    print(jurPS, jurK, jurPS)