# Логические операции
# ==  равно
# !=  не равно
# >   больше
# >=  больше или равно
# <   меньше
# <=  меньше или равно
# средняя продолжительность жизни
ale = 71
age = int(input('Сколько вам лет ?'))
print('Ваш возраст равен средней продолжительности жизни',ale == age)
print('Ваш возраст Не равен средней продолжительности жизни',ale != age)
print('Ваш возраст меньше средней продолжительности жизни', age < ale)
print('Ваш возраст больше средней продолжительности жизни', age > ale)
print('Ваш возраст меньше или равен средней продолжительности жизни', age <= ale)
print('Ваш возраст больше или равен средней продолжительности жизни', age >= ale)

print('У вас юбилей : ', age % 5 == 0)
# Сложные логические выражения
# and - и (ИСТИНА когда все ИСТИНА иначе ЛОЖЬ)
# or - или (ЛОЖЬ когда всё ЛОЖЬ иначе ИСТИНА )
# not - не (ИСТИНА когда ЛОЖЬ ,ЛОЖЬ когда ИСТИНА)
