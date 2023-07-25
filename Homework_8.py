#1
from folder1 import total, dif
print(total(50, 80))
print(dif(80, 30))

'''
2
Part (%) of one number in another number
'''


def percNum(num1, num2):
    try:
        res = num1/num2*100
        print(res)
    except ZeroDivisionError:
        print("You can not use 0")
    except TypeError:
        print("You can use only int")


percNum(0,100)

#3
from datetime import datetime, timedelta

def findNewDate():
    date = input("Введіть дату в форматі (dd/mm/yyyy)\n")
    days = int(input("Введшіть кількість днів: "))
    action = input("Оберіть дію (+/-): ")
    date1 = datetime.strptime(date, '%d/%m/%Y').date()
    if action == '+':
        print(date1 + timedelta(days=days))
    elif action == '-':
        print(date1 - timedelta(days=days))

findNewDate()

#4
import timespan as timespan


def findAge(birthDate):
    try:
        birthDate = datetime.strptime(birthDate, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Невірний формат! Введіть дату у форматі: DD/MM/YYYY HH:MM")
    birthDate1 = birthDate.timestamp()
    currentDate1 = datetime.now().timestamp()
    age = currentDate1 - birthDate1
    ageInYears = int(age/31622400)
    print(f'Тобі {ageInYears} роки/ів!')
    print(f'Твій точний вік в секундах складає {age}!')


# Example usage:
inputDateBirth = input("Введіть дату та час народження в форматі (DD/MM/YYYY HH:MM): ")
findAge(inputDateBirth)