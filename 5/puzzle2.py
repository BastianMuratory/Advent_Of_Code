training = False
file = "exemple" if training else "inputs"
answer = 0

rules = {}
updates = []

def isPagesNumberOK(firstNumber, secondNumber):
    if secondNumber in rules and firstNumber in rules[secondNumber] :
        return False
    return True

def isPageCorrect(update, pageId):
    for otherPageId in range(pageId+1, len(update)):
            if not isPagesNumberOK(update[pageId],update[otherPageId]):
                return False, otherPageId
    return True, None

def swap(update, firstPageId, secondPageId):
    temp = update[firstPageId]
    update[firstPageId] = update[secondPageId]
    update[secondPageId] = temp
    #return update

with open(file, 'r') as file:
    checkingRules = True
    for line in file:
        if line == "\n":
            checkingRules = False
            print(rules)
        
        else:
            if checkingRules:
                pageNumbers = line.split("|")
                previousPage = int(pageNumbers[0])
                afterPage = int(pageNumbers[1])

                if not previousPage in rules:
                    rules[previousPage] = []
                rules[previousPage].append(afterPage)

            else:
                pageNumbers = line.split(",")
                update = []
                for pageNumber in pageNumbers:
                    update.append(int(pageNumber))
                updates.append(update)

sumOfMiddleNumbers = 0
incorectUpdates = []

for update in updates:
    isPageOrderCorrect = True

    for pageId in range(len(update)-1):
        for otherPageId in range(pageId+1, len(update)):
            #print(f"Checking {pageId} {otherPageId}")
            if not isPagesNumberOK(update[pageId],update[otherPageId]):
                isPageOrderCorrect = False
    
    if isPageOrderCorrect:
        sumOfMiddleNumbers += (update[int(len(update)/2)])
    else :
        incorectUpdates.append(update)

sumOfCorrectedMiddleNumbers = 0

for update in incorectUpdates:
    print(update)
    for pageId in range(len(update)-1):
        isOrderCorrect, problematicId = isPageCorrect(update, pageId)
        while not isOrderCorrect:
            print(" -> ", update)
            swap(update, pageId, problematicId)
            print(" -> ", update)
            isOrderCorrect, problematicId = isPageCorrect(update, pageId)
    
    sumOfCorrectedMiddleNumbers += (update[int(len(update)/2)])


print(f"sumOfMiddleNumbers = {sumOfMiddleNumbers}")
print(f"sumOfCorrectedMiddleNumbers = {sumOfCorrectedMiddleNumbers}")


