# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input('введите натуральное число: '))
list_res = []
i = 2

while i <= num:
    if num % i == 0:
        list_res.append(i)
        num /= i
    else:
        i += 1
print(list_res)