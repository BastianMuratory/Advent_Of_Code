safeReports = 0
training = False
file = "exemple" if training else "inputs"

def calculateDeltas(report):
    deltas = []
    for id in range(1,len(report)):
        previousNumber = report[id-1]
        currentNumber = report[id]
        deltas.append(currentNumber - previousNumber)
    return deltas

def checkReport(report):
    # Calculate the delats between each values
    print("\nReport = ",report)

    deltas = calculateDeltas(report)
    print("deltas = ",deltas)

    # Check if everything is good
    if checkDeltas(deltas) :
        return True
    
    else:
        print("ERROR")
        for id_to_be_removed in range(len(report)):
            reportMinus1 = []
            for id in range(len(report)):
                if id != id_to_be_removed:
                    reportMinus1.append(report[id])
            print("Checking = ",reportMinus1)
            deltasMinus1 = calculateDeltas(reportMinus1)
            if checkDeltas(deltasMinus1):
                print("SAFE solution has been found")
                return True
    
    print("No safe solutions")
    return False
    


def checkDeltas(deltas):
    deltasAreGood = False
    # check if all deltas are positives and in [+1, +3]
    if all(delta > 0 and delta < 4 for delta in deltas) :
        deltasAreGood = True

    # check if all deltas are negatives and in [-1, -3]
    if all(delta < 0 and delta > -4 for delta in deltas) :
        deltasAreGood = True

    return deltasAreGood


def remove1stBadDelta(deltas):
    shortenedDeltasList = []

    print("One or more error Detected")
    # check if mostly increasing
    increasings = 0
    decreasings = 0
    stable = 0
    for delta in deltas:
        if delta > 0:
            increasings += 1
        if delta < 0:
            decreasings += 1
        else:
            stable += 1

            


with open(file, 'r') as file:
    for line in file:
        report = []
        reportIsSafe = False
        
        # Create the variable holding the report as int to be processed later
        for number_in_char in line.split(" "):
            report.append(int(number_in_char))


        if checkReport(report) :
            safeReports +=1

    print(safeReports)


