# 1
import random


def compare_asc(param_1, param_2):
    common = sorted(param_1.intersection(param_2))
    print(common)


list_1 = {0.001, 1, 4, 7, 112, 5, 1, 666, 89}
list_2 = {5, 4, 1, 34, 890, 23, 666, 45, 0.001}

compare_asc(list_1, list_2)

# 2
students_range = {'Yulia': 5, 'Roman': 2, 'Mark': 4, 'Alona': 1}
students_range_2 = {'Claire': 3.8, 'Jim': 5, 'Robert': 5, 'Gloria': 1}


def best_students(**rating):
    total = sum(rating.values())
    avg_sum = total / len(rating)
    print(f'Середній бал в групі {avg_sum}')
    print('Студенти з балом вище середнього:')
    for key, value in rating.items():
        if value >= avg_sum:
            print(f'{key} - {value}')


best_students(**students_range)
best_students(**students_range_2)


# 3
def create_random_dict(param_1, param_2, param_3):
    from random import shuffle
    random.shuffle(param_1)
    random.shuffle(param_2)
    random.shuffle(param_3)
    zipped = zip(param_1, param_2, param_3)
    keys = ['name', 'surname', 'location']
    for values in zipped:
        new_dict = dict(zip(keys, values))
        print(new_dict)


name = ['Yulia', 'Maks', 'Slava']
surname = ['Hlushko', 'Avtunich', 'Kravchenko']
location = ['Kyiv', 'New York', 'Paris', 'Toronto', 'Milan']
name_2 = ['Sam', 'Robert', 'Nicole', 'Nick']
surname_2 = ['Rudenko', 'Smith', 'Homenko', ' Smith']
location_2 = ['Rome', 'Chernihiv', 'London', 'Kherson']
create_random_dict(name, surname, location)
create_random_dict(name_2, surname_2, location_2)