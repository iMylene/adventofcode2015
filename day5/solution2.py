import sys

data = sys.stdin.readlines()

countnicestrings = 0
for item in data:
    
    #It contains a pair of any two letters that appears at least twice in the string without overlapping.
    nice1 = False
    
    for i in range(0,len(item)):
        if len(item[i+2:]) > 1:
            pair = item[i] + item[i+1]
            restofstring = item[i+2:]
            
            if pair in restofstring:
                nice1 = True
                break

    #It contains at least one letter which repeats with exactly one letter between them
    nice2 = False

    for i in range(2,len(item)):
        firstletter = item[i]
        secondletter = item[i-2]
        if firstletter == secondletter:
            nice2 = True
            break
    
    if bool(nice1) and bool(nice2):
        countnicestrings += 1

print(countnicestrings)