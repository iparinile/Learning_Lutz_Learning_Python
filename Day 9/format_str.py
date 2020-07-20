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

# 251 стр