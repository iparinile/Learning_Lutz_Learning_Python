f = open('data.txt', 'w')  # Создать новый файл в режиме записи ('w')
f.write('Hello\n')  # Записать в него строки символов
f.write('world\n')
f.close()  # Закрыть для сбрасывания буферов вывода на диск

f = open('data.txt', 'r')  # 'r' (чтение) - стандартный режим обработки
text = f.read()  # Прочитать все содержимое файла в строку
print(text)
# Hello
# world
print(text.split())  # Содержимое файла - всегда строка
# ['Hello', 'world']
for line in open('data.txt'):
    print(line)

import struct
packed = struct.pack('>i4sh', 7, b'spam', 9)  # Создание упакованных двоичных данных
print(packed)  # b'\x00\x00\x00\x07spam\x00\t'  # 10 байтов, не объекты и не текст
file = open('data.bin', 'wb')  # Открыть двоичный файл для записи
file.write(packed)  # Записать упакованные двоичные данные
file.close()

data = open('data.bin', 'rb').read()  # Открыть/прочитать двоичный файл данных
print(data)  # b'\x00\x00\x00\x07spam\x00\t'
print(data[4:8])  # b'spam'     # Нарезать байты в середине
print(list(data))  # [0, 0, 0, 7, 115, 112, 97, 109, 0, 9]   # Последовательность 8-битных байтов
print(struct.unpack('>i4sh', data))  # (7, b'spam', 9)      # Снова распаковать в объекты
