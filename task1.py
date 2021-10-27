"""
    Задача 1. 
    Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. 
    Оценить эффективность своего решения. 
"""

array1 = ['samat', 'sam', 'kurmanov', 'skurmanov']

array2 = ['bob', 'garry', 'kate', 'wolf']

input_array = ['head', 'first', 'samat', 'bob', 'welcome', 'jade', 'simple', 'wolf', 'sam', 'skurmanov']

def filter_array(in_num):
    if in_num in array1 and in_num not in array2:
        return True
    else:
        return False

out_filter = filter(filter_array, input_array)

print('Тип объекта out_filter: ', type(out_filter))
print('Отфильтрованный список: ', list(out_filter))
