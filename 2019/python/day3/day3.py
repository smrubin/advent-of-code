import math

file = open('./day3.txt')
wires = list(file)  # read all the lines of a file
file.close()

wire1 = wires[0]
wire2 = wires[1]

# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'


wire1Directions = wire1.split(',')
wire2Directions = wire2.split(',')

wire1coordinates = {0: [0]}

# keep track of coordinates
x = 0
y = 0

# make data struc from wire 1
# data struc to be object with x-pos as key, and y-pos as array of values, easier to search
for direction in wire1Directions:
    directionSymbol = direction[0]

    directionValueString = direction[1:]  # get all chars starting at pos 1
    directionValue = int(directionValueString)

    for i in range(0, directionValue):
        if directionSymbol == 'R':
            x = x + 1
        elif directionSymbol == 'L':
            x = x - 1
        elif directionSymbol == 'U':
            y = y + 1
        elif directionSymbol == 'D':
            y = y - 1
        else:
            print('Error, direction not valid')


        # store the current coordinate position
        # if we've already seen the x, just add to the values. else create the new index
        if x in wire1coordinates:
            wire1coordinates[x].append(y)
        else:
            wire1coordinates[x] = [y]

print(wire1coordinates)

# only make data struc for the first wire, then match second wire against it
# todo - clean up
x = 0
y = 0
matches = [] # array of tuples of matches
for direction in wire2Directions:
    directionSymbol = direction[0]

    directionValueString = direction[1:]  # get all chars starting at pos 1
    directionValue = int(directionValueString)

    for i in range(0, directionValue):
        if directionSymbol == 'R':
            x = x + 1
        elif directionSymbol == 'L':
            x = x - 1
        elif directionSymbol == 'U':
            y = y + 1
        elif directionSymbol == 'D':
            y = y - 1
        else:
            print('Error, direction not valid')


        # store the current coordinate position
        # if we've already seen the x, just add to the values. else create the new index
        if x in wire1coordinates:
            yValues = wire1coordinates[x]
            if y in yValues:
                print('Match found')
                matches.append([x, y])

print(matches)
shortest = 1000000000
for match in matches:
    distance = abs(match[0]) + abs(match[1])
    if (distance < shortest):
        shortest = distance

print(shortest)