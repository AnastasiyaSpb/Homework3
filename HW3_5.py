# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_num(num: int) -> list[int]:
    list_res = [0, 1]
    for i in range(2, num+1):
        list_res.append(list_res[i-1] + list_res[i - 2])
    list_res2 = [-1, 1]
    x = -1
    for i in range(num-2):
        k = list_res2[x+2] - list_res2[x+1]
        list_res2.insert(0, k)
    return list_res2 + list_res


# def fibonacci_num(num: int) -> int:
#     if num >= 0:
#         if num == 1 or num == 0:
#             return num
#         return fibonacci_num(num - 1) + fibonacci_num(num - 2)
#     else:
#         return int((-1)**(num+1)) * fibonacci_num(-num)

# a = int(input("Введите число: "))
# print([fibonacci_num(a) for a in range(-a,a+1)])

a = int(input("Введите число: "))
print(fibonacci_num(a))
