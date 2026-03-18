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

def saveBoard(iteration):
    with open('output.txt', 'a') as f:
        f.write("="*WIDTH + "\n")
        for y in range(HEIGHT):

            for x in range(WIDTH):
                botNumber = 0
                for r in robots:
                    if r.x == x and r.y == y:
                        botNumber+=1
                
                if botNumber != 0:
                    f.write(str(botNumber))
                else:
                    f.write(".")
            f.write("\n")
        f.write("="*WIDTH + "\n")
        f.write("^^^" + str(iteration) + "^^^\n")

def maxDiff(a, b, c, d):
    m = min(a,b,c,d)
    M = max(a,b,c,d)
    return M - m


def calculateQuadrants():
    Q1 = Q2 = Q3 = Q4 = diff = 0
    r : Robot
    middleX = int(WIDTH/2)
    middleY = int(HEIGHT/2)
    meanX = 0
    meanY = 0

    for r in robots:
        meanX+=r.x
        meanY+=r.y
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
    meanX = meanX / len(robots)
    meanY = meanY / len(robots)
    return Q1, Q2, Q3, Q4, meanX, meanY

saveBoard(0)

MAX = 7862

lQ1 = []
lQ2 = []
lQ3 = []
lQ4 = []
test = []
for i in range(MAX):
    print(f"{i}/{MAX}")
    for r in robots:
        r.moveOnce(WIDTH,HEIGHT)
    
    Q1, Q2, Q3, Q4, meanX, meanY = calculateQuadrants()
    lQ1.append(Q1)
    lQ2.append(Q2)
    lQ3.append(Q3)
    lQ4.append(Q4)
    diff = maxDiff(Q1,Q2,Q3,Q4)
    test.append(diff)

    if diff > 50:
        saveBoard(i+1)


    with open('output.txt', 'a') as f:
        f.write(f"Q1={Q1}, Q2={Q2}, Q3={Q3}, Q4={Q4}, meanX={meanX}, meanY={meanY}\n")

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(lQ1, c='b', marker="s", label='first')
ax1.plot(lQ2, c='r', marker="s", label='first')
ax1.plot(lQ3, c='g', marker="s", label='first')
ax1.plot(lQ4, c='black', marker="s", label='first')

ax1.plot(test, c='grey', marker="s", label='first')

plt.legend(loc='upper left')
plt.show()

print(f"HAHA Brute force with human verification = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

