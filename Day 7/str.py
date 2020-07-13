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

print('_' * 10)

print('spam' in 'abcspamkkj')  # True

print(ord('s'))  # 115
print(chr(115))  # s

S = '5'
S = chr(ord(S) + 1)
print(S)  # 6
S = chr(ord(S) + 1)
print(S)  # 7

B = '1101'  # Преобразование двоичных цифр в целое число с помощью ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)  # 13
print(int('1101', 2))  # Преобразование строки двоичных цифр в целое: встроенная функция
# 13
print(bin(13))  # Преобразование целого в строку двоичных цифр: встроенная функция
# 0b1101
