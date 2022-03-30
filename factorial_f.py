self = int(input('Введіть число, яке хочете піднести до факторіала: '))
f = 1
if self == 0:
     print('Число не можу бути 0!')
else:
    for i in range(2,self+1):
         f*=i
    print(f)