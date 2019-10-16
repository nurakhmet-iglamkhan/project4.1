# Имеется двумерный массив 10х2 в виде списка. Сделать консольную программу,
# которая вводит данные массива с клавиатуры, осуществляет заданый вариантом
# алгоритм и выводит получиенный список-результат на экран

import math

# Функция создание массива
def input_array(row, column):
    array = []
    for i in range(0, row):
        sub_array = []
        for j in range(column):
            if j == 0:
                print('Введите число [ ', i, ' ]', '[ ', j, ' ]:')
                number = int(input())
                sub_array.append(number)
            if j == 1:
                sub_array.append(0)
        array.append(sub_array)
    return array

# Функция вывода массива
def output_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print('')

def output_arrayAns(array):
    print()
    for i in range(len(array)):
        print('[', array[i][0], ']', '\t', '{:.2f}'.format(array[i][1]))

def main():
    array = input_array(10, 2)
    output_array(array)

    for i in range(0, 10):
        proiz = 1
        summa = 0
        for j in range(i):
            if array[j][0] == 0:
                summa += array[j][0]
                proiz *= array[j][0]
        if array[i] == 0:
            answer = 0
        else:
            summa += array[i][0]
            numerator = ((math.cos(array[i][0]**2)) / (math.factorial(i) + math.sin(array[i-1][0])**2))**(1.0 / 2)*proiz
            denominator = summa
            value = numerator / denominator
            try:
                answer = value
            except ValueError:
                print("В python нельзя  возвести %d" % value, end='')
                print("в дробную степень. Число будет пропущено")
                continue
        array[i][1] = answer
    print()
    output_arrayAns(array)

if __name__ == '__main__':
    main()