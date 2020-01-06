import sys

data = sys.stdin.readlines()

papers = []
for present in data:
    #length l, width w, and height h
    l, w, h = [ int(x) for x in present.split('x') ]

    #find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
    lw = l*w
    wh = w*h
    hl = h*l
    smallest = min(lw, wh, hl)
    
    paper = 2*lw + 2*wh + 2*hl + smallest
    papers.append(paper)
print(sum(papers)) 