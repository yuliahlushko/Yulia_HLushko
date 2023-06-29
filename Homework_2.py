# Task 1

import random
minute = random.randint (0, 59)
print(f'{minute} minutes')
if minute <= 15:
    print ('First quoter of hour')
elif 16 <= minute <= 30:
    print('Second quoter of hour')
elif 31 <= minute <= 45:
    print('Third quoter of hour')
else:
    print('Forth quoter of hour')

# Task 2

bitrh_month = input('Введіть місяць народження на україській мові з великої літери: ')
if bitrh_month in ['Грудень', 'Січень', 'Лютий']:
    print('Зима. За вікном падав сніг')
elif bitrh_month in ['Березень', 'Квітень', 'Травень']:
    print('Весна. Все довкола розцвітало')
elif bitrh_month in ['Червень', 'Липень', 'Серпень']:
    print('Літо. Діти насолоджувались літніми канікулами')
elif bitrh_month in ['Вереснь', 'Жовтень', 'Листопад']:
    print('Осінь. Все довкола загоралось яскравими фарбами')
else:
    print('Місяць народження введено неправильно!')

# Task 3

x = float(input('Введіть координату x (абсцису) точки М: '))
y = float(input('Введіть координату y (ординату) точки М: '))
if x == 0 or y == 0:
    if x == 0 and y == 0:
        print('Це точка початку координат')
    elif x == 0 and y != 0:
        print('Точка лежить на осі абсцис')
    elif y == 0 and x != 0:
        print('Точка лежить на осі ординат')
elif x > 0 and y > 0:
    print('Точка М знаходиться в першій коордитантій чверті')
elif x < 0 and y > 0:
    print('Точка М знаходиться в другій коордитантій чверті')
elif x < 0 and y < 0:
    print('Точка М знаходиться в третій коордитантій чверті')
elif x > 0 and y < 0:
    print('Точка М знаходиться в четверій коордитантій чверті')
