import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0


class Data:
    def __init__(self, id, size, free):
        self.id = id
        self.size = size
        self.free = free

        self.next = None
        self.previous = None

    def printBlock(self):
        if self.free :
            return "." * self.size
        else :
            return str(self.id) * self.size
    
    def list(self):
        lst = []
        for i in range(self.size):
            if not self.free:
                lst.append(self.id)
            else:
                lst.append(".")
        return lst

dataStream : Data = None


with open(file, 'r') as file:
    for line in file:
        id = 0
        freeSpace = False # first number is not free space
        previous : Data = None

        for char in line:
            data : Data = None
            if not freeSpace :
                data = Data (id, int(char), False)
                id += 1
            else:
                data = Data (-1, int(char), True)
            freeSpace = not freeSpace
            
            if dataStream == None:
                dataStream = data
            else : 
                data.previous = previous
                previous.next = data
            previous = data

last = data


iter = dataStream
diskMap = ""
while iter != None:
    diskMap += iter.printBlock()
    iter = iter.next
print(diskMap)


def swapData(data1: Data, data2 : Data):
    if not data1.free : 
        print("DATA 1 NOT FREE")
    
    if data1.size < data2.size:
        print("DATA 1 TOO LITTLE")

    #print(f"Swapping {data2.id} with free space {data1.size}")
    
    # If same size
    # A-> <-data1-> <-B
    # C-> <-data2-> <-D
    # becomes 
    # A-> <-data2-> <-B
    # C-> <-data1-> <-D
    if data1.size == data2.size:
        if data1.next != data2:
            # A
            data1.previous.next = data2
            # B 
            data1.next.previous = data2
            # C
            data2.previous.next = data1
            # D
            if not data2.next == None:
                data2.next.previous = data1
            
            # internal
            temp = data1.previous
            data1.previous = data2.previous
            data2.previous = temp
            
            temp = data1.next
            data1.next = data2.next
            data2.next = temp

        else: # edge case
            print("EDGE CASE HAAAAAAAAAAAAAAAAA")
            print("EDGE CASE HAAAAAAAAAAAAAAAAA")
            print("EDGE CASE HAAAAAAAAAAAAAAAAA")
            print("EDGE CASE HAAAAAAAAAAAAAAAAA")
            print("EDGE CASE HAAAAAAAAAAAAAAAAA")
            # edge case
            # A-> <-data1-> <-data2-> <-B
            # becomes 
            # A-> <-data2-> <-data1-> <-B
            A = data1.previous
            B = data2.next

            # by order of arrows
            A.next = data2
            data2.previous = A
            data2.next = data1
            data1.previous = data2
            data1.next = B
            B.previous = data1
            
    # If different sizes
    # A-> <-data1-> <-B
    # C-> <-data2-> <-D
    # becomes 
    # A-> <-data2-> <-freeDifference-> <-B
    # C-> <-data1-freeDifference-> <-D
    else :
        # Create the new free data
        difference = data1.size - data2.size
        newData = Data(-1,difference,True)
        newData.previous = data2
        newData.next = data1.next
        data1.size -= difference

        # A 
        data1.previous.next = data2
        # B 
        data1.next.previous = newData
        # C
        data2.previous.next = data1
        # D
        if not data2.next == None:
            data2.next.previous = data1

        data1.next = data2.next
        data2.next = newData
        
        temp = data1.previous
        data1.previous = data2.previous
        data2.previous = temp
    #print("Swapped")



# Reorder the free space
iter = last
init = True
it = 0
while iter != None :
    previousOne = iter.previous

    # Only process filled spaces
    if not iter.free:
        print(f"iter.id {iter.id}")

        # then find large enough free space
        findFree = dataStream

        while findFree != iter:
            #print(f"Comparing with {findFree.id}")
            nextOne = findFree.next

            if findFree.free:
                if findFree.size >= iter.size:
                    swapData(findFree, iter)
                    break
            findFree = nextOne

    iter = previousOne

iter = dataStream
diskBlock = []

#print(diskBlock)
while iter != None:
    #print(iter.id)
    for item in iter.list():
        diskBlock.append(item)
    iter = iter.next
#print(diskBlock)

checksum = 0

id = 0
for elem in diskBlock:
    #print(elem)
    if elem != ".":
        checksum += id * int(elem)
    id += 1


print(f"checksum = {checksum}")
print("--- %s seconds ---" % (time.time() - start_time))
