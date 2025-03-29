from itertools import product
print(list(product([1,2,3], repeat = 2))) # product([1,2,3], [1,2,3])
print(list(product([1,2,3], ['a','b'])))
print(list(product(['a','b'], [1,2,3])))