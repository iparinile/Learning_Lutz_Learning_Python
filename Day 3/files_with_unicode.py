s = 'sp\xc4m'  # Текст Unicode, отличающийся от ASCII
print(s)  # spÄm
print(s[2])  # Ä

file = open('unidata.txt', 'w', encoding='utf-8')  # Записать/закодировать текст UTF-8
file.write(s)  # Записано 4 символа
file.close()
text = open('unidata.txt', encoding='utf-8').read()  # Прочитать/декодировать текст UTF-8
print(text)  # spÄm
print(len(text))  # 4 символа (кодовые точки)

raw = open('unidata.txt', 'rb').read()  # Читать закодированные байты
print(raw)  # b'sp\xc3\x84m'
print(len(raw))  # 5 байтов в кодировке UTF-8
# 5
print(text.encode('utf-8'))  # Вручную кодировать в байты
# b'sp\xc4m'
print(raw.decode('utf-8'))  # Вручную декодировать в байты
# spÄm

print(text.encode('latin-1'))  # Байты отличаются от других
# b'sp\xc4m'
print(text.encode('utf-16'))
# b'\xff\xfes\x00p\x00\xc4\x00m\x00'
print(len(text.encode('latin-1')), len(text.encode('utf-16')))  # 4 10
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))  # Но декодируются в ту же самую строку
# spÄm
