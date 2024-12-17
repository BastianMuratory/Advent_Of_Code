import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

stones = {}

with open(file, 'r') as file:
    for l in file:
        numbers = l.split(" ")
        for n in numbers:
            number = int(n)
            if number not in stones:
                stones[number] = 1
            else:
                stones[number] += 1
print(stones)   

def blink(stones : dict):
    i = 0
    keys = stones.keys()
    newStones = {}
    # check every stones
    for stoneNumber in keys:
        
        # If there are this kind of stones
        stonesAmount = stones[stoneNumber]
        if stonesAmount > 0:
            
            #print("Checking stone ",stoneNumber, " with amount ", stonesAmount)
            # rule 1
            if stoneNumber == 0:
                #print("Turning to 1")
                if 1 not in newStones:
                    newStones[1] = 0
                newStones[1] += stonesAmount

            
            # rule 2
            elif len(str(stoneNumber)) % 2 == 0:
                stringNumber = str(stoneNumber)
                firstpart, secondpart = stringNumber[:len(stringNumber)//2], stringNumber[len(stringNumber)//2:]
                #print("Spliting into ", firstpart ," and ", secondpart)
                stone1 = int(firstpart)
                stone2 = int(secondpart)
                # HAAAAAAAAAAAA
                if stone1 not in newStones:
                    newStones[stone1] = 0
                newStones[stone1] += stonesAmount
                if stone2 not in newStones:
                    newStones[stone2] = 0
                newStones[stone2] += stonesAmount
                


            else :
                #print("Multiplying by 2024")
                result = stoneNumber * 2024
                if result not in newStones:
                    newStones[result] = 0
                newStones[result] += stonesAmount

    return newStones

print(stones)
numberOfBlinks = 75
for b in range(numberOfBlinks):
    print(f"\nBlink n°{b}")
    stones = blink(stones)

#print(stones)
numberOfStones = 0

for stoneNumber in stones:
    numberOfStones += stones[stoneNumber]


# Puzzle One
# Number of stones = 189167
# --- 92.27516674995422 seconds ---


# Puzzle One with solution 2
# Number of stones = 189167
# --- 0.004051685333251953 seconds ---

# Puzzle 2 with solution 1

print(f"Number of stones = {numberOfStones}")
print("--- %s seconds ---" % (time.time() - start_time))

