# Когда нам может помочь range

winners = ['Max','Leo','Kate']

# простой перебор
for winner in winners:
    print(winner)

# что делать если нам нужно вывести место победителя ?
# использовать while ?
# или есть способ лучше ?

# вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]
for number in numbers:
    print(number)
# как это сделать если цифр будет 100 ? 1000 ?
# использовать while ?
# или есть способ лучше ?
# Функция range
# Позволяет создать последовательность целых чисел
# Чаше всего используется с циклом for
numbers = range(10)
print(numbers)
print(type(numbers))
# если хотим посмотреть числа,можно воспользоваться привидению к типу list -список
print(list(numbers))

numbers = range(80)
print(list(numbers))

winners = ['Max','Leo','Kate']
# простой перебор
for winner in winners:
    print(winner)

# используем range
# переменная счётчика будет i потому что будем перебирать индексы
for i in range (len(winners)):
    #print(i)
    #print(i, ')', winners[i])
    print(i + 1, ')', winners[i])





