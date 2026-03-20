import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

WALL = "#"
BOX_L = "["
BOX_R = "]"
BOX_L_MOVED = "("
BOX_R_MOVED = ")"
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
                wideRow = ""
                for char in row:
                    if char == WALL:
                        wideRow += WALL*2
                    elif char == EMPTY:
                        wideRow += EMPTY*2
                    elif char == BOX:
                        wideRow += "[]"
                    else:
                        wideRow += ROBOT + EMPTY
 
                if ROBOT in row:
                    robotX = row.find(ROBOT)*2
                    print(f"{robotX} {robotY}")
                if robotX==0: # If robot has not been found
                    robotY +=1
                warehouse.append(wideRow)
        else:
            directions += line.replace("\n","")

def replace(warehouse, x,y, component):
    warehouse[y] = warehouse[y][:x] + component + warehouse[y][x + 1:]
    return warehouse


def movePiece(warehouse, x, y, direction, replacement):
    nextX = x
    nextY = y
    vertical = False
    if direction == UP:
        nextY -= 1
        vertical = True
    elif direction == DOWN:
        nextY += 1
        vertical = True
    elif direction == LEFT:
        nextX -= 1
    elif direction == RIGHT:
        nextX += 1

    print(f"Moving piece {x} {y} {warehouse[y][x]} to {warehouse[nextY][nextX]}")
    if warehouse[y][x] == EMPTY:
        print("Empty space detected OK")
        replace(warehouse, x, y, replacement)
        return True

    if warehouse[nextY][nextX] == WALL:
        print("WALL DETECTED")
        return False # can't move everything
    

    bool1 = bool2 = False
    if(vertical):
        if warehouse[y][x] == BOX_L :
            replace(warehouse,x+1, y, EMPTY)
            bool1 = movePiece(warehouse, nextX, nextY, direction, BOX_L_MOVED)
            bool2 = movePiece(warehouse, nextX+1, nextY, direction, BOX_R_MOVED)
        elif warehouse[y][x] == BOX_R :
            replace(warehouse,x-1, y, EMPTY)
            bool1 = movePiece(warehouse, nextX, nextY, direction, BOX_R_MOVED)
            bool2 = movePiece(warehouse, nextX-1, nextY, direction, BOX_L_MOVED)
        elif warehouse[y][x] == ROBOT :
            bool2 = True
            bool1 = movePiece(warehouse, nextX, nextY, direction, ROBOT)
    else:
        bool2 = True
        bool1 = movePiece(warehouse, nextX, nextY, direction, warehouse[y][x])

        
    if bool1 and bool2:
        replace(warehouse, x, y, replacement)
        return True
    
    return False


def displayWarehouse(warehouse):
    lineX = " "
    for i in range(len(warehouse[0])):
        lineX += str(i%10)
    print(lineX)
    j=0
    for line in warehouse:
        printline = str((j)%10) + line
        j+=1
        print(printline)

def sanitizeWarehouse(ware):

    print("HAAAAAAAA")
    for i in range(len(ware)):
        ware[i] = ware[i].replace("(","[")
        ware[i] = ware[i].replace(")","]")
        print(ware[i])
    
    print("HAAAAAAAA")
    return ware

def move(direction):
    global robotX, robotY, warehouse

    newWarehouse = [] # make a temporary copy to check if possible to move everything
    for line in warehouse:
        newWarehouse.append(line)

    

    print(f"Robot in {robotX} {robotY} moving {direction}")
    if movePiece(newWarehouse, robotX, robotY, direction, EMPTY):
        warehouse = newWarehouse

        replace(warehouse, robotX, robotY, EMPTY)
        if direction == UP:
            robotY -= 1
        elif direction == DOWN:
            robotY += 1
        elif direction == LEFT:
            robotX -= 1
        elif direction == RIGHT:
            robotX += 1

displayWarehouse(warehouse)

for i in directions:
    move(i)

    warehouse = sanitizeWarehouse(warehouse)

    displayWarehouse(warehouse)

def calculateGPSCoordinatesSum():
    sum = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == BOX_L:
                sum += 100*y + x
    return sum


answer = calculateGPSCoordinatesSum()

displayWarehouse(warehouse)

print(f"\nAnswer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

