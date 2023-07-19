#1
import re

def returnDomains(fileName):
    with open(fileName, 'r') as file:
        for i in file:
            pattern = r'\.'
            i = re.sub(pattern, '', i)
            print(i, end='')


returnDomains('domains.txt')


#2

import csv
userData = [
    ('#', 'Surname', 'Country'),
    [1, 'Hlushko', 'UA'],
    [2, 'Smith', 'UK'],
    [3, 'Rodriges', 'SP']
]
def fillFile(fileName2, data):
    with open(fileName2, 'w') as file2:
        for row in data:
            csv_row = ','.join(str(cell) for cell in row)
            file2.write(csv_row + '\n')

data2 = [
    ['#', 'Surnames', 'Country'],
    [1, 'Hlushko', 'UA'],
    [2, 'Smith', 'UK'],
    [3,'Rodriges', 'SP']
]

fillFile('names.txt', data2)


def receiveSurnames(fileName3):
    surnames = []
    with open(fileName3, 'r') as file3:
        csv_reader = csv.reader(file3)
        header = next(csv_reader, None)
        for row in csv_reader:
            surname = row[1].strip()
            surnames.append(surname)
        print(surnames)

receiveSurnames('names.txt')

# 3

import re
def extract_dates_from_text(file_path):
    pattern1 = r'(\d{1,2})(?:st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})'

    with open('authors.txt', 'r') as file:
        text = file.read()

    matches = re.findall(pattern1, text)
    formatted_dates = [f"{day} {month} {year}" for day, month, year in matches]
    for i in formatted_dates:
        key = 'date:'
        datesDict = {key: i}
        print(datesDict)


extract_dates_from_text('authors.txt')