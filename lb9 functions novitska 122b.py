'''
Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
всіх алгоритмів тестові вихідні дані
'''
import numpy as np
import random
import time
while True:
    while True:
        try:
            answer1 = int(input("\nPlease type '1' if you want to input a sequence of integers,\ntype '2' if you want to generate a sequence of integers:"))
            if answer1 == 1: # користувач задає послідовність цілих чисел, для цього використаємо масив
                while True:
                    try:
                        number = int(input('\nInput the numbers of elements in your sequence(up to 30): '))
                        seq = np.zeros((number), dtype=int) # створюється масив довжиною заданою користувачем заповнений нулями
                        for i in range(number):
                            while True:
                                try:
                                    seq[i] = input(f'Please input {i} element: ')
                                except TypeError and ValueError:
                                    print('Error. Please input only integers.\n')
                                    continue
                                break
                    except TypeError and ValueError:
                        print('Error. Please input only integers.\n')
                        continue
                    break
                print(f'\nSequence of {number} inputed integers: {seq}')

            elif answer1 == 2:  # послідовність цілих чисел генерується рандомно
                seq = []  # у цей список будуть записуватись рандомно згенеровані елементи

                start = time.time()
                def sequence(seq, g):
                    ''' Згенерована послідовність псевдовипадкових чисел, достатня для оцінки
                        швидкості роботи алгорит-му сортування (близько 100000 цілих чисел). '''
                    while g < 1000:
                        a = random.randint(0,1000)
                        seq.append(a)
                        g += 1 # лічильник, для якого при кожній ітерації створюється елемент масиву
                    return seq, g
                    # за допомогою циклу була створена послідовність з 10000 рандомними цілими числами

                seq, comp_first_func = sequence(seq, 0)
                # з функції повернули згенерований масив,
                # а також кількість порівнянь на виконання умови
                end = time.time()
                print(f'\nGenerated sequence of 1000 random integers: {seq}')
                print(f'Time spent on generating 1000 random integers: {end-start}')
                print(f'Number of comparisons: {comp_first_func}')
                # час виконання функції є різницею значень змінної, що містить час відліку до початку виконання функції
                # і змінної, що містить час після виконання

            else:
                print("Input '1' or '2'.")
                continue
        except TypeError and ValueError:
            print('Error. Please input only integers.\n')
            continue
        break
    start1 = time.time()
    def growing_order(seq, g):
        '''
        Вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
        в порядку зростання.
        '''
        for i in range(len(seq) - 1, 0, -1):
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    g += 1 # кількість обмінів, порівнянь
        # за допомогою циклів відбувається проходження по всім елементам і порівняння кожного елемента з наступним.
        # якщо він більший за наступний, то вони міняються місцями.
        # вкінці першої ітерації першого циклу for найбільший елемент вже стоїть на останній позиції,
        # тому наступна ітерація буде здійснюватись до цього елементу, і так доки всі елементи не будуть відсортовані у порядку зростання
        return seq, g
    seq_grow, comp_second_func = growing_order(seq, 0)
    end1 = time.time()
    print(f'\nSequence in growing order: {seq_grow}')
    print(f'Time spent on sorting {len(seq)} integers in growing order: {end1 - start1}')
    print(f'Number of comparisons: {comp_second_func}, number of interchanges: {comp_second_func}')
    # час виконання функції є різницею значень змінної, що містить час відліку до початку виконання функції
    # і змінної, що містить час після виконання

    start2 = time.time()
    def descending_order(seq, g):
        '''
        Вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
        в порядку за спаданням.
        '''
        for i in range(len(seq) - 1, 0, -1):
            for j in range(i):
                if seq[j] < seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    g += 1 # кількість обмінів, порівнянь
        # за допомогою циклів відбувається проходження по всім елементам і порівняння кожного елемента з наступним.
        # якщо він менший за наступний, то вони міняються місцями.
        # вкінці першої ітерації першого циклу for найменший елемент вже стоїть на останній позиції,
        # тому наступна ітерація буде здійснюватись до цього елементу, і так доки всі елементи не будуть відсортовані у порядку спадання
        return seq, g
    seq_desc, comp_third_func = descending_order(seq, 0)
    end2 = time.time()
    print(f'\nSequence in descending order: {seq_desc}')
    print(f'Time spent on sorting {len(seq)} integers in descending order: {end2 - start2}')
    # час виконання функції є різницею значень змінної, що містить час відліку до початку виконання функції
    # і змінної, що містить час після виконання
    print(f'Number of comparisons: {comp_third_func}, number of interchanges: {comp_third_func}')

    answer = input('\nDo you want to continue? Yes-1, No-2:')
    if answer == '1':
        continue
    else:
        break