# для разных типов данных ,СТРОКА.СПИСОК И КОРТЕЖ
# можем применять одинаковые функции
friend_name = 'Max'
friends = ['Max','Leo','Kate']
roles = ('admin','quest','user')

# Типы данных
print(type(friend_name))
print(type(friends))
print(type(roles))

# Индексация
print(friend_name[1])
print(friends[1])
print(roles[1])

# Срезы
print(friend_name[1:1])
print(friends[1:])
print(roles[1:])

# Длина
print(len(friend_name))
print(len(friends))
print(len(roles))

# Все эти типы данных можно обобщить в одно понятие последовательности
# контейнер ,элементы которого представляют собой некую последовательность
# могут быть как изменяемыми (список), и неизменяемыми (кортеж,строка)
# реализует определённые методы (доступна индексация,взятие длины,....
# можно использовать цикл for
friend_name = 'Max'
friends = ['Max','Leo','Kate']
roles = ('admin','quest','user')

# Если объект содержит реализацию методов последовательности
# - он будет считаться последовательностью
# оператор in может проверить вхождение элемента в последовательность
if 'Max' in friends:
    print('У меня есть этот друг')
if 'M' in friend_name:
    print('Буква М есть в имени друга')

# цикл for позволяет перебирать элементы последовательности по очереди
# - не применяя при этом цикл while
# Для примера используем цикл while ,чтобы это сделать нам нужен счётчик
# например переменная i
i = 0
# будем перебирать элементы , пока i меньше < friends (то есть пока не привысил длину friends)
while i < len(friends):
# будем печатать элемент который берём из индекса ,получаем нашего friend
# берём друзей и по индексу получаем какого то друга
    friend = friends[i]
# после этого выводим на экран
    print(friend)
# самое главное когда используем цикл while не забывать прибавлять счётчик
# - иначе получится бесконечный цикл
    i += 1
# мы получим по очереди друзей
# Цикл for
# Позволяет перебирать элементы последовательности
# - по порядку без указания индекса
# for friend in friends:
#      print(friend)
# Заканчивается выполнение когда заканчивается последов.элементов
for friend in friends:
    print(friend)
# по очереди возьмёт все элементы и напечатает

for letter in friend_name:
    print(letter) # так это строка берёт все элементы по очереди пока не закон.

# перебор кортежа
for role in roles:
    print(role)
# for vs while
# Преимущество следует отдавать циклу for
# Особенно при переборе последовательности
# И когда нам не нужно манипулировать счётчиком индекса и условием цикла
#

