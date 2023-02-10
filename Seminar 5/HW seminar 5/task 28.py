# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

a = int(input('Введите число А ='))
b = int(input('Введите число B ='))

# def sum(a,b):
#     if a and b < 0:
#         return (a+b)
#     return (a+b)
# print(a+b)

def sum(a, b):
    if b == 0:
        if a == 0:
            return 0
        return sum(a - 1, b) + 1
    return sum(a, b - 1) + 1
print(sum(a, b))