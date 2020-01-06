import sys

#data = sys.stdin.readlines()
data = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']


#It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

countnicestrings = 0
for item in data:
    pairs = []
    for i,j in zip(item,item[1:]):
        pairs.append(i + j)
    
    
    for i in range(0, len(item), 2):
        chars = item[i:i+2]
        #if chars in pairs:



    #It contains at least one letter which repeats with exactly one letter between them
    nice = [ i+j for i,j in zip(item,item[2:]) if (i==j) ]
    naughty = [string for string in naughtystrings if (string in item) ]

    if not bool(naughty) and bool(nice):
        countnicestrings += 1

print(countnicestrings)