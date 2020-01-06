import sys

data = sys.stdin.readlines()
naughtystrings = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'

countnicestrings = 0
for item in data:
    countvowels = 0
    for i in item:
        if i in vowels:
            countvowels += 1

    nice = [ i+j for i,j in zip(item,item[1:]) if (i==j) ]
    naughty = [string for string in naughtystrings if (string in item) ]

    if not bool(naughty) and countvowels >= 3 and bool(nice):
        countnicestrings += 1

print(countnicestrings)