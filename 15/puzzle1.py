import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

WALL = "#"
AIR = "."
BOX = "O"
ROBOT = "@"

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
x = y = 0
with open(file, 'r') as file:
    for line in file:
        line.replace("\n","")
        
        if ROBOT in line:
            x = line.find(ROBOT)

        
        warehouse.append(line)
        y +=1

for line in warehouse:
    print(line,end="")



print(f"\nAnswer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

