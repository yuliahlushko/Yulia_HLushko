'''
TASK 1
1.1 Напишіть програму, в яку спочатку запишіть в 1 змінну ваше ім'я,
в 2 ваше прізвище, а потім виводить на екран повідомлення з вашими особистими даними.
Тут використайте конкатенацію, тобто об'єднайте стрічки.
'''

first_name = 'Yulia'
second_name = 'Hlushko'
print(first_name + ' ' + second_name)

'''
1.2 Виведіть результат в нижньому, верхнього регістрах з капіталізацією перших букв кожного слова.
'''

full_name = first_name + ' ' + second_name
print(full_name.lower())
print(full_name.title())

'''
1.3 Змініть значення своєї змінної, яку ви створили на кроці 1 , додавши до свого імені декілька пробілів
 на початку та вкінці. Прослідкуйте щоб \t \n зустрічались хоча б один раз. Виведіть нове значення. 
 Видаліть пропуски і збережіть новий результат.
'''

first_name = '  Yulia  '
second_name = '   Hlushko   '
