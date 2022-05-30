# варианты перебора словаря
# по ключам
# по значениям
# по парам ключ, значение
friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}
# по ключам
for key in friend.keys():
    print(key)
# чтобы получить значения берём словарь и в скобках key
    print(friend[key])
# тоже самое ,если не будем указывать keys

for key in friend:
    print(key)
    print(friend[key])

# если не нужны ключи ,нужны только значения
for val in friend.values():
    print(val)

# пары ключ значение
# будем перебирать пары в виде кортежа
for item in friend.items():
# метод items возвращает список из кортежа
    print(item)

# так же можем получить в одну переменную ключ
# в другую значение делаем две переменные key и val
for key, val in friend.items():
    print(key)
    print(val)

