M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

col2 = [row[1] for row in M]  # Собрать элементы в столбце 2
print(col2)  # [2, 5, 8]

print([row[1] + 1 for row in M])  # Добавить 1 к каждому элементу в столбце 2
# [3, 6, 9]
print([row[1] for row in M if row[1] % 2])  # Отфильтровать нечетные элементы
# [5]

diag = [M[i][i] for i in [0, 1, 2]]  # Собрать диагональ из матрицы
print(diag)  # [1, 5, 9]
doubles = [c * 2 for c in 'spam']  # Повторить символы в строке
print(doubles)  # ['ss', 'pp', 'aa', 'mm']

print({sum(row) for row in M})  # Создать множество сумм элементов в строках
# {24, 6, 15}
print({i: sum(M[i]) for i in range(3)})  # Создать таблицу ключей/значений сумм элементов в строках
# {0: 6, 1: 15, 2: 24}

print([ord(x) for x in 'spaam'])  # Список порядковых чисел для символов
# [115, 112, 97, 97, 109]
print({ord(x) for x in 'spaam'})  # Множество с удаленными дубликатами
# {112, 97, 115, 109}
print({x: ord(x) for x in 'spaam'})  # Словарь с уникальными ключами
# {'s': 115, 'p': 112, 'a': 97, 'm': 109}
print((ord(x) for x in 'spaam'))  # Генератор значений
# <generator object <genexpr> at 0x037CC8E8> (Значние генератора меняется каждый раз. Почему так я не понимаю,
# но в книге говорится что это будет объяснено позже.)
