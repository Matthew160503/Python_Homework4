#Вычислить число с заданной точностью
import math

accuracy = input('Введите желаемую точность: ')
string_pi = str(math.pi)
res = string_pi[0:len(accuracy)]
print(f'Округления числа Пи до желаемой точности = {res}')