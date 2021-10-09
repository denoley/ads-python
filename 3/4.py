'''4. Определить, какое число в массиве встречается чаще всего.'''

import random

_len = int(input('Введите количество элементов массива\n'))

_array1 = list(random.randrange(1,_len+1,1) for i in range(_len))

print(_array1)  

_max_count,_max_values = -1,[]

for i in set(_array1):
  _count = _array1.count(i) 
  if _max_count <= _count:
    if _max_count < _count:
      _max_count,_max_values = _count,[i]
    else:
      _max_values.append(i)

  
print('Число(а)',_max_values,'встречается чаще всего:',_max_count)
  