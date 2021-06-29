from itertools import permutations, combinations, product, combinations_with_replacement

data = [1, 2, 3,4]
data_a = ['a','b','c','d']

perm = list(permutations(data, 3))
print('순열')
print(perm)
print('')
comb = list(combinations(data, 3))
print('조합')
print(comb)
print('')
prod = list(product(data, repeat = 2))
print('중복있는 각각의 조합')
print(prod)
print('')
prod = list(product(data, data_a))
print(prod)
print('')
comb_w = list(combinations_with_replacement(data, 2))
print('중복없는 각각의 조합')
print(comb_w)
print('')