"""
    Задача 2. Дан массив целых чисел. 
    Нужно удалить из него нули. 
    Можно использовать только О(1) дополнительной памяти.
"""

array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
print(set(array))

def filter_zero_num(in_num):
    if in_num == 0:
        return False
    else:
        return True

out_filter = filter(filter_zero_num, array)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))
