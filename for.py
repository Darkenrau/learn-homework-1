"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

classes = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5a', 'scores': [5,4,4,5,3]},
    {'school_class': '7a', 'scores': [3,1,5,5,2]}
]

school_summ = 0
len_all = 0

for clasz in classes:
    class_summ = 0
    for mark in clasz['scores']:
        
        class_summ += mark  
    class_average = class_summ/len(clasz['scores'])
    
    print(class_average)
    
    school_summ += class_summ
    
    len_all += len(clasz['scores'])

school_average = school_summ/len_all

print(school_average)