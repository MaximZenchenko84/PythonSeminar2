# Задача 12: Петя и Катя - брат и сестра. Петя - студент, а Катя - школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y<=1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму сумму этих чисел S и их произведение P. Помогите Кате
# отгадать задуманные Петей числа

S = int(input('Введите сумму задуманных чисел S = '))
P = int(input('Введите произведение задуманных чисел P = '))

X=0
Y=0

for counter in range(0,S):
        if ((S-counter)*counter == P):
                Y = counter
                X = S - Y
                break
        
if ((X!=0) and (Y!=0) or (S==0) and (P==0)):
    print(f'X = {X}, Y = {Y}')
else:
    print(f'Некорректные условия')