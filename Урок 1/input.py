result = input()
print('Ползователь ввел', result)
name = input('Как тебя зовут : ')
print('Привет', name)
# Тип введенных данных
# Для программы результатом ввода всегда будет строка
# тип данных (str)
name = input('Как вас зовут?: ')
print(type(name))
age = input('Сколько вам лет ?: ')
print(type(age))
is_love = input('Вы любите pythoh?: ')
print(type(is_love))
age = int(input('Сколько вам лет ?: '))
period = 20
age_period = age + period
print('Через', period, 'вам будет',age_period)
