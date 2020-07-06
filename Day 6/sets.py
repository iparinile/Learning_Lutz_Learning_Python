# Для чего используются множества?
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))  # {1, 2, 3, 4, 5}
L = list(set(L))  # Удаление дубликатов
print(L)  # [1, 2, 3, 4, 5]

print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))  # Найти различия в списках
# {3, 7}
print(set('abcdefg') - set('abdghij'))  # Найти различия в строках
# {'e', 'f', 'c'}
print(set('spam') - set(['h', 'a', 'm']))  # Найти различия, разнородные типы
# {'s', 'p'}
print(set(dir(bytes)) - set(dir(bytearray)))  # В bytes , но не в bytearray
# {'__getnewargs__'}
print(set(dir(bytearray)) - set(dir(bytes)))
# {'__iadd__', 'insert', 'append', 'clear', '__imul__', '__delitem__', '__setitem__', 'reverse', 'remove', '__alloc__',
# 'extend', 'copy', 'pop'}

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)  # В последовательностях порядок имеет значение
# False
print(set(L1) == set(L2))  # Проверка на равенство, нейтральное к порядку
# True
print(sorted(L1) == sorted(L2))  # Похожая проверка, но результаты упорядочены
# True
print('spam' == 'asmp', set('spam') == set('asmp'), sorted(('spam')) == sorted('asmp'))
# False True True

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print('bob' in engineers)  # Является ли сотрудник bob инженером (engineer)?
# True
print(engineers & managers)  # Кто одновременно инженер и менеджер (manager)?
# {'sue'}
print(engineers | managers)  # Все сотрудники в обеих категориях
# {'sue', 'vic', 'ann', 'tom', 'bob'}
print(engineers - managers)  # Инженеры, не являющиеся менеджерами
# {'bob', 'ann', 'vic'}
print(managers - engineers)  # Менеджеры, не являющиеся инженерами
# {'tom'}
print(engineers > managers)  # Все ли менеджеры - инженеры? (надмножество)
# False
print({'bob', 'sue'} < engineers)  # Оба ли сотрудника - инженеры? (подмножество)
# True
print((managers | engineers) > managers)  # Все сотрудники - надмножество менеджеров?
# True
print(managers ^ engineers)  # Кто находится в одной категории, но не в обеих?
# {'ann', 'bob', 'tom', 'vic'}
print((managers | engineers) - (managers ^ engineers))  # Пересечение!
# {'sue'}
