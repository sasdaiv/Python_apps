import random
i = input("камінь, ножиці, папір, що вибираєш?: ")
a = ['камінь', 'ножиці', 'папір']
while type(a)==list:
    d = random.choice(a)
    print(d)
    if i==d:
        print(input('Нічия, граємо ще ?(жми Enter):'))
        i = input("камінь, ножиці, папір, що вибираєш?: ")
    elif (i==a[0] and d ==a[1]) or (i==a[1] and d ==a[2]) or (i==a[2] and d==a[0]):
        print(input('Ти виграв, граємо ще ?(жми Enter):'))
        i = input("камінь, ножиці, папір, що вибираєш?: ")
    else:
        print(input('Ти програв, граємо ще ?(жми Enter):'))
        i = input("камінь, ножиці, папір, що вибираєш?: ")