import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

with open(file, 'r') as file:
    for line in file:
        pass

END = "E"
START = "S"
WALL = "#"
EMPTY = "."

print(f"\nAnswer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))
import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

maze = []
startX = startY = 0
endX = endY = 0

x = y = 0
with open(file, 'r') as file:
    if END in line :
        x = 0
        for c in line:
            if c == END:
                endX = x
                endY = y
            x += 1
    
    if START in line :
        x = 0
        for c in line:
            if c == START:
                startX = x
                startY = y
            x += 1
    for line in file:
        maze.append(line.replace("\n",""))
    y += 1

print(f"Start ({startX},{startY}) END ({endX},{endY})")
for line in maze:
    print(line)


# exploration en largeur d'abord privilégiant les lignes droites


print(f"\nAnswer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))


