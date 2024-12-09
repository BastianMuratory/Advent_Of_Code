training = True
file = "exemple" if training else "inputs"
answer = 0

rules = {}
updates = []

def isPagesNumberOK(firstNumber, secondNumber):
    if firstNumber in rules[secondNumber] :
        return False 

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
            

for update in updates:
    print(update)
    isPageOrderCorrect = True

    for pageId in range(len(update)):
        for otherPageId in range(pageId, len(update)):
            if not isPagesNumberOK(update[pageId],update[otherPageId])






print(f"Answer = {answer}")


