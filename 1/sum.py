v = int(input('Введите число\n'))

print('Ввели число:',v,'\nВычисляю...\n')
#Разбиваем на разряды
res = []
while v > 0:
    res.append(v % 10)
    v //= 10
res.reverse()
print('Список цифр:',res)

#Считаем сумму цифр
sum = 0
for x in res:
  sum+=x
print('Сумма цифр:',sum)

#Считаем произведение цифр

mult = 1 if sum > 0 else 0

for x in res:
  mult*=x
print('Произведение цифр:',mult)