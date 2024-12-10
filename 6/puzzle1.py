training = False
file = "exemple" if training else "inputs"
answer = 0

map = []
class Position:
    def __init__(self, h=0, w=0):
        self.h = h
        self.w = w

    def move(self, dh, dw):
        self.h += dh
        self.w += dw

    def __repr__(self):
        return f"Position({self.h}, {self.w})"

with open(file, 'r') as file:
    
    for line in file:
        row = []
        for char in line:
            if char != '\n':
                row.append(char)
        map.append(row)
        if training:
            print(row)
    height = len(map)
    width = len(map[0])
print(f"height {height} width {width}")

currentPosition = Position()

for h in range(height):
    if '^' in map[h]: 
        currentPosition.move(h,0)
        for w in range(width):
            if map[h][w] == '^':
                currentPosition.move(0,w)

def move(currentDirection, currentPosition : Position, map):
    map[currentPosition.h][currentPosition.w] = "X"
    outside = False

    if currentDirection == "UP":
        if(currentPosition.h-1) == -1:
            outside = True
        elif map[currentPosition.h-1][currentPosition.w] == "#":
            currentDirection = "RIGHT"
        else:
            currentPosition.move(-1,0)

    if currentDirection == "RIGHT":
        if(currentPosition.w+1) == width:
            outside = True
        elif map[currentPosition.h][currentPosition.w+1] == "#":
            currentDirection = "DOWN"
        else:
            currentPosition.move(0,+1)
    
    elif currentDirection == "DOWN":
        if(currentPosition.h+1) == height:
            outside = True
        elif map[currentPosition.h+1][currentPosition.w] == "#":
            currentDirection = "LEFT"
        else:
            currentPosition.move(+1,0)

    elif currentDirection == "LEFT" :
        if(currentPosition.w-1) == -1:
            outside = True
        if map[currentPosition.h][currentPosition.w-1] == "#":
            currentDirection = "UP"
        else:
            currentPosition.move(0,-1)
    
    return outside,currentDirection




directions = ["UP", "RIGHT", "DOWN", "LEFT"]
currentDirection = "UP"
outside = False

while not outside:
    if training:
        print(currentPosition, currentDirection)

    outside, currentDirection = move(currentDirection,currentPosition,map)



exploredTiles = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'X':
            exploredTiles +=1

with open("output.txt", "w") as file:
    for row in map:
        if(training): print(row)
        for char in row:
            file.write(char)
        file.write('\n')



print(f"exploredTiles = {exploredTiles}")


