'''Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.'''

	
import random

def gen_int():
  low,high = map(int,input('Введите нижнюю и верхнюю границу диапазона\n').split())
  if low>high:
    print('Нижняя граница диапазона больше верхней границы. Подразумеваю ошибку. Меняю границы местами')
    tmp=high
    high=low
    low=tmp
  
  print(random.randrange(low, high,1))
  

def gen_float():
  low,high = map(float,input('Введите нижнюю и верхнюю границу диапазона\n').split())
  if low>high:
    print('Нижняя граница диапазона больше верхней границы. Подразумеваю ошибку. Меняю границы местами')
    tmp=high
    high=low
    low=tmp
  
  print(low + (high-low)*random.random())

def gen_char():
  low,high = map(str,input('Введите нижнюю и верхнюю границу диапазона\n').split())
  if ord(low)>ord(high):
    print('Нижняя граница диапазона больше верхней границы. Подразумеваю ошибку. Меняю границы местами')
    tmp=high
    high=low
    low=tmp
  print (low,ord(low))
  print (high,ord(high))
  new=random.randrange(ord(low), ord(high),1)
  print(new)
  print(chr(new))

mode=int(input('Что нужно сгенерировать?\n1-целое число\n2-вещественное число\n3-символ\n'))

if mode==1:
  print('Будем генерировать целое число')
  gen_int()
elif mode==2:
  print('Будем генерировать вещественное число')
  gen_float()
elif mode==3:
  print('Будем генерировать символ')  
  gen_char()
else:
  print('Вы ошиблись режимом...')  