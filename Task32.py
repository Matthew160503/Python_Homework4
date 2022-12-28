# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

our_list = [1,3,2,3,1,4,5,6,4,7,8]
res = []

for i in range(len(our_list)):
    flag = 1
    for j in range(len(our_list)):
        if our_list[i] == our_list[j] and i != j:
            flag = 0
            break
    if flag == 1:
        res.append(our_list[i])
print(f'Список из неповторяющихся чисел: {res}')