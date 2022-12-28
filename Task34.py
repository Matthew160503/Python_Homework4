# Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('TextTask34Formula1.txt') as file:
    lines1 = file.readlines()
lines1 = ''.join(lines1[1])      


with open('TextTask34Formula2.txt') as file:
    lines2 = file.readlines()
lines2 = ''.join(lines2[1])      


def Transformation(lines):
    #Удаляем ненужные символы
    lines_update = (((lines.translate({ord(','): None})).translate({ord('{'): None})).translate({ord('}'): None})).translate({ord(':'): None})

    #Приводим к списку для дальнейшей работы
    our_list = lines_update.split()
    result = list(map(int, our_list))

    #Создаем словарь с элементами многочлена
    dict = {}
    for i in range(len(result)):
        if i % 2 == 0:
            dict[result[i]] = result[i+1]

    return dict

dict1 = Transformation(lines1)
dict2 = Transformation(lines2)

if dict1.keys() != dict2.keys():
    if dict1.keys() < dict2.keys():
        max_key = max(dict2.keys())
        dict1[max_key] = 0
    else:
        max_key = max(dict1.keys())
        dict2[max_key] = 0
sum_dict = {}
for i in dict2:
    sum_dict[i] = dict1[i] + dict2[i]
print(sum_dict)


def recursiveFunc1(num,dict_value):
        if num == 0:
            return f'{dict_value[num]} = 0' 
        else:
            return f'{dict_value[num]}*x**{num} + '+ recursiveFunc1(num-1,dict_value)

path = 'Task34SumOfFormules.txt'
data = open(path,'w')
data.write(recursiveFunc1(max_key,sum_dict)+'\n')
data.write(str(sum_dict))
data.close()