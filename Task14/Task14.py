# Задача 14. Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа n

n = 0

while (n<=0):
        n = int(input('Введите натуральное число n = '))

current_stepen = 1

print(f'Степени двойки до числа {n}\n1')

while (2*current_stepen <= n):
    print(f'{2*current_stepen}')
    current_stepen *= 2