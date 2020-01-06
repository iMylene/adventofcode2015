data = input()

for i in range(1,len(data)+1):
    instructions = data[:i]
    
    countup = instructions.count('(')
    countdown = instructions.count(')')
    
    dif = countup - countdown
    if dif == -1:
        print(i)
        break
