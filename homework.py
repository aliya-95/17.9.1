# Вводим последовательность чисел [16 20 42 4 8 15] и проверка соответствия условию
element = input("Введите последовательность чисел через пробел:").split()
array = list(map(int, element))
number = int(input('Введите число   '))
print(type(array))

while number:
    if number < min(array):
        print('Введенное число не прошла проверку соответствия указанному условию ввода данных ')
        number = int(input('Введите число:   '))
    elif number > max(array):
        print('Введенное число не прошла проверку соответствия указанному условию ввода данных ')
        number = int(input('Введите число:   '))
    else:
         break

#Сортировка списка по возрастанию элементов в нем, метод Сортировка пузырьком

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу. Метод алгоритм двоичного поиска

def binary_search(array, number, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == number:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif number < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, number, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, number, middle + 1, right)


print("Индекс введенного числа в списке: ", binary_search(array, number, 0, len(array) - 1))








