import sys
data = sys.stdin.readlines()

ribbons = []
for present in data:
    #length l, width w, and height h
    l, w, h = [ int(x) for x in present.split('x') ]

    #find the smallest perimeter and bow
    biggest = max(l,w,h)
    bow = l*w*h

    ribbon = (2*l + 2*w + 2*h - 2*biggest) + bow
    ribbons.append(ribbon)
print(sum(ribbons)) 