'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

_len = int(input('Введите количество элементов массива\n'))

_array1 = list(random.randrange(1,_len+1,1) for i in range(_len))

print(_array1)  

_min, _max = min(set(_array1)),max(set(_array1))

print('Мин/Макс значения',_min, _max)

_min_i, _max_i = -1,-1

for i in range(0,len(_array1)):
  if _min_i  == -1 and _array1[i] == _min:
    _min_i = i
  if _max_i  == -1 and _array1[i] == _max:
    _max_i = i
  if _min_i >= 0 and _max_i >= 0:
    print('Индексы',_min_i,_max_i)
    _array1[_min_i],_array1[_max_i] = _array1[_max_i],_array1[_min_i]
    print(_array1)
    print('Итераций',i)    
    break