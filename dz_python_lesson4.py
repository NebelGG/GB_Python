'''Задание 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv

file_name, worked_hour, rate, benefit = argv

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Your pay is equal {calculation}")

'''Задание 2
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''
'''Вариант с генератором'''
my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)

''' Вариант с циклом
i = 0
new= []
for el in my_list:
    if el > my_list[i-1]:
        new.append(el)
    i+=1
print(new)
'''
'''Задание 3
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.'''

numbers = range(20, 241)
new_list = [el for el in numbers if el%20==0 or el%21==0]
print(new_list)

'''Задание 4
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.'''
from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [1, 2, 2, 3, 4, 1, 2]
new = [el for el in my_list if my_list.count(el)==1]
print(new)

'''Задание 5
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))

'''Задание 6
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.'''
from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_count_func(start_number = int(input("enter start number: ")), stop_number = int(input("enter stop number: ")))
my_cycle_func(my_list = [1, 2], iteration = int(input("enter iteration: ")))

'''Задание 7
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''
def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)

