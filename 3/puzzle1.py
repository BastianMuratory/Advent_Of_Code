training = False
file = "exemple" if training else "inputs"

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def charCanBeValid(char, currentState, validSequence, consecutiveNumbers):
    print(f"Current char = {char}")
    isAValidChar = False
    shouldIncreaseDicoId = False
    number = 0

    if currentState == 0:
        if char == 'm':
            isAValidChar = True

        # check if validSequence is not empty
        elif validSequence and validSequence + char in "mul(":
            isAValidChar = True    
            if char == '(':
                shouldIncreaseDicoId = True
    
    if currentState == 1:
        if char in numbers :
            consecutiveNumbers += 1
            print(f"consecutiveNumbers = {consecutiveNumbers}")
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
            print(f"consecutiveNumbers = {consecutiveNumbers}")
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


    for line in file:
        
        for char in line :
            isValid, increaseDicoId, consecutiveNumbers, number = charCanBeValid(char, state, validSequence, consecutiveNumbers)
            
            # if the char can be accepted as input
            if isValid:
                validSequence += char
                print(f"Current validSequence = {validSequence}")

                # Update the index to check next part of the dico
                if increaseDicoId :
                    state += 1
                    consecutiveNumbers = 0

                    if number != 0 and state == 2:
                        print(f"Found the first number {number}")
                        number1 = number

                    if number != 0 and state == 3:
                        print(f"Found the second number {number}")
                        number2 = number

                        print("===============")
                        print(f" {number1} X {number2}")
                        print("===============")
                        sumOfMult += (int(number1) * int(number2))
                                
                        validSequence = ""
                        number1 = 0
                        number2 = 0
                        state = 0



            # If the char can't be accepted as input
            else :
                validSequence = ""
                number1 = 0
                number2 = 0
                state = 0

            


print(f"sumOfMult = {sumOfMult}")


