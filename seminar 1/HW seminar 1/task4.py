# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите размер "n" шоколадки')
n = int(input())
print(('Введите размер "m" шоколадки'))
m = int(input())
print('Введите количество "k" долек которые хотите отломить от шоколадки')
k = int(input())
if k % n == 0 or k % m == 0:
    print('Yes')
else:
    print('No')