import time
training = False
start_time = time.time()
file = "exemple" if training else "inputs"
numberOfSolvableEquations = 0

equations = []
with open(file, 'r') as file:
    for line in file:
        sides = line.split(":")

        equation = []
        equation.append(int(sides[0]))

        numbers = []
        for n in sides[1].split(" "):
            if n != '':
                numbers.append(int(n))
        
        equation.append(numbers)
        equations.append(equation)
        print(equation)

print("\n============\n")

def eval(value, values : list, possibleResults : list):
    #  end recursion if last two values
    if len(values) == 1:
        possibleResults.append(value + values[0])
        possibleResults.append(value * values[0])


    # add, then multiply and eval output
    else :
        newValue = values[0]
        eval(value + newValue, values[1:], possibleResults)
        eval(value * newValue, values[1:], possibleResults)

totalCalibrationResult = 0
for eq in equations:
    print(eq)
    possibleResults = []

    # Eval first number and rest of the list
    print(f"Testing {eq[1][0]} and {eq[1][1:]}")
    eval(eq[1][0], eq[1][1:], possibleResults)

    if eq[0] in possibleResults:
        totalCalibrationResult += eq[0]
        numberOfSolvableEquations += 1
    print("\n")



print(f"numberOfSolvableEquations = {numberOfSolvableEquations}")
print(f"totalCalibrationResult = {totalCalibrationResult}")

print("--- %s seconds ---" % (time.time() - start_time))

