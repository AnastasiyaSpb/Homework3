# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def sum_odd_elements(lst: list[int]) -> int:
    sum_result = 0
    for i in range(1, len(lst), 2):
        sum_result += lst[i]
    return sum_result


a = list(map(int, input("Введите числа через пробел: ").split()))

print(sum_odd_elements(a))
