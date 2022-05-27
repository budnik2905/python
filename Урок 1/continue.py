#Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
# Вывод чётных чисел от 0 до n
number = 0
n = int(input('Введите n: '))
while number <= n:
    if number % 2 == 0 :
        number += 1
        continue
    print(number)