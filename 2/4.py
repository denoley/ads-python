'''4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.'''

def progr(val_,n_):
  if n_>0:
    return val_+progr(val_/-2,n_-1)  
  else:
    return val_   
    
print('Сумма элементов:',progr(1,int(input('Введите количество элементов\n'))-1))