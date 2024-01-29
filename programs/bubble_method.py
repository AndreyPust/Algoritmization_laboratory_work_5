#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import random


def bubble_sort(list_to_sort):
    """
    Функция сортировки массива методом пузырька.
    """
    n = len(list_to_sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return None


if __name__ == '__main__':
    # Необходимо создать программу, которая создает данные для анализа скорости работы
    # алгоритма сортировки списка методом пузырька.

    current_list = [random.randint(-100, 100) for i in range(1000)]

    # Для записи результатов используется файл с данными в той же директории, что и данный модуль.
    filename_results = 'results.txt'

    # Получим данные времени работы алгоритма.
    for number in range(0, 70):

        with open(filename_results, 'a') as file:
            time_search = timeit.timeit(lambda: bubble_sort(current_list), number=10)
            file.write(str(time_search) + '\n')
        file.close()

        # Увеличим размер данного списка.
        for i in range(0, 100):
            current_list.append(random.randint(-100, 100))
