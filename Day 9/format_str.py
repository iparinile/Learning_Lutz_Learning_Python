print('That is %d %s bird' % (1, 'dead'))  # Выражение формата
# That is 1 dead bird
exclamation = 'Hi!'
print('The knights who say %s' % exclamation)  # Подстановка строки
# The knights who say Hi!
print('%d %s %g you' % (5, 'hi', 4.0))  # Подстановки, специфичные для типов
# 5 hi 4 you
print('%s -- %s -- %s' % (32, 3.9348, [1, 5, 3]))  # Все типы соответствуют цели %s
# 32 -- 3.9348 -- [1, 5, 3]

x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)  # integers: ...1234...1234  ...001234
x = 1.23456789
print(x)  # 1.23456789
print('%e | %f | %g' % (x, x, x))  # 1.234568e+00 | 1.234568 | 1.23457
print('%E' % x)  # 1.234568E+00
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))  # 1.23   | 01.23 | +001.2
print(('%s' % x, str(x)))  # ('1.23456789', '1.23456789')
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))  # 0.333333, 0.33, 0.3333

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})  # 1 more spam
# Шаблон с целями подстановки
reply = """  
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}  # Создание значений для подстановки
print(reply % values)  # Выполнение подстановок
# Greetings...
# Hello Bob!
# Your age is 40

food = 'spam'
qty = 10
print(vars())
# {’food’: ’spam’, ’qty': 10, ... плюс встроенные имена, установленные Python,.. }
print('%(qty)d more %(food)s' % vars())  # Переменные являются ключами в vars()
# 10 more spam

template = '{0}, {1} and {2}'  # По позициям
print(template.format('spam', 'ham', 'eggs'))  # spam, ham and eggs
template = '{motto}, {pork} and {food}'  # По ключевым словам
print(template.format(motto='spam', pork='ham', food='eggs'))  # spam, ham and eggs
template = '{motto}, {0} and {food}'  # По позициям и ключевым словам
print(template.format('ham', motto='spam', food='eggs'))  # spam, ham and eggs
template = '{}, {} and {}'  # По относительным позициям - Нововведение Python 3.1 и 2.7
print(template.format('spam', 'ham', 'eggs'))  # spam, ham and eggs

import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))  # My laptop runs linux
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))  # My laptop runs linux

somelist = list('SPAM')
print(somelist)  # ['S', 'P', 'A', 'M']
print('first={0[0]}, third={0[2]}'.format(somelist))  # first=S, third=A
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))  # first=S, last=M
parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))
# first=S, last=M, middle=['P', 'A']
