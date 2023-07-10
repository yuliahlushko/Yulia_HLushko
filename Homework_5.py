#1
import collections
from functools import reduce

list_1 = [1, 3, 4, 6, 10, 11, 15, 12, 14]
list_2 = [1, 9, 4, 12, 10, 22, 15,24, 14]
print(list(filter(lambda x: x in list_1, list_2)))


#2
print((lambda a: 'This is a number' if isinstance(a, int) else 'This is not a number')(67))

#3
nums = [1, 2, 3, 4, 5]
words = ['first', 'second', 'third', 'fifth', 'sixth', 'sevens']
booll = [True, False]

max_length = lambda x, y, z: max([(x, len(x)), (y, len(y)), (z, len(z))], key=lambda item: item[1])[0]
min_length = lambda x, y, z: min([(x, len(x)), (y, len(y)), (z, len(z))], key=lambda item: item[1])[0]
result_max = max_length(nums, words, booll)
result_min = min_length(nums, words, booll)
print(result_max)
print(result_min)