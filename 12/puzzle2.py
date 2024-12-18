import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

class Cell:
    def __init__(self, h=0, w=0, id ="."):
        self.h = h
        self.w = w
        self.id = id
        self.fences = 0
        self.seen = False

    def move(self, dh, dw):
        self.h += dh
        self.w += dw
    
    def equal(self, otherP):
        return self.h == otherP.h and self.w == otherP.w and self.id == otherP.id

    def __eq__(self, value):
        return self.h == value.h and self.w == value.w and self.id == value.id

    def __repr__(self):
        return f"{self.id}({self.h+1},{self.w+1})[{self.fences}]"


def isAlreadyAdded(plant: Cell, regions : dict):
    alreadySeen = False

    if plant.id in regions :
        for region in regions[plant.id]:
            print(region)
            for regionPlant in region:

                if plant.equal(regionPlant):
                    alreadySeen = True
                    break
            if alreadySeen:
                break

    if alreadySeen:
        print(f"Cell {plant} already Added")

    return alreadySeen



map = []
regions = {}

with open(file, 'r') as file:
    h = 0
    for line in file:
        w = 0
        map.append([])
        for char in line:
            if char != "\n":
                plant = Cell(h,w,char)
                map[h].append(plant)
                w+=1
        h+=1
height = h
width = w




def explore(p: Cell, map : list):
    # Prevent future inspection of this plant
    p.seen = True
    fences = 4

    returnedList = [p]
    print(f"Added {p}")
    # UP
    if p.h > 0 :
        upPlant = map[p.h-1][p.w]
        if upPlant.id == p.id:
            fences -= 1
            if not upPlant.seen:
                returnedList += explore(upPlant, map)
    # Down
    if p.h < height-1 :
        downPlant = map[p.h+1][p.w]
        if downPlant.id == p.id:
            fences -= 1
            if not downPlant.seen:
                returnedList += explore(downPlant, map)
    # Left
    if p.w > 0 :
        LeftPlant = map[p.h][p.w-1]
        if LeftPlant.id == p.id:
            fences -= 1
            if not LeftPlant.seen:
                returnedList += explore(LeftPlant, map)
    # Right
    if p.w < width-1 :
        rightPlant = map[p.h][p.w+1]
        if rightPlant.id == p.id:
            fences -= 1
            if not rightPlant.seen:
                returnedList += explore(rightPlant, map)
    
    p.fences = fences
    # returns the list of neighbouring plants and count their fences
    return returnedList

print(height,width)
for line in map:
    print(line)


for line in map:
    for plant in line:
        print(f"Checking {plant}")
        # Check first if a previous explore already added the plant
        if not plant.id in regions:
            print(f"Creating list for plant {plant.id}")
            regions[plant.id] = [] # create the new list of regions

        if not plant.seen:
            # Now explore the new area
            print(f"Exploring {plant}")
            similarCloseCells  = explore(plant, map)
            # and add it to the regions dict
            regions[plant.id].append(similarCloseCells)
        else:
            print("Already added")






def printDict(d):
    print("===============")
    for key in d:
        print(key)
        print(d[key])
        print("----")
    
    print("===============")

printDict(regions)

totalPrice = 0

for key in regions:
    for region in regions[key]:
        numberOfFences = 0
        print(plant.id)
        for plant in region:
            numberOfFences += plant.fences
        print(numberOfFences)
        totalPrice += numberOfFences * len(region)
        




print(f"totalPrice = {totalPrice}")
print("--- %s seconds ---" % (time.time() - start_time))

