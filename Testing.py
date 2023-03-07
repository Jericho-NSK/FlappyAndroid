from io import BytesIO

from PIL import Image

icon = Image.open(r'G:\Python\FlappyAndroid\images\originals\original_big_jump.png', mode='r').resize((620 // 5, 620 // 5)).crop()  #
# требуемый размер
# icon = Image.open(r'G:\Python\PyPython\2023-03 Pygame\cart.png', mode='r').reduce(5).crop()  # Уменьшение в 10 раз
icon_arr = BytesIO()
icon.save(icon_arr, format='PNG')
icon_arr = icon_arr.getvalue()
# print(icon_arr)  # <- скопировал результат из консоли в новую переменную byte_icon

byte_icon = b'...'  # <- тут длинная строка в байтовом виде. Весь код выше можно удалять.
# Кроме "from tkinter import PhotoImage", так как он еще нужен ниже

# final_img = PhotoImage(data=byte_icon, format='png')

with open(r'G:\Python\FlappyAndroid\images\big_jump.png', 'wb') as file:  # Сохранение в новый файл
    file.write(icon_arr)
