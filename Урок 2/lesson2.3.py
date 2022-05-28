# форматирование строк
name = 'leo'
age = 30
print(type(age))
# конкатенация склеиваем несколько строк с помощью операции сложения
hello_str = 'Привет, ' + name + ' тебе ' + str(age) + 'лет'
print(hello_str)

# % форматирование
hello_str = 'Привет %s тебе %d лет'%(name,age)
print(hello_str)
# format() поддерживает передачу значений по позиции и по имени
hello_str = 'Привет {} тебе {} лет'.format(name,age)
print(hello_str)
# f-стороки появилось в Python 3.6
hello_str = f'Привет ,{name} тебе {age} лет'
print(hello_str)