training = False
file = "exemple" if training else "inputs"

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def charCanBeValid(char, currentState, validSequence, consecutiveNumbers):
    print(f"Char = {char}")
    isAValidChar = False
    shouldIncreaseDicoId = False
    number = 0

    if currentState == 0:
        testedSequence = validSequence + char
        #print(f"Current = [{validSequence}] Testing [{testedSequence}]")
        
        # check if it's the first char
        if not validSequence and char == 'm' or char == 'd':
            isAValidChar = True

        # check if validSequence is not empty and seems ok
        elif validSequence and ( testedSequence in "mul(" or testedSequence in "do()" or testedSequence in "don't()") :
            isAValidChar = True
            if testedSequence == "mul(" or testedSequence == "do()" or testedSequence == "don't()":
                shouldIncreaseDicoId = True

    
    if currentState == 1:
        if char in numbers :
            consecutiveNumbers += 1
            #print(f"consecutiveNumbers = {consecutiveNumbers}")
            if consecutiveNumbers > 3 :
                isAValidChar = False
            else:
                isAValidChar = True

        if char == ',': 
            isAValidChar = True
            shouldIncreaseDicoId = True
            #print(validSequence[len(validSequence)-consecutiveNumbers:len(validSequence)])
            number = validSequence[len(validSequence)-consecutiveNumbers:len(validSequence)]
    
    if currentState == 2:
        if char in numbers :
            consecutiveNumbers += 1
            #print(f"consecutiveNumbers = {consecutiveNumbers}")
            if consecutiveNumbers > 3 :
                isAValidChar = False
            else:
                isAValidChar = True

        if char == ')': 
            isAValidChar = True
            shouldIncreaseDicoId = True
            #print(validSequence[len(validSequence)-consecutiveNumbers:len(validSequence)])
            number = int(validSequence[len(validSequence)-consecutiveNumbers:len(validSequence)])

    return isAValidChar, shouldIncreaseDicoId, consecutiveNumbers, number


sumOfMult = 0

with open(file, 'r') as file:
    
    validSequence = ""
    
    # The state correspond to which part should be checked
    # 0 = "mul("
    # 1 = "number,"
    # 2 = "number)"
    state = 0
    
    number1 = 0
    number2 = 0
    consecutiveNumbers = 0

    doOrNot = 1

    for line in file:
        
        for char in line :
            isValid, increaseDicoId, consecutiveNumbers, number = charCanBeValid(char, state, validSequence, consecutiveNumbers)
            
            # if the char can be accepted as input
            if isValid:
                validSequence += char
                print(f"Current validSequence = {validSequence}")

                # Update the index to check next part of the dico
                if increaseDicoId :
                    #print("Goto next state")
                    state += 1
                    consecutiveNumbers = 0

                    if state == 1:
                        if validSequence == "do()" :
                            doOrNot = 1
                            validSequence = ""
                            state = 0
                        elif validSequence == "don't()" :
                            doOrNot = 0
                            validSequence = ""
                            state = 0

                    if number != 0 and state == 2:
                        print(f"Found the first number {number}")
                        number1 = number

                    if number != 0 and state == 3:
                        print(f"Found the second number {number}")
                        number2 = number

                        print("===============")
                        print(f" {doOrNot} X {number1} X {number2}")
                        print("===============")
                        sumOfMult += ( doOrNot * int(number1) * int(number2))
                                
                        validSequence = ""
                        number1 = 0
                        number2 = 0
                        state = 0

            # If the char can't be accepted as input
            else :
                print("")
                validSequence = ""
                number1 = 0
                number2 = 0
                state = 0

            


print(f"sumOfMult = {sumOfMult}")


