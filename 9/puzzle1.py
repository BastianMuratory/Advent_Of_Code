import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

diskMap = []

with open(file, 'r') as file:
    for line in file:
        diskMap = line

print(f"diskMap {diskMap}")

def convertToBlock(diskMap):
    result = []
    index = 0

    if diskMap == "":
        return ""

    # Is space used or free
    used = True
    for elem in diskMap:
        lenght = int(elem)
        for i in range(lenght):
            if used:
                result.append(index)
            else:
                result.append(".")

        # Alternante between used and free and increment index
        used = not used
        if used :
            index += 1
    return result


diskBlock = convertToBlock(diskMap)
print(diskBlock)

for i in range(len(diskBlock)):
    # get used spaces from the end
    if diskBlock[-i-1] != '.':
        #print(f"checking {diskBlock[-i-1]}")
        swapped = False
        
        # find first empty space
        for j in range(0,len(diskBlock)-i-1):
            if diskBlock[j] == ".":
                
                # Swap empty with used
                diskBlock[j] = diskBlock[-i-1]
                diskBlock[-i-1] = "."
                print(f"Swapping {j} and {len(diskBlock)-i-1}")
                break

print(diskBlock)

checksum = 0

id = 0
for elem in diskBlock:
    if elem == ".":
        break
    else:
        checksum += id * elem
    id += 1


print(f"checksum = {checksum}")
print("--- %s seconds ---" % (time.time() - start_time))

