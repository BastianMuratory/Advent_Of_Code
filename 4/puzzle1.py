training = False
file = "exemple" if training else "inputs"
numberOfXmas = 0
wordSearch = [] 

with open(file, 'r') as file:
    for line in file:
        wordSearch.append(line[0:-1])

for l in wordSearch:
    print(l)



for line in range(len(wordSearch)):
    for column in range(len(wordSearch[line])):
        if wordSearch[line][column] == 'X':
            print(f"X in {line} {column}")
            
            # search NORTH EAST
            if line >= 3 and column <= len(wordSearch[line]) - 4: # check if there is enough space
                if wordSearch[line-1][column+1] == 'M' and wordSearch[line-2][column+2] == 'A' and wordSearch[line-3][column+3] == 'S': # check if letters correspond
                    print(f"Found NE")
                    numberOfXmas += 1

            # search EAST
            if column <= len(wordSearch[line]) - 3: # check if there is enough space
                if wordSearch[line][column+1] == 'M' and wordSearch[line][column+2] == 'A' and wordSearch[line][column+3] == 'S': # check if letters correspond
                    print(f"Found E")
                    numberOfXmas += 1

            # search SOUTH EAST
            if line <= len(wordSearch) - 4 and column <= len(wordSearch[line]) - 4: # check if there is enough space
                if wordSearch[line+1][column+1] == 'M':
                    if wordSearch[line+2][column+2] == 'A':
                        print(f"Searching {line+3} {column+3}")
                        if wordSearch[line+3][column+3] == 'S': # check if letters correspond
                            print(f"Found SE")
                            numberOfXmas += 1

            # search SOUTH
            if line <= len(wordSearch) - 4: # check if there is enough space
                if wordSearch[line+1][column] == 'M' and wordSearch[line+2][column] == 'A' and wordSearch[line+3][column] == 'S': # check if letters correspond
                    print(f"Found S")
                    numberOfXmas += 1


print("\n\n")
# now reverse the word search
reversedWordSearch = []
for line in range(len(wordSearch)):
    reversedLine = ""
    for column in range(len(wordSearch[line])):
        reversedLine += wordSearch[len(wordSearch)-1 - line][len(wordSearch[line])-1 - column]
    reversedWordSearch.append(reversedLine)


for l in reversedWordSearch:
    print(l)

print("\n\n")


# And check again 
for line in range(len(reversedWordSearch)):
    for column in range(len(reversedWordSearch[line])):
        if reversedWordSearch[line][column] == 'X':
            
            # search NORTH EAST
            if line >= 3 and column <= len(reversedWordSearch[line]) - 4: # check if there is enough space
                if reversedWordSearch[line-1][column+1] == 'M' and reversedWordSearch[line-2][column+2] == 'A' and reversedWordSearch[line-3][column+3] == 'S': # check if letters correspond
                    numberOfXmas += 1

            # search EAST
            if column <= len(reversedWordSearch[line]) - 4: # check if there is enough space
                if reversedWordSearch[line][column+1] == 'M' and reversedWordSearch[line][column+2] == 'A' and reversedWordSearch[line][column+3] == 'S': # check if letters correspond
                    numberOfXmas += 1

            # search SOUTH EAST
            if line <= len(reversedWordSearch) - 4 and column <= len(reversedWordSearch[line]) - 4: # check if there is enough space
                if reversedWordSearch[line+1][column+1] == 'M' and reversedWordSearch[line+2][column+2] == 'A' and reversedWordSearch[line+3][column+3] == 'S': # check if letters correspond
                    numberOfXmas += 1

            # search SOUTH
            if line <= len(reversedWordSearch) - 4: # check if there is enough space
                if reversedWordSearch[line+1][column] == 'M' and reversedWordSearch[line+2][column] == 'A' and reversedWordSearch[line+3][column] == 'S': # check if letters correspond
                    numberOfXmas += 1




print(f"numberOfXmas = {numberOfXmas}")


