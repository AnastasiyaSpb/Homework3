# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_couple_elements(lst: list[int]) -> list[int]:
    list_result = []
    k = range(len(lst)//2+1) if len(lst) % 2 else range(len(lst)//2)
    for i in k:
        list_result.append(lst[i]*lst[-1-i])
    return list_result


a = list(map(int, input("Введите числа через пробел: ").split()))

print(mult_couple_elements(a))