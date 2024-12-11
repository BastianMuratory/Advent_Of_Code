import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
numberOfAntinodes = 0

string = []
antennas = {}

class Position:
    def __init__(self, h=0, w=0):
        self.h = h
        self.w = w

    def move(self, dh, dw):
        self.h += dh
        self.w += dw
    
    def equal(self, otherP):
        return self.h == otherP.h and self.w == otherP.w
    

    def __repr__(self):
        return f"Position({self.h+1}, {self.w+1})"
    
with open(file, 'r') as file:
    h=0 # height
    for line in file:
        string.append(line[0:-1])
        print(line[0:-1])

        w = 0 # width
        for antenna in line[0:-1]:
            # check if there is an antenna 
            
            if antenna != '.':
                antennaPosition = Position(h,w)

                if not antenna in antennas:
                    antennas[antenna] = []
                
                antennas[antenna].append(antennaPosition)
            w += 1
        h += 1
height = len(string)
width = len(string[0])
print(antennas)
print(f"height {height} width {width}\n")

antinodesLocations = []

for antenna in antennas:
    currentAntennasAntinodes = []
    currentAntennas = antennas[antenna]
    
    print(f"Calculating antinodes for {antenna}")
    print(f"With {currentAntennas}")

    # Single antennas do not add antinodes
    if len(currentAntennas) > 1:

        # Compare each antennas with each other one
        for i in range(len(currentAntennas)):

            # Antinode is created at antennas' position
            print(f"\nChecking Antenna {currentAntennas[i]}")
            currentAntennasAntinodes.append(Position(currentAntennas[i].h, currentAntennas[i].w))

            for j in range(len(currentAntennas)):
                if i != j : # Don't compare one antenna to itself
                    print(f"Compare with Antenna {currentAntennas[j]}")

                    # Calculate Antinode position
                    deltaH = currentAntennas[i].h - currentAntennas[j].h
                    deltaW = currentAntennas[i].w - currentAntennas[j].w
                    print(f"deltaH {deltaH} deltaW {deltaW}")

                    numberOfDeltaBeforeGoingOutside = int(max(abs(width/deltaW), abs(height/deltaH)))

                    for repeat in range(1,numberOfDeltaBeforeGoingOutside):

                        antinodePosition = Position(currentAntennas[i].h + repeat * deltaH, currentAntennas[i].w + repeat * deltaW)
                        
                        # if the antinode is inside the map
                        if antinodePosition.h >= 0 and antinodePosition.h < height and antinodePosition.w >= 0 and antinodePosition.w < width:
                            print(f"Antinode Position = {antinodePosition}")

                            # add the position of the created antinode
                            currentAntennasAntinodes.append(antinodePosition)
        
        # now make sure they are not already present and inside the map
        for antinode in currentAntennasAntinodes:
            
            alreadyPresent = False
            for previousAntinode in antinodesLocations:
                if antinode.equal(previousAntinode):
                    alreadyPresent = True
                    break
            
            if not alreadyPresent:
                antinodesLocations.append(antinode)



output = []
for i in range(height):
    line = []
    for j in range(height):
        line.append(".")
    output.append(line)

print("\nFinal Antinodes")
for antinode in antinodesLocations:
    print(antinode)
    output[antinode.h][antinode.w] = "#"
    



with open(f"output.txt", "w") as file:
    for line in output:
        for char in line:
            file.write(char)
        file.write("\n")



numberOfAntinodes = len(antinodesLocations)

print(f"numberOfAntinodes = {numberOfAntinodes}")
print("--- %s seconds ---" % (time.time() - start_time))

