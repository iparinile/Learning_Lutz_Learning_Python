# Примеры строковых методов: изменение строк

S = 'spammy'
S = S[:3] + 'xx' + S[5:]  # Нарезать сегменты из S
print(S)  # spaxxy

S = 'spammy'
S = S.replace('mm', 'xx')  # Заменить все mm на хх в S
print(S)  # spaxxy

# Метод replace более универсальный
print('aa$bb$cc$dd'.replace('$', 'SPAM'))
# aaSPAMbbSPAMccSPAMdd

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')  # Поиск позиции
print(where)  # Нашлась по смещению 4
# 4
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)  # xxxxEGGSxxxxSPAMxxxx

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))  # Заменить все
# xxxxEGGSxxxxEGGSxxxx
print(S.replace('SPAM', 'EGGS', 1))  # Заменить одну
# xxxxEGGSxxxxSPAMxxxx

line = 'aaa bbb ccc'
cols = line.split()
print(cols)  # ['aaa', 'bbb', 'ccc']

line = 'bob,hacker,40'
print(line.split(','))  # ['bob', 'hacker', '40']
line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))  # ["i'm", 'a', 'lumberjack']

line = 'The knights who say Hi!\n'
print(repr(line.rstrip()))  # 'The knights who say Hi!'
print(repr(line.upper()))  # 'THE KNIGHTS WHO SAY HI!\n'
print(line.isalpha())  # False
print(line.endswith('Hi!\n'))  # True
print(line.startswith('The'))  # True
# Альтернатива:
print(repr(line))  # 'The knights who say Hi!\n'
print(line.find('Hi') != -1)  # Поиск через вызов метода или выражение
# True
print('Hi' in line)  # True
sub = 'Hi!\n'
print(line.endswith(sub))  # Проверка наличия подстроки в конце через вызов метода или срез
# True
print(line[-len(sub):] == sub)  # True


