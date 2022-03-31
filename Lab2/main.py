import random
import time

A = []
for i in range(20):
    A.append(random.randint(-20,20))
A.sort()
print(A)

# функция для вставки элемента в массив
def insert_elem(massive, ins_value):
    massive.append(ins_value)
    massive.sort()
    return massive

# функция для удаления элемента из массива
def delete_elem(massive, del_value):
    massive.remove(del_value)
    massive.sort()
    return massive
#-----------------------------------------------------------------------------
print("Введите значение, которое нужно найти, для функции линейного поиска")
elem = int(input())
# линейный поиск
lin_start_time = time.time()
def linear_search(massive, element):
    for i in range(len(massive)):
        if massive[i] == element:
            return i
    return 'В сгенерированном массиве нет элемента с таким значением'
print(linear_search(A,elem))
print(f"{(time.time() - lin_start_time)*1000} миллисекунд")
print("Введите значение которое хотите вставить: ")
ins1_value = int(input())
print(insert_elem(A, ins1_value))

print("Введите значение которое хотите удалить: ")
del1_value = int(input())
print(delete_elem(A, del1_value))
#-----------------------------------------------------------------------------
print("Введите значение, которое нужно найти, для функции бинарного поиска")
value = int(input())
#бинарный поиск
bin_start_time = time.time()
def binary_search_iterativ(massiv, desired_value):
    # находим среднее значение массива, обозначим верхнюю и нижнюю границу
    mid = len(massiv) // 2
    bottom_line = 0
    upper_line = len(massiv) - 1
    # сравниваем искомое значение с серединой
    while massiv[mid] != desired_value and bottom_line <= upper_line:
        if desired_value > massiv[mid]:
            bottom_line = mid + 1
        else:
            upper_line = mid - 1
        # вычесляем индекс новой середины после сдвига одной из границ
        mid = (bottom_line + upper_line) // 2
    # проверка условия, если границы пересеклись
    if bottom_line > upper_line:
        return 'В сгенерированном массиве нет элемента с таким значением'
    else:
        return mid
print(binary_search_iterativ(A, value))
print(f"{(time.time() - bin_start_time)*1000} миллисекунд")
print("Введите значение которое хотите вставить: ")
ins2_value = int(input())
print(insert_elem(A, ins2_value))

print("Введите значение которое хотите удалить: ")
del2_value = int(input())
print(delete_elem(A, del2_value))
#-----------------------------------------------------------------------------

print("Ниже введите значение,для получения результата с помощью фибоначчиева поиска")
fib_value = int(input())
# фибоначчиев поиск
fib_start_time = time.time()
def fibonacci_search(massiv, desired_value):
    # первые два числа и третье выраженное суммой прошлых
    fib_num_first = 0
    fib_num_second = 1
    fib_num_sumFS = fib_num_first + fib_num_second
    # наименьшее число в последовательности
    while fib_num_sumFS < len(massiv):
        fib_num_first = fib_num_second
        fib_num_second = fib_num_sumFS
        fib_num_sumFS = fib_num_first + fib_num_second
    index = -1
    # пока в массиве есть элементы и значением суммы>1 делаем следующее
    while (fib_num_sumFS > 1):
        # i ищем для того, чтобы понять на сколько вниз нам сдвигаться
        i = min(index+fib_num_first, len(massiv)-1)
        if massiv[i] < desired_value:
            # перемещаем  наши значения на два шага вниз и индекс становится индексом элемента
            fib_num_sumFS = fib_num_second
            fib_num_second = fib_num_first
            fib_num_first = fib_num_sumFS - fib_num_second
            index = i
        elif massiv[i] > desired_value:
            # перемещаем наши значения на один шаг вниз
            fib_num_sumFS = fib_num_first
            fib_num_second = fib_num_second - fib_num_first
            fib_num_first = fib_num_sumFS - fib_num_second
        else:
            return i
    # проверяем значение
    if fib_num_second and index < len(massiv)-1 and massiv[index+1] == desired_value:
        return index+1
    return 'В сгенерированном массиве нет элемента с таким значением'
print(fibonacci_search(A,fib_value))
print(f"{(time.time() - fib_start_time)*1000} миллисекунд")
print("Введите значение которое хотите вставить: ")
ins3_value = int(input())
print(insert_elem(A, ins3_value))

print("Введите значение которое хотите удалить: ")
del3_value = int(input())
print(delete_elem(A, del3_value))
#-----------------------------------------------------------------------------
print("Ниже введите значение,для получения результата с помощью интерполяционного поиска")
inter_value = int(input())
int_start_time = time.time()
def interpolation_searsh(massiv, desired_value):
    start_index = 0
    last_index = len(massiv)-1
    while start_index <= last_index and desired_value >= massiv[start_index] and desired_value <= massiv[last_index]:
        # вычисление вероятной позиции искомого элемента
        index = start_index + int(((float(last_index-start_index) / (massiv[last_index]-massiv[start_index]))*(desired_value-massiv[start_index])))
        # элемент найден
        if massiv[index] == desired_value:
            return index
        # пересчитываем индекс для праваого подмассива
        elif massiv[index] < desired_value:
            start_index = index + 1
        # пересчитываем индекс для левого подмассива
        else:
            last_index = index - 1
    return 'В сгенерированном массиве нет элемента с таким значением'
print(interpolation_searsh(A,inter_value))
print(f"{(time.time() - int_start_time)*1000} миллисекунд")
print("Введите значение которое хотите вставить: ")
ins4_value = int(input())
print(insert_elem(A, ins4_value))

print("Введите значение которое хотите удалить: ")
del4_value = int(input())
print(delete_elem(A, del4_value))
