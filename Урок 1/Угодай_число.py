number = 44
value = int(input('Введите число от 1 до 100: '))
if value == number:
    print('Вы угадали !')
else:
    if value > number:
        print('Нужно меньше')
    else:
        print('Нужно больше')

