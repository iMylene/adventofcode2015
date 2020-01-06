import hashlib

data = input()
lengthanswer = len(data)
zeroes = '000000'

stringnumber = ''
for i in range(lengthanswer):
    stringnumber = stringnumber + '9'
number = int(stringnumber)

for i in range(int(stringnumber)):
    key = data + str(i)
    hash = hashlib.md5(key.encode("utf-8")).hexdigest()
    if zeroes in hash[0:len(zeroes)]:
        print(i)
        break