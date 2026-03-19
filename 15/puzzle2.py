import time
training = True
start_time = time.time()
file = "exemple2" if training else "inputs"
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

    print(f"Checking space {x} {y} {warehouse[y][x]} next {warehouse[nextY][nextX]}")
    if warehouse[y][x] == EMPTY:
        replace(warehouse, x, y, replacement)
        return True

    if warehouse[nextY][nextX] == WALL:
        print("WALL DETECTED")
        return False # can't move everything
    

    bool1 = bool2 = False
    if(vertical):
        if warehouse[y][x] == BOX_L :
            bool1 = movePiece(warehouse, nextX, nextY, direction, BOX_L_MOVED)
            bool2 = movePiece(warehouse, nextX+1, nextY, direction, BOX_R_MOVED)
        elif warehouse[y][x] == BOX_R :
            bool1 = movePiece(warehouse, nextX, nextY, direction, BOX_L_MOVED)
            bool2 = movePiece(warehouse, nextX-1, nextY, direction, BOX_R_MOVED)
    else:
        bool2 = True
        bool1 = movePiece(warehouse, nextX, nextY, direction, warehouse[y][x])

        
    if bool1 and bool2:
        replace(warehouse, x, y, replacement)
        return True
    
    return False

    


def move(direction):
    global robotX, robotY, warehouse

    newWarehouse = [] # make a temporary copy to check if possible to move everything
    for line in warehouse:
        newWarehouse.append(line)

    

    print(f"Robot in {robotX} {robotY} moving {direction}")
    if movePiece(newWarehouse, robotX, robotY, direction, EMPTY):
        warehouse = newWarehouse
        // Faire un if/else pour mettre à jour la position du robot + supprimer son ancienne position 

for line in warehouse:
    print(line)

for i in directions:
    move(i)

    for line in warehouse:
        print(line)

print(f"\nAnswer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

