'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'''

result = []

for i in range(2,10):
  result.append([i,len(list(range(i,100,i)))])

print(result)  