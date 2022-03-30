cnt=0
slovo= input('Введіть слово в якому буде виконуватися пошук символу: ').lower()
symbol = (input('Введіть символ для пошуку: ')).lower()
for i in slovo:
    if i != symbol:
        continue
    else:
        cnt+=1
print(cnt)
print(input('Продовжимо?:'))
slovo= input('Введіть слово в якому буде виконуватися пошук символу: ').lower()

# slovo = input('Введіть слово в якому буде виконуватися пошук символу: ').lower()
# symbol = (input('Введіть символ для пошуку: ')).lower()
# list = []
# for i in slovo:
#     if i !=symbol:
#         continue
#     else:
#         list.append(symbol)
# print(len(list))