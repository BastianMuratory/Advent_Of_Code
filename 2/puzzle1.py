safeReports = 0
training = False
file = "exemple" if training else "inputs"

with open(file, 'r') as file:
    for line in file:
        report = []
        reportIsSafe = False
        
        # Create the variable holding the report as int to be processed later
        for number_in_char in line.split(" "):
            report.append(int(number_in_char))

        # Calculate the delats between each values
        deltas = []
        for id in range(1,len(report)):
            previousNumber = report[id-1]
            currentNumber = report[id]
            deltas.append(currentNumber - previousNumber)

        # check if all deltas are positives and in [+1, +3]
        if all(delta > 0 and delta < 4 for delta in deltas) :
            reportIsSafe = True

        # check if all deltas are negatives and in [-1, -3]
        if all(delta < 0 and delta > -4 for delta in deltas) :
            reportIsSafe = True
        
        if reportIsSafe :
            safeReports +=1

    print(f"Answer = {safeReports}")


