#  Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
#  Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
#  арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных
#  на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

print("Введите число арбузов: A")
A = int(input())
weight = []
for i in range(A):
    weight.append(int(input('Введите вес выбранного арбуза')))
weight_min = weight[0]
weight_max = weight[0]
for i in range(len(weight)):
    if weight[i] > weight_max:
        weight_max = weight[i]
    elif weight[i] < weight_min:
        weight_min = weight[i]
print(weight_max)
print(weight_min)




