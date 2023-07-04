'''
TASK 1
1.1
'''

first_name = 'Yulia'
second_name = 'Hlushko'
print(first_name + ' ' + second_name)

# 1.2 

full_name = first_name + ' ' + second_name
print(full_name.lower())
print(full_name.title())

# 1.3

first_name = first_name.replace('Yulia', ' Yulia   ')
full_name = first_name + '\n' + '\t' + second_name
print(full_name)
full_name = first_name.strip() + '\n' + '\t' + second_name
print(full_name)

# Task 2

course = 36.5685
dol = round(1000 / course, 2)
print(f'Поточний курс складає: {dol} $')

