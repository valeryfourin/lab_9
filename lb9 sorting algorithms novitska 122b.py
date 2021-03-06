'''
Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
всіх алгоритмів тестові вихідні дані
Виконати сортування масиву цілих чисел Ai,i = 0,(N−1) в порядку зростання / за спаданням елементів.
'''
import numpy as np
import random
import time
while True:
    while True:
        try:
            number = int(input('\nInput the numbers of elements in your sequence: '))
            answer_arr = int(input("\nPlease type '1' if you want to input integers,"
                                "\ntype '2' if you want to generate integers:"))
            answer_order = int(input("\nPlease type '1' if you want to sort in growing order,"
                                "\ntype '2' if you want to sort in descending order:"))
            answer_sort = int(input("\nPlease type '1' if you want to use bubble sort,"
                                "\ntype '2' if you want to use selection sort,"
                                "\ntype '3' if you want to use insertion sort:"))
            if answer_arr == 1:  # користувач задає послідовність цілих чисел, для цього використаємо масив
                seq = np.zeros((number), dtype=int)  # створюється масив довжиною заданою користувачем заповнений нулями
                for i in range(number):
                    while True:
                        try:
                            seq[i] = input(f'Please input {i} element: ')
                        except TypeError and ValueError:
                            print('Error. Please input only integers.\n')
                            continue
                        break

            elif answer_arr == 2: # послідовність цілих чисел генерується рандомно
                seq = []  # у цей список будуть записуватись рандомно згенеровані елементи
                def sequence(seq):
                    ''' Згенерована послідовність псевдовипадкових чисел, достатня для оцінки
                        швидкості роботи алгорит-му сортування. '''
                    i = 0  # лічильник, для якого при кожній ітерації створюється елемент масиву
                    while i < number:
                        a = random.randint(0, 1000)
                        seq.append(a)
                        i += 1
                    return seq
                    # за допомогою циклу була створена послідовність з рандомними цілими числами,
                    # кількість яких задав користувач
                sequence(seq)
            else:
                print("Input '1' or '2'.")
                continue
            print(f'\nGenerated sequence of {number} random integers: {seq}')
        except TypeError and ValueError:
            print('Error. Please input only integers.\n')
            continue
        break


    def growing_order_bubble(seq, comp, t):
        ''' Сортування бульбашкою за зростанням '''
        start = time.time()
        for i in range(len(seq) - 1, 0, -1):
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    comp += 1 # кількість обмінів, порівнянь
        # за допомогою циклів відбувається проходження по всім елементам і порівняння кожного елемента з наступним.
        # якщо він більший за наступний, то вони міняються місцями.
        # вкінці першої ітерації першого циклу for найбільший елемент вже стоїть на останній позиції,
        # тому наступна ітерація буде здійснюватись до цього елементу, і так доки всі елементи не будуть відсортовані у порядку зростання
        end = time.time()
        t = end - start
        # час виконання функції є різницею значень змінної, що містить час відліку до початку виконання функції
        # і змінної, що містить час після виконання
        return seq, comp, t



    def descending_order_bubble(seq, comp, t):
        ''' Сортування бульбашкою за спаданням '''
        start = time.time()
        for i in range(len(seq) - 1, 0, -1):
            for j in range(i):
                if seq[j] < seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    comp += 1 # кількість обмінів, порівнянь
        # за допомогою циклів відбувається проходження по всім елементам і порівняння кожного елемента з наступним.
        # якщо він менший за наступний, то вони міняються місцями.
        # вкінці першої ітерації першого циклу for найменший елемент вже стоїть на останній позиції,
        # тому наступна ітерація буде здійснюватись до цього елементу, і так доки всі елементи не будуть відсортовані у порядку спадання
        end = time.time()
        t = end - start
        return seq, comp, t


    def growing_order_selection(seq, comp, inter, t):
        ''' Сортування вибором за зростанням '''
        start = time.time()
        for i in range(len(seq)-1): # ітерація по всім елементам масиву
            min_el = i 
            # в цьому лічильнику буде зберігатись індекс останнього елемента відсортованої частини масиву, 
            # який є найменшим елементом для кожної ітерації. на початку ітерації це перший елемент
            for j in range(i+1, len(seq)): # ітерація по невідсортованій частині масиву
                if seq[j] < seq[min_el]: 
                    # якщо елемент ітерації менший за елемент з індексом min_el, то в цю змінну записується його індекс
                    min_el = j
                    comp +=1 # к-ть порівнянь
            if min_el != i:
                seq[i], seq[min_el] = seq[min_el], seq[i]
                # якщо після пройдення ітерації по масиву знайдениий найменший елемент не дорівнює першому
                # (відносно певної ітерації, не обов*язково перший у масиві), індекс якого записуєтсья у змінну min_el
                # на початку кожної ітерації, то потрібно здійснити обмін цього елемента з тим, у якого індекс і,
                # щоб найменші елементи розташовувались спочатку масиву. якщо ж найменший елемент є першим, обмін не потрібен
                comp += 1 #  к-ть порівнянь
                inter += 1 # к-ть обмінів
        end = time.time()
        t = end - start
        return seq, comp, inter, t


    def descending_order_selection(seq, comp, inter, t):
        ''' Сортування вибором за спаданням '''
        start = time.time()
        for i in range(len(seq)-1): # ітерація по всім елементам масиву
            max_el = i
            # в цьому лічильнику буде зберігатись індекс останнього елемента відсортованої частини масиву,
            # який є найбільшим елементом для кожної ітерації. на початку ітерації це перший елемент
            for j in range(i+1, len(seq)): # ітерація по невідсортованій частині масиву
                if seq[j] > seq[max_el]:
                    # якщо елемент ітерації більший за елемент з індексом min_el, то в цю змінну записується його індекс
                    max_el = j
                    comp += 1  # к-ть порівнянь
            if max_el != i:
                seq[i], seq[max_el] = seq[max_el], seq[i]
                # якщо після пройдення ітерації по масиву знайдениий найбільший елемент не дорівнює першому
                # (відносно певної ітерації, не обов*язково перший у масиві), індекс якого записуєтсья у змінну min_el
                # на початку кожної ітерації, то потрібно здійснити обмін цього елемента з тим, у якого індекс і,
                # щоб найбільші елементи розташовувались спочатку масиву. якщо ж найбільший елемент є першим, обмін не потрібен
                comp += 1  # к-ть порівнянь
                inter += 1  # к-ть обмінів
        end = time.time()
        t = end - start
        return seq, comp, inter, t


    def growing_order_insertion(seq, comp, inter, t):
        ''' Сортування вставками за зростанням '''
        start = time.time()
        for i in range(1, len(seq)):
            # цикл починається з другого елементу, перший будемо вважати вже відсортованим,
            # пізніше кількість таких відсортованих елементів будемо збільшувати утворюючи відсортовану частину масиву
            for j in range(i-1, -1, -1):
                # цикл буде проходити по всім елементам з кінця у зворотньому порядку для того, щоб, при знайденні
                # елементу меншого за даний, ми могли поміняти їх місцями, порівнювати його (елемент менший за даний)
                # з попереднім і пересувати його вліво, доки не знайдемо його логічне місце в масиві
                # (наступний по порядку елемент більший за даний) або доки не поставимо даний елемент на початок масиву
                if seq[j] > seq[j+1]:
                    seq[j], seq[j+1] = seq[j+1], seq[j]
                    # якщо елемент менший за попередній, то потрібно здійснити обмін
                    comp +=1 # к-ть порівнянь
                    inter += 1  # к-ть обмінів
                else:
                    comp += 1
                    break
                    # якщо елемент менший за наступний, значить в цій ітерації він на своєму місці, виходимо з ітерації
        end = time.time()
        t = end - start
        return seq, comp, inter, t


    def descending_order_insertion(seq, comp, inter, t):
        ''' Сортування вставками за спаданням '''
        start = time.time()
        for i in range(1, len(seq)):
            # цикл починається з другого елементу, перший будемо вважати вже відсортованим,
            # пізніше кількість таких відсортованих елементів будемо збільшувати утворюючи відсортовану частину масиву
            for j in range(i - 1, -1, -1):
                # цикл буде проходити по всім елементам з кінця у зворотньому порядку для того, щоб, при знайденні
                # елементу більшого за даний, ми могли поміняти їх місцями, порівнювати його (елемент більший за даний)
                # з попереднім і пересувати його вліво, доки не знайдемо його логічне місце в масиві
                # (наступний по порядку елемент менший за даний) або доки не поставимо даний елемент на початок масиву
                if seq[j] < seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    comp += 1 # к-ть порівнянь
                    inter += 1  # к-ть обмінів
                else:
                    comp += 1
                    break
                    # якщо елемент більший за наступний, значить в цій ітерації він на своєму місці, виходимо з ітерації
        end = time.time()
        t = end - start
        return seq, comp, inter, t


    if answer_order == 1 and answer_sort == 1: # Сортування бульбашкою за зростанням
        seq_grow_bubble, comp_b1, t1 = growing_order_bubble(seq, 0, 0)
        print(f'\nBubble sorting in growing order: {seq_grow_bubble}')
        print(f'Time spent on bubble sorting {len(seq)} integers in growing order: {t1}')
        print(f'Number of comparisons: {comp_b1}, number of interchanges: {comp_b1}')

    elif answer_order == 1 and answer_sort == 2: # Сортування вибором за зростанням
        seq_grow_selection, comp_s1, inter_s1, t3 = growing_order_selection(seq, 0, 0, 0)
        print(f'\nSelection sorting in growing order: {seq_grow_selection}')
        print(f'Time spent on selection sorting {len(seq)} integers in growing order: {t3}')
        print(f'Number of comparisons: {comp_s1}, number of interchanges: {inter_s1}')

    elif answer_order == 1 and answer_sort == 3: # Сортування вставками за зростанням
        seq_grow_insertion, comp_i1, inter_i1, t5 = growing_order_insertion(seq, 0, 0, 0)
        print(f'\nInsertion sorting in growing order: {seq_grow_insertion}')
        print(f'Time spent on insertion sorting {len(seq)} integers in growing order: {t5}')
        print(f'Number of comparisons: {comp_i1}, number of interchanges: {inter_i1}')

    elif answer_order == 2 and answer_sort == 1: #  Сортування бульбашкою за спаданням
        seq_desc_bubble, comp_b2, t2 = descending_order_bubble(seq, 0, 0)
        print(f'Bubble sorting in descending order: {seq_desc_bubble}')
        print(f'Time spent on bubble sorting {len(seq)} integers in descending order: {t2}')
        print(f'Number of comparisons: {comp_b2}, number of interchanges: {comp_b2}')

    elif answer_order == 2 and answer_sort == 2: # Сортування вибором за спаданням
        seq_desc_selection, comp_s2, inter_s2, t4 = descending_order_selection(seq, 0, 0, 0)
        print(f'Selection sorting in descending order: {seq_desc_selection}')
        print(f'Time spent on selection sorting {len(seq)} integers in descending order: {t4}')
        print(f'Number of comparisons: {comp_s2}, number of interchanges: {inter_s2}')

    elif answer_order == 2 and answer_sort == 3: # Сортування вставками за спаданням
        seq_desc_insertion, comp_i2, inter_i2, t6 = descending_order_insertion(seq, 0, 0, 0)
        print(f'Insertion sorting in descending order: {seq_desc_insertion}')
        print(f'Time spent on insertion sorting {len(seq)} integers in descending order: {t6}')
        print(f'Number of comparisons: {comp_i2}, number of interchanges: {inter_i2}')

    answer = input('\nDo you want to continue? Yes-1, No-2:')
    if answer == '1':
        continue
    else:
        break
