# Функция len и методы списка (сколько в нем элементов)
# friends.append('Ron')- добавление нового элемента
# friends.pop() - удаляем последний элемент и возвращаем его
# friends.clear() - очищаем весь список
# friends.remove('Ron') - удаление объекта из списка
# del friends[0]- удаление элемента по индексу

# Смотрим длину списка len
friends = ['Max', 'Leo', 'Kate']
print(friends)
print(len(friends))

# добавляем новые элементы в список append
friends.append('Ron')
print(friends)

# удаляем элементы метод pop() удалит последний элемент
print(friends.pop())
print(friends)

# очищаем весь список clear()
friends.clear()
print(friends)

# вернём друзей на место ,переопредилим переменную friends
friends = ['Max', 'Leo', 'Kate']

# удалим элемент по значению remove
friends.remove('Kate')
print(friends)

# удаление элемента через функцию del по номеру индекса
del friends[0]
print(friends)



