bob1 = dict(name='Bob', job='dev', age=40)  # Как еще можно создать словарь
print(bob1)  # {'name': 'Bob', 'job': 'dev', 'age': 40}

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))  # То же самое
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec['name'])  # 'name' - вложенный словарь
# {'first': 'Bob', 'last': 'Smith'}
print(rec['name']['last'])  # Индексация во вложенном словаре
# Smith
print(rec['jobs'])  # 'jobs' - вложенный список
# ['dev', 'mgr']
print(rec['jobs'][-1])  # Индексация
# mgr
rec['jobs'].append('janitor')  # Расширение списка названий должностей на месте
print(rec)  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'janitor'], 'age': 40.5}

D = {'a': 1, 'b': 2, 'c': 3}
print('f' in D)  # False
if 'f' not in D:
    print('missing')
# missing

Ks = list(D.keys())  # Неупорядоченный список ключей
print(Ks)  # ['a', 'b', 'c']
Ks.sort()  # Отсортированный список ключей
for key in Ks:  # Проход по отсортированным ключам
    print(key, '=>', D[key])
# a => 1
# b => 2
# c => 3

# Альтернативный способ:
for key in sorted(D):
    print(key, '=>', D[key])
