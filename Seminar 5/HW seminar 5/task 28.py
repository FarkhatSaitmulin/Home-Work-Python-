# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

a = int(input('Введите число А ='))
b = int(input('Введите число B ='))

def sum(a,b):
    if a and b < 0:
        return (a+b)
    return (a+b)

print(sum(a,b))