# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.
import random 

k = int(input('Введите число для задания 33: '))
k34_1 = int(input('Введите число для задания 34 формулы 1: '))
k34_2 = int(input('Введите число для задания 34 формулы 2: '))
if k > 0 and k34_1 > 0 and k34_2 > 0:

    def func(num):
        dict_value = {}
        for i in range(num, -1, -1):
            dict_value[i] = random.randint(0, 100)
        return dict_value
    dict_k = func(k)
    dict_k34_1 = func(k34_1)  
    dict_k34_2 = func(k34_2) 

    def recursiveFunc(num,dict_value):
        if num == 0:
            return f'{dict_value[num]} = 0' 
        else:
            return f'{dict_value[num]}*x**{num} + '+ recursiveFunc(num-1,dict_value)


    path = 'TextForTask33.txt'
    data = open(path,'w')
    data.write(recursiveFunc(k,dict_k)+'\n')
    data.write(str(dict_k))
    data.close()
    #для задания 34
    path = 'TextTask34Formula1.txt'
    data = open(path,'w')
    data.write(recursiveFunc(k34_1,dict_k34_1)+'\n')
    data.write(str(dict_k34_1))
    data.close()
    #для задания 34
    path = 'TextTask34Formula2.txt'
    data = open(path,'w')
    data.write(recursiveFunc(k34_2, dict_k34_2)+'\n')
    data.write(str(dict_k34_2))
    data.close()
else:
    print('Перезадайте числа. Они должны быть больше 0')
