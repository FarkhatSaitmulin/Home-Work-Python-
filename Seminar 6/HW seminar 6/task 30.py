# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


firstElement, step, n = (map(int,input().split( )))
listX = [firstElement]
for i in range(n-1):
    listX.append(listX[i]+step)
print(listX)


