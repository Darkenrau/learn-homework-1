"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def some_func(a, b):
    if type(a) != str:
        return 0
    elif type(b) != str:
        return 0

    if len(a) == len(b):
        return 1
    
    if len(a) > len(b):
        return 2
    
    if len(a) != len(b) and b == 'learn':
        return 3