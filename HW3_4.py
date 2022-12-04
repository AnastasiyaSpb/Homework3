# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binar_num(num: int) -> int:
    res = ""
    while num >= 2:
        res = str(num % 2) + res
        num //= 2
    res = str(num) + res
    return int(res)


a = int(input("Введите число: "))
print(binar_num(a))
