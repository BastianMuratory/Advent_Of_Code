import os
import shutil
import time
start_time = time.time()

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

startingPosition = Position()

for h in range(height):
    if '^' in map[h]: 
        startingPosition.move(h,0)
        for w in range(width):
            if map[h][w] == '^':
                startingPosition.move(0,w)

def move(currentDirection, currentPosition : Position, map):
    map[currentPosition.h][currentPosition.w] = "X"
    outside = False
    loop = False

    if currentDirection == "UP":
        if(currentPosition.h-1) == -1:
            outside = True
        elif map[currentPosition.h-1][currentPosition.w] in walls:
            # increment number of colisions
            if map[currentPosition.h-1][currentPosition.w] == "#":
                map[currentPosition.h-1][currentPosition.w] = 1
            elif map[currentPosition.h-1][currentPosition.w] == "O":
                pass
            else:
                map[currentPosition.h-1][currentPosition.w] += 1
                # If more than 4 collisions, loop has been found
                if map[currentPosition.h-1][currentPosition.w] > 4 :
                    loop = True 
            
            # change direction
            currentDirection = "RIGHT"
        else:
            currentPosition.move(-1,0)

    if currentDirection == "RIGHT":
        if(currentPosition.w+1) == width:
            outside = True
        elif map[currentPosition.h][currentPosition.w+1] in walls:
            # increment number of colisions
            if map[currentPosition.h][currentPosition.w+1] == "#":
                map[currentPosition.h][currentPosition.w+1] = 1
            elif map[currentPosition.h][currentPosition.w+1] == "O":
                pass
            else:
                map[currentPosition.h][currentPosition.w+1] += 1
                # If more than 4 collisions, loop has been found
                if map[currentPosition.h][currentPosition.w+1] > 4 :
                    loop = True 
            
            # change direction
            currentDirection = "DOWN"
        else:
            currentPosition.move(0,+1)
    
    elif currentDirection == "DOWN":
        if(currentPosition.h+1) == height:
            outside = True
        elif map[currentPosition.h+1][currentPosition.w] in walls:
            # increment number of colisions
            if map[currentPosition.h+1][currentPosition.w] == "#":
                map[currentPosition.h+1][currentPosition.w] = 1
            elif map[currentPosition.h+1][currentPosition.w] == "O":
                pass
            else:
                map[currentPosition.h+1][currentPosition.w] += 1
                # If more than 4 collisions, loop has been found
                if map[currentPosition.h+1][currentPosition.w] > 4 :
                    loop = True 
            
            # change direction
            currentDirection = "LEFT"
        else:
            currentPosition.move(+1,0)

    elif currentDirection == "LEFT" :
        if(currentPosition.w-1) == -1:
            outside = True
        if map[currentPosition.h][currentPosition.w-1] in walls:
            # increment number of colisions
            if map[currentPosition.h][currentPosition.w-1] == "#":
                map[currentPosition.h][currentPosition.w-1] = 1
            elif map[currentPosition.h][currentPosition.w-1] == "O":
                pass
            else:
                map[currentPosition.h][currentPosition.w-1] += 1
                # If more than 4 collisions, loop has been found
                if map[currentPosition.h][currentPosition.w-1] > 4 :
                    loop = True 
            
            # change direction
            currentDirection = "UP"
        else:
            currentPosition.move(0,-1)
    
    return outside,currentDirection,loop

walls = ["#", "O", 0, 1, 2, 3 ,4, 5] # 5 would mean a loop

def copyMap():
    myCopy = []

    for line in map:
        copiedLine = []

        for char in line :
            copiedLine.append(char)
        
        myCopy.append(copiedLine)
    
    return myCopy

def reset_directory(dir_path):
    """
    Removes the specified directory and all its contents, then recreates it.
    :param dir_path: The path to the directory to reset.
    """
    # Check if the directory exists
    if os.path.exists(dir_path):
        # Remove the directory and its contents
        shutil.rmtree(dir_path)
        print(f"Removed directory: {dir_path}")
    
    # Recreate the directory
    os.makedirs(dir_path)
    print(f"Recreated directory: {dir_path}")


NumberOfLoopsFound = 0

reset_directory("./outputs")

# Brute Force :)
for h in range(height):
    print(f"{h}/{height}")
    for w in range(width):
        
        # First check if applicable to this place
        if map[h][w] != '#' and map[h][w] != '^' :

            # Reset the map explored and add the object
            currentMap = copyMap()
            currentMap[h][w] = "O"
            currentPosition = Position(startingPosition.h,startingPosition.w)
            currentDirection = "UP"
            outside = False
            looping = False

            while not outside:
                if training:
                    #print(currentPosition, currentDirection)
                    pass

                outside, currentDirection, looping = move(currentDirection, currentPosition, currentMap)

                if looping :
                    outside = True
                    NumberOfLoopsFound += 1
                    #print("LOOOPING")

                    with open(f"outputs/output{h}.{w}.txt", "w") as file:
                        for row in currentMap:
                            if(training): 
                                print(row)

                            for c in row:
                                try:
                                    file.write(str(c))
                                except:
                                    file.write(c)
                            file.write('\n')

print("--- %s seconds ---" % (time.time() - start_time))
print(f"NumberOfLoopsFound = {NumberOfLoopsFound}")


