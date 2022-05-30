# Словарь dict
# неупорядочные коллекции произвольных объектов с доступом по ключу
# обозначается словарь в фигурных скобках в которых мы указываем ключ и значение
# my_dict = {key1:val1,key2:val2,...}
# dog = {'name':'Rocky',age:3}
friends = ['Max','Leo','Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))
# как добавить возраст другу ? объявим переменную friend
# которая будет словарём
# в словаре мы указываем пары ключ и значение
# ключом будет name , значение Max
friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))
# ОСНОВНЫЕ ДЕЙСТИЯ СО СЛОВАРЁМ
# получение элемента по ключу friend['name']
# добавление значения friend['has_car']=True
# изменение значения friend['has_car'] = False
# удаление значения remove friend['age']
# оператор in 'age' in friend

# узнаем сколько лет ,вместо индекса указываем ключ
print(friend['age'])
# по ключу получаем значение

# теперь добавим что-нибудь в словарь
friend['has_car']= True
print(friend)
friend['has_car']= False
print(friend)
# с одним ключом может быть одно значение

# теперь удалим какой нибудь элемент воспользуемся оператором del
# указываем переменную и ключ значения которого хотим удалить

del friend['age']
print(friend)
# удалится сразу пара ,ключ и значение

# с помощью оператора in можем проверить есть ли какой-нибудь ключ в словаре

if 'age' in friend:
    print('Есть возраст')

if 'has_car' in friend:
    print('Есть машина')
