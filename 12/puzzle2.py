import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

class Cell:
    def __init__(self, h=0, w=0, id ="."):
        self.h = h
        self.w = w
        self.id = id
        self.seen = False
        self.fences = 0

        self.u = True
        self.d = True
        self.l = True
        self.r = True

    def move(self, dh, dw):
        self.h += dh
        self.w += dw
    
    def equal(self, otherP):
        return self.h == otherP.h and self.w == otherP.w and self.id == otherP.id

    def __eq__(self, value):
        return self.h == value.h and self.w == value.w and self.id == value.id

    def __repr__(self):
        return f"{self.id}({self.h+1},{self.w+1})" + (f"[{self.u}{self.r}{self.d}{self.l}]" if self.seen else "")


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


print(height,width)
for line in map:
    print(line)

print("\n============\n")

def explore(p: Cell, map : list):
    # Prevent future inspection of this plant
    #print(f"Exploring {p}")
    p.seen = True
    fences = 4

    returnedList = [p]
    # UP
    if p.h > 0 :
        upPlant = map[p.h-1][p.w]
        if upPlant.id == p.id:
            fences -= 1
            p.u = False # No fences on the upper side
            if not upPlant.seen:
                returnedList += explore(upPlant, map)
    # Down
    if p.h < height-1 :
        downPlant = map[p.h+1][p.w]
        if downPlant.id == p.id:
            fences -= 1
            p.d = False # No fences on the lower side
            if not downPlant.seen:
                returnedList += explore(downPlant, map)
    # Left
    if p.w > 0 :
        LeftPlant = map[p.h][p.w-1]
        if LeftPlant.id == p.id:
            fences -= 1
            p.l = False # No fences on the left
            if not LeftPlant.seen:
                returnedList += explore(LeftPlant, map)
    # Right
    if p.w < width-1 :
        rightPlant = map[p.h][p.w+1]
        if rightPlant.id == p.id:
            fences -= 1
            p.r = False # No fences on the right
            if not rightPlant.seen:
                returnedList += explore(rightPlant, map)
    
    p.fences = fences
    #print(f"Finished {p}")
    # returns the list of neighbouring plants and count their fences
    return returnedList

for line in map:
    for plant in line:
        #print(f"Pointer at {plant}")
        # Check first if a previous explore already added the plant
        if not plant.id in regions:
            #print(f"Creating list for type {plant.id}")
            regions[plant.id] = [] # create the new list of regions

        if not plant.seen:
            # Now explore the new area
            #print(f"Plant never seen, exploring")
            similarCloseCells  = explore(plant, map)
            # and add it to the regions dict
            regions[plant.id].append(similarCloseCells)
        else:
            pass
            #print("Already seen, do nothing")






def printDict(d):
    print("===============")
    for key in d:
        print(key)
        print(d[key])
        print("----")
    
    print("===============")
printDict(regions)

class Fence:
    def __init__(self, p1 : tuple, p2 : tuple, id, vertical : bool):
        self.p1 = p1
        self.p2 = p2
        self.vertical = vertical
        self.path = None
        self.ordered = False
        self.type = id
    
    def __repr__(self):
        return f" [{self.p1[0]},{self.p1[1]},{self.p2[0]},{self.p2[1]},{self.type}]"
    
    def has(self, point : tuple):
        return self.p1 == point or self.p2 == point

    def equal(self, f):
        return f.p1 == self.p1 and f.p2 == self.p2

def processConnectedFences(fence, fences : list, pathId, FencesToVisit : list, fencesCopy : list):
    connected = []

    junction = 0
    for otherFence in fencesCopy:
        if not fence.equal(otherFence) and (otherFence.has(fence.p1) or otherFence.has(fence.p2)):
            junction += 1
            #Make sure not already processed
            if otherFence.path == None :
                otherFence.path = pathId
                connected.append(otherFence)
    '''if junction >= 3:
        fuck = False

        wrongFenceH2 = None
        wrongFenceW2 = None

        print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(f"connected {connected}")
        for f2 in connected:
            if f2.vertical == fence.vertical : 
                f2.path = None
                print(f"Removing {f2}")
                connected.remove(f2)
        
        if fence.vertical :
            # p1.w == p2.w
            h = int((fence.p1[0] + fence.p2[0])/2)
            y = fence.p1[1]-1
            print(map[h][y])
            if map[h][y].id == fence.type:
                print("Case 1")
                wrongFenceH = max(fence.p1[0], fence.p2[0])
                wrongFenceW = fence.p1[1] - 1
                print("Also remove ")
                wrongFenceH2 = min(fence.p1[0], fence.p2[0])
                wrongFenceW2 = fence.p1[1] - 1
            else:
                print("Case 2")
                wrongFenceH = min(fence.p1[0], fence.p2[0])
                wrongFenceW = fence.p1[1] + 1
                print("Also remove ")
                wrongFenceH2 = max(fence.p1[0], fence.p2[0])
                wrongFenceW2 = fence.p1[1] + 1


        else :
            # p1.h == p2.h
            h = fence.p1[0]
            y = int((fence.p1[1] + fence.p2[1])/2)
            print(map[h][y])
            if map[h][y].id == fence.type:
                print("Case 3")
                wrongFenceH = fence.p1[0] + 1 
                wrongFenceW = max(fence.p1[0], fence.p2[0])
                print("Also remove ")
                wrongFenceH2 = fence.p1[0] + 1 
                wrongFenceW2 = min(fence.p1[0], fence.p2[0])
            else:
                print("Case 4")
                wrongFenceH = fence.p1[0] - 1 
                wrongFenceW = max(fence.p1[0], fence.p2[0])
                print("Also remove ")
                wrongFenceH2 = fence.p1[0] - 1 
                wrongFenceW2 = min(fence.p1[0], fence.p2[0])
        
        print(f"Removing {wrongFenceH} {wrongFenceW}")
        for f2 in connected:
            if f2.has((wrongFenceH, wrongFenceW)) : 
                f2.path = None
                print(f"Removing {f2}")
                connected.remove(f2)
            
            if wrongFenceW2 != None:
                if f2.has((wrongFenceH2, wrongFenceW2)) : 
                    f2.path = None
                    print(f"Removing ALSO {f2}")
                    if f2 in connected: # THIS IS REALLY DANGEROUS
                        connected.remove(f2)



        print(f"Connected Fences {connected}")
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    else :
        print(f"Connected Fences {connected}")
    '''
    for f in connected:
        fences.remove(f)

    #if fuck : exit(0)    
    return connected

def split(fences : list):
    paths = {}

    # Make initial copy 
    fencesCopy = []
    for f in fences:
        fencesCopy.append(f)

    pathId = 0
    paths[pathId] = []
    FencesToVisit = []
    # Add the first element to check
    FencesToVisit.append(fences[0])
    fences.remove(fences[0])

    
    while len(fences) > 0:
        
        # If a new path needs to be added
        if len(FencesToVisit) == 0:
            # Make another copy
            fencesCopy = []
            for f in fences:
                fencesCopy.append(f)

            FencesToVisit.append(fences[0])
            fences.remove(fences[0])
            pathId += 1
            paths[pathId] = []
            print(f" ##### There is another path {pathId+1} here #####")
            


        # Make a copy of the fences not yet discovered
        
        
        # get all the fences connected to the first one

        print(f"fencesCopy  {fencesCopy}")
        while len(FencesToVisit) > 0:
            print(f"FencesToVisit {FencesToVisit}")
            print(f"Processing {FencesToVisit[0]}")
            currentFence = FencesToVisit[0]
            currentFence.path = pathId # Make sure it can't be processed again
            connectedFences = processConnectedFences(currentFence, fences, pathId, FencesToVisit, fencesCopy)
            for f in connectedFences:
                FencesToVisit.append(f)
            paths[pathId].append(currentFence)
            FencesToVisit.remove(currentFence)

    return paths

def getFences(tile : Cell):
    fences = []
    if tile.u:
        p1 = (tile.h + (0.1 if tile.l else 0), tile.w + (0.1 if tile.l else 0))
        p2 = (tile.h + (0.1 if tile.r else 0), tile.w + 1 - (0.1 if tile.r else 0))
        fences.append(Fence(p1,p2,tile.id, False))
    if tile.d:
        p1 = (tile.h + 1 - (0.1 if tile.l else 0), tile.w + (0.1 if tile.l else 0))
        p2 = (tile.h + 1 - (0.1 if tile.r else 0), tile.w + 1 - (0.1 if tile.r else 0))
        fences.append(Fence(p1,p2,tile.id, False))
    if tile.l:
        p1 = (tile.h + (0.1 if tile.u else 0), tile.w + (0.1 if tile.u else 0))
        p2 = (tile.h + 1 - (0.1 if tile.d else 0), tile.w + (0.1 if tile.d else 0))
        fences.append(Fence(p1,p2,tile.id, True))
    if tile.r:
        p1 = (tile.h + (0.1 if tile.u else 0), tile.w + 1 - (0.1 if tile.u else 0))
        p2 = (tile.h + 1 - (0.1 if tile.d else 0), tile.w + 1 - (0.1 if tile.d else 0))
        fences.append(Fence(p1,p2,tile.id, True))

    print(f"Fences {fences}")
    return fences

def findNext(point : tuple, fences : list):
    #print(f"Looking for {point}")
    for fence in fences:
        if fence.has(point) and not fence.ordered:
            #print(f"Next fence {fence}")
            return fence
    
    #print("HAAAAAAAAAAA")
    return None

def reorder(pathDict : dict):
    for pathId in pathDict:
        unsortedList = pathDict[pathId]
        #print("Now Sorting :")
        #print(unsortedList)

        SortedList = []

        currentFence = unsortedList[0]
        currentFence.ordered = True
        SortedList.append(currentFence)
        checkingPoint1 = True 
        # need to do one operation for every fence

        nextFence = findNext(currentFence.p1, unsortedList)
        while nextFence != None:
            if currentFence.has(nextFence.p1):
                checkingPoint1 = False # need to check p2 as p1 is in common with previous fence
            else : 
                checkingPoint1 = True
            SortedList.append(nextFence)
            nextFence.ordered = True
            currentFence = nextFence

            if checkingPoint1 :
                nextFence = findNext(nextFence.p1, unsortedList)
            else:
                nextFence = findNext(nextFence.p2, unsortedList)
        
        #print(SortedList)
        pathDict[pathId] = SortedList

def printD(d : dict):
    print("###")
    for k in d:
        print(f"{k} => {d[k]}")
    print("###")

def countEdges(splitedFences):
    numOfEdges = 0
    print(splitedFences)
    for pathId in splitedFences:
        currentPath = splitedFences[pathId]
        isVertical = currentPath[-1].vertical
        for fence in currentPath:
            if fence.vertical == isVertical :
                print("SameDirection")
            else:
                print("Turned")
                numOfEdges += 1
                isVertical = not isVertical
    print("Number of edges = ",numOfEdges)
    return numOfEdges

def getEdges(region : list[Cell]):
    print(f"Counting edges in {region}")
    totalFences = []

    for tile in region:
        tileSpecificFences = getFences(tile)
        
        for fence in tileSpecificFences:
            totalFences.append(fence)

    print("\nSplit")
    splitedFences = split(totalFences)
    printD(splitedFences)

    print("Reorder")
    reorder(splitedFences)

    print("Count")
    return countEdges(splitedFences)
            



totalPrice = 0
for key in regions:
    for region in regions[key]:
        numberOfEdges = getEdges(region)
        print(numberOfEdges)
        totalPrice += numberOfEdges * len(region)
        


# 829756



print(f"totalPrice = {totalPrice}")
print("--- %s seconds ---" % (time.time() - start_time))

