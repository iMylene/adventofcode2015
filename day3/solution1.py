data = input()

coord = (0,0)
houses = set()
houses.add(coord)

for move in data:
    # Moves are always exactly one house to the north (^), south (v), east (>), or west (<)
    if '^' in move:
        coord = (coord[0],coord[1]+1)
    elif 'v' in move:
        coord = (coord[0],coord[1]-1)
    elif '>' in move:
        coord = (coord[0]+1,coord[1])
    else: #<
        coord = (coord[0]-1,coord[1])
    houses.add(coord)

print(len(houses))