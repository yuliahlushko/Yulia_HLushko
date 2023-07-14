# 1
import re
text = input('Input any string: ')
x = re.findall(r'[a-zA-z0-9_]', text)
if x == list(text):
  print("String consist of upper/lower case letters or/and numbers or/and '_'")
else:
  print("String may has spesial symbols or spaces")

# 2
import re

web = ['example.com', 'github.com', 'stackoverflow.com']


def findSiteName(listOfLinks):
    pattern3 = r'.com'
    newList = []
    for i in listOfLinks:
        if re.findall(pattern3, i):
            i = re.sub(pattern3, '', i)
            newList.append(i)
        print(i)


findSiteName(web)

# 3
someText = 'AnyTextWithoutSpaces'
someText2 = '24Novemder 1990'
sentence = 'I like to watch movies.My favorite is Avatar'


def addSpaces(row):
    pattern4 = r'(?=[A-Z])'
    newRow = re.sub(pattern4,' ', row)
    print(newRow)


addSpaces(someText)
addSpaces(someText2)
addSpaces(sentence)