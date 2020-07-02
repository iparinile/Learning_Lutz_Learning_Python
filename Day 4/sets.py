# По-русски - множества
x = set('abcde')
y = set('bdxyz')
print(x)  # {'d', 'c', 'b', 'a', 'e'}

print(x - y)  # Разность
# {'c', 'a', 'e'}
print(x | y)  # Объединение
# {'b', 'a', 'x', 'y', 'c', 'e', 'd', 'z'}
print(x & y)  # Пересечение
# {'b', 'd'}
print(x ^ y)  # Исключающее ИЛИ
# {'e', 'a', 'z', 'c', 'x', 'y'}
print(x > y, x < y)  # Надмножество/подмножество
# False False
print('e' in x)  # Проверка членства
# True

z = x.intersection(y)  # То же, что и x & y
print(z)  # {'b', 'd'}
z.add('SPAM')  # Вставка одного элемента
print(z)  # {'d', 'SPAM', 'b'}
z.update(set(['X', 'Y']))  # Слияние: объединение на месте
print(z)  # {'X', 'd', 'SPAM', 'Y', 'b'}
z.remove('b')  # Удаление одного элемента
print(z)  # {'SPAM', 'd', 'Y', 'X'}
