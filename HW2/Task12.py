# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y ≤ 1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Ввод:
# 7
# 12
# Вывод
# 3 4 или 4 3

# s = x + y
# p = x * y

s = int(input("Сумма чисел x и y: "))
p = int(input("Произведение чисел x и y: "))
have_answer = 0

for x in range(1, s + 1):
    y_ = s - x
    if p / x == y_:
        print(x, y_)
        have_answer = 1
        
if have_answer == 0:
    print("Ответов нет")
