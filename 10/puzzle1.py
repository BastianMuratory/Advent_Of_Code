import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

class Cell:
    def __init__(self, h=0, w=0, id=-1):
        self.h = h
        self.w = w
        self.id = id

    def move(self, dh, dw):
        self.h += dh
        self.w += dw
    
    def equal(self, otherP):
        return self.h == otherP.h and self.w == otherP.w and self.id == otherP.id
    
    def __repr__(self):
        return f"Cell {self.id} at ({self.h+1}, {self.w+1})"



gridd = []

with open(file, 'r') as file:
    h = 0
    for line in file:
        w = 0
        gridd.append([])
        for char in line:
            if not char == "\n":
                cell = Cell(h,w,int(char))
                w+=1
                gridd[h].append(cell)
        h+=1

width = w
height = h

for line in gridd :
    string = ""
    for cell in line:
        string += str(cell.id)
    print(string)


def explore(gridd,h,w) :
    #print("Checking ",gridd[h][w])
    value = gridd[h][w].id
    returnedList = []
    # if top just return the cell
    if value == 9:
        cell = gridd[h][w]
        #print("End :",cell)
        return [cell]
    # UP
    if h > 0 and gridd[h-1][w].id == value + 1:
        returnedList += explore(gridd,h-1,w)
    # DOWN
    if h < height-1 and gridd[h+1][w].id == value + 1:
        returnedList += explore(gridd,h+1,w)
    # LEFT
    if w > 0 and gridd[h][w-1].id == value + 1:
        returnedList += explore(gridd,h,w-1)
    # RIGHT
    if w < width-1 and gridd[h][w+1].id == value + 1:
        returnedList += explore(gridd,h,w+1)
    return returnedList

summOfScores = 0

for h in range(height):
    for w in range(width):
        
        # check if trailheads
        if gridd[h][w].id == 0:
            #print("For ",gridd[h][w])
            ends = explore(gridd,h,w)

            individualEnds = []
            for end in ends:
                alreadyFound = False
                for individualEnd in individualEnds:
                    if end.equal(individualEnd):
                        alreadyFound = True
                if not alreadyFound:
                    individualEnds.append(end)
            
            print("IndividualEnds = ",len(individualEnds))
            summOfScores += len(individualEnds)


            






print(f"summOfScores = {summOfScores}")
print("--- %s seconds ---" % (time.time() - start_time))

