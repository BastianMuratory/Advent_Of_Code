import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

WALL = "#"
EMPTY = "."
BOX = "O"
ROBOT = "@"

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


"""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########
"""

warehouse = []
robotX = robotY = 0
directions = ""
warehouseRetreiving = True
with open(file, 'r') as file:
    for line in file:
        if warehouseRetreiving:
            if line == '\n':
                warehouseRetreiving = False
            else:
                row = line.replace("\n","")
                if ROBOT in row:
                    robotX = row.find(ROBOT)
                    print(f"{robotX} {robotY}")
                if robotX==0: # If robot has not been found
                    robotY +=1
                warehouse.append(row)
        else:
            directions += line.replace("\n","")

def isMovementPossible(direction, posX, posY):
    print(f"checking movement {posX} {posY}")
    print(f"going to  {warehouse[posY][posX]}")

    if (warehouse[posY][posX] == EMPTY):
        return True, posX, posY
    elif(warehouse[posY][posX] == WALL):
        return False, posX, posY
    else:
        if direction == UP:
            return isMovementPossible(direction, posX, posY-1)
        elif direction == DOWN:
            return isMovementPossible(direction, posX, posY+1)
        elif direction == LEFT:
            return isMovementPossible(direction, posX-1, posY)
        elif direction == RIGHT:
            return isMovementPossible(direction, posX+1, posY)
        


def move(direction):
    global robotX, robotY
    print(f"Robot in {robotX} {robotY} moving {direction}")
    success, emptyX, emptyY = isMovementPossible(direction,robotX,robotY)
    if success :
        print(f"Pushing to {emptyX} {emptyY}")
        warehouse[emptyY] = warehouse[emptyY][:emptyX] + BOX + warehouse[emptyY][emptyX + 1:]
        warehouse[robotY] = warehouse[robotY][:robotX] + EMPTY + warehouse[robotY][robotX + 1:]
        print("new lines :")
        print(warehouse[emptyY])
        print(warehouse[robotY])

        if direction == UP:
            robotY -= 1
        elif direction == DOWN:
            robotY += 1
        elif direction == LEFT:
            robotX -= 1
        elif direction == RIGHT:
            robotX += 1
        
        warehouse[robotY] = warehouse[robotY][:robotX] + ROBOT + warehouse[robotY][robotX + 1:]
        


for line in warehouse:
    print(line)

for i in range(len(directions)):
    move(directions[i])

    for line in warehouse:
        print(line)


def calculateGPSCoordinatesSum():
    sum = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == BOX:
                sum += 100*y + x
    return sum

answer = calculateGPSCoordinatesSum()
print(f"\nAnswer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

