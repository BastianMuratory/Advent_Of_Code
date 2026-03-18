import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

WIDTH = 101
HEIGHT = 103

class Robot:
    def __init__(self, px, py, vx, vy):
        self.x = px
        self.y = py
        self.vx = vx
        self.vy = vy
    

    def moveOnce(self, boundaryX, boundaryY):
        self.x = (self.x + self.vx) % boundaryX
        self.y = (self.y + self.vy) % boundaryY
    
    def move(self, seconds, boundaryX, boundaryY):
        self.x = (self.x + seconds * self.vx) % boundaryX
        self.y = (self.y + seconds * self.vy) % boundaryY


robots = []


with open(file, 'r') as file:
    for line in file:
        parts = line.replace("\n","").replace("p","").replace("v","").replace("=","").split(" ")
        position = parts[0].split(",")
        velocity = parts[1].split(",")
        robots.append(Robot(int(position[0]), int(position[1]), int(velocity[0]), int(velocity[1])))

def displayBoard():
    print("="*WIDTH)

    for y in range(HEIGHT):

        for x in range(WIDTH):
            botNumber = 0
            for r in robots:
                if r.x == x and r.y == y:
                    botNumber+=1
            
            if botNumber != 0:
                print(botNumber, end='')
            else:
                print(".", end='')
        print("\n")
    print("="*WIDTH)

def calculateQuadrants():
    Q1 = Q2 = Q3 = Q4 = 0
    r : Robot
    middleX = int(WIDTH/2)
    middleY = int(HEIGHT/2)

    for r in robots:
        if r.x != middleX and r.y != middleY:
            if r.x < middleX:
                if r.y < middleY:
                    Q1 += 1
                else:
                    Q3 += 1
            else:
                if r.y < middleY:
                    Q2 += 1
                else:
                    Q4 += 1
    print(f"Q1={Q1} Q2={Q2} Q3={Q3} Q4={Q4}")
    return Q1 * Q2 * Q3 * Q4

displayBoard()
for r in robots:
    r.move(100, WIDTH,HEIGHT)

displayBoard()

answer = calculateQuadrants()

print(f"Answer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

