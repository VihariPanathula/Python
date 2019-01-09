from itertools import permutations
n = input("Enter a string: ")
b = list(n)
a = permutations(b,3)
for i in a:
    print(i)
