data = input()
santa, robot = [], [] 
for i in range(len(data)): 
    if i % 2: 
        robot.append(data[i]) 
    else : 
        santa.append(data[i]) 

coord_santa, coord_robot = (0,0), (0,0)
houses = set()
houses.add(coord_santa)

for move in santa:
    # Moves are always exactly one house to the north (^), south (v), east (>), or west (<)
    if '^' in move:
        coord_santa = (coord_santa[0],coord_santa[1]+1)
    elif 'v' in move:
        coord_santa = (coord_santa[0],coord_santa[1]-1)
    elif '>' in move:
        coord_santa = (coord_santa[0]+1,coord_santa[1])
    else: #<
        coord_santa = (coord_santa[0]-1,coord_santa[1])
    houses.add(coord_santa)

for move in robot:
    # Moves are always exactly one house to the north (^), south (v), east (>), or west (<)
    if '^' in move:
        coord_robot = (coord_robot[0],coord_robot[1]+1)
    elif 'v' in move:
        coord_robot = (coord_robot[0],coord_robot[1]-1)
    elif '>' in move:
        coord_robot = (coord_robot[0]+1,coord_robot[1])
    else: #<
        coord_robot = (coord_robot[0]-1,coord_robot[1])
    houses.add(coord_robot)

print(len(houses))