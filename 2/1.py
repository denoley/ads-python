'''1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.'''

def mult_():
  print('Введите 2 числа')
  v1,v2=int(input()),int(input())
  print(v1,'*',v2,'=',v1*v2,'\n')

def div_():
  print('Введите 2 числа')
  v1,v2=int(input()),int(input())
  if v2==0:
    print('Не нужно делить на 0\n')  
  else:
    print(v1,':',v2,'=',v1/v2,'\n')

def sum_():
  print('Введите 2 числа')
  v1,v2=int(input()),int(input())
  print(v1,'+',v2,'=',v1+v2,'\n')

def sub_():
  print('Введите 2 числа')
  v1,v2=int(input()),int(input())
  print(v1,'-',v2,'=',v1-v2,'\n')

while True:
  oper = input('Введите операцию +-*/ или q для выхода:\n')
  if oper not in('0', '+', '-', '*', '/','q','Q'):
    print('Вы ввели что-то не то... Введите корректную операцию или q для выхода:\n')
  elif oper in('q','Q'):
    break
  elif oper == '*':
    mult_()
  elif oper == '/':
    div_()
  elif oper == '+':
    sum_()
  else :
  # oper == '-':
    sub_()