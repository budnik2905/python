# математические операции (расчёты нашей жизни)
# средняя продолжительность жизни в России (лет)
ale = 71
age = int(input('Сколько вам лет ? '))
#  +
after20 = age + 20
print('Через 20 лет вам будет ', after20)
# -
alive = ale - age
print('По статистике вам осталось жить ', alive)
#  *
count = 14400000
all_alive = count * ale
print('Среднее время жизни всех людей', all_alive)
# /
live_part = age / ale
print('Часть прожитой жизни', live_part)
# результат деления
print(type(live_part))