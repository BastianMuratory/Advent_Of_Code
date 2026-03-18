import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

with open(file, 'r') as file:
    for line in file:
        pass



print(f"Answer = {answer}")
print("--- %s seconds ---" % (time.time() - start_time))

