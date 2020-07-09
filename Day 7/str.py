s = 'a\0b\0c'
print(s)  # a b c
print(len(s))  # 5
print(repr(s))  # 'a\x00b\x00c'
s = '\001\001\x03'
print(repr(s))  # '\x01\x01\x03'
print(len(s))  # 3

S = 's\tp\na\x00m'
print(repr(S))  # 's\tp\na\x00m'
print(len(S))  # 7
print(S)
#  s	p
# a m

path = r'C:\new\text.dat'
print(repr(path))  # Отображает в формате, как в коде Python
# 'C:\\new\\text.dat'
print(path)  # Отображает в формате, дружественном к пользователю
# C:\new\text.dat
print(len(path))  # Длина строки
# 15
