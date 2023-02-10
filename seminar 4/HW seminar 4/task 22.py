# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12



n = int(input("введите кол-во элементов 1-го  множества = "))
m = int(input("введите кол-во элементов 2-го  множества = "))
set1 = set(int(input("введите эл-ты 1-го множества = ")) for i in range(n))
set2 = set(int(input("введите эл-ты 2-го множества = ")) for i in range(m))

sortList = list(set1.intersection(set2))
sortList.sort()

print(*sortList)