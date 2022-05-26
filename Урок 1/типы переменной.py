person_name = 'Max'
#определяем тип переменной
print(type(person_name))
#вывод <class 'str'>

age = 30
print(type(age))
#вывод <class 'int'>

period = 3.2
print(type(period))

is_goog = True
print(type(is_goog))

person = None
print(type(person))
#Приведение типов :
birthday_year = '1988'
print(type(birthday_year))

period = 20
print(type(period))

age = int(birthday_year) + period
print(age)

some_str = birthday_year + str(period)
print(some_str)
