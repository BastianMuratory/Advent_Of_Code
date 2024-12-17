import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

stones = []

with open(file, 'r') as file:
    for l in file:
        numbers = l.split(" ")
        for n in numbers:
            stones.append(int(n))
print(stones)   

def blink(stones):
    i = 0
    # check every stones
    while i != len(stones):
        #print("Checking stone ",stones[i])
        # rule 1
        if stones[i] == 0:
            #print("Turning to 1")
            stones[i] = 1
        
        # rule 2
        elif len(str(stones[i])) % 2 == 0:
            string = str(stones[i])
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            #print("Spliting into ", firstpart ," and ", secondpart)
            stone1 = int(firstpart)
            stone2 = int(secondpart)
            # HAAAAAAAAAAAAA
            #print([stone1, stone2])
            #print(stones[:i])
            #print(stones[i+1:])
            stones = stones[:i] + [stone1, stone2] + stones[i+1:]
            #print(stones)
            i+=1
        
        else :
            #print("Multiplying by 2024")
            stones[i] = stones[i] * 2024

        i+=1
    return stones

print(stones)
numberOfBlinks = 6
for b in range(numberOfBlinks):
    print(f"\nBlink n°{b}")
    stones = blink(stones)
    #print(stones)

print(f"Number of stones = {len(stones)}")
print("--- %s seconds ---" % (time.time() - start_time))

