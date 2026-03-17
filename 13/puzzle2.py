import time
training = True
start_time = time.time()
file = "exemple" if training else "inputs"
answer = 0

#How else would someone be expected to play?
MAX_PRESSES = 100
# Price in token
PRICE_A = 3
PRICE_B = 1


"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176
"""

machineParsingProgress = 0
AX = AY = BX = BY = 0
PrizeX = PrizeY = 0
sumToken = 0

with open(file, 'r') as file:
    for line in file:
        if line != '\n':
            words = line.replace(",","").replace("X","").replace("Y","").replace("\n","").replace("=","").split(" ")
            print(words)
            if machineParsingProgress == 0: # checking for A
                AX = int(words[2])
                AY = int(words[3])
                machineParsingProgress=1

            elif machineParsingProgress == 1: # checking for B
                BX = int(words[2])
                BY = int(words[3])
                machineParsingProgress=2

            elif machineParsingProgress == 2: # checking for Prize
                PrizeX = int(words[1])# + 10000000000000
                PrizeY = int(words[2])# + 10000000000000
                machineParsingProgress=0
            
            # When the machine has been parsed
            if machineParsingProgress == 0:
                print("Calculating optimal solution")
                minA = -1
                minB = -1
                solutionFound = False
                minCost = -1
                #print(f"AX={AX} AY={AY}")
                #print(f"BX={BX} BY={BY}")
                #print(f"PrizeX={PrizeX} PrizeY={PrizeY}")

                # calculate B presses to reach the designated prize: 
                B_Press = (PrizeY - (AY * PrizeX) / AX - (BX * AY) / AX ) / (-AY / AX + BY)
                A_Press = (PrizeY - B_Press * BY) / AY


                        
                print(f"{A_Press}*AX + {B_Press}*BX = {A_Press*AX + B_Press*BX}")

                if solutionFound :
                    print(f"Best solution :{minA}xA + {minB}xB for {minCost} Tokens")
                    sumToken += minCost

print(f"Answer = {sumToken}")
print("--- %s seconds ---" % (time.time() - start_time))

