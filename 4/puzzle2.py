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
        if wordSearch[line][column] == 'M':
            print(f"M in {line} {column}")
            
            # search 
            #  M M
            #   A
            #  S S
            if line <= len(wordSearch) - 3 and column <= len(wordSearch[line]) - 3: # check if there is enough space
                if wordSearch[line][column+2] == 'M' and wordSearch[line+1][column+1] == 'A' and wordSearch[line+2][column] == 'S' and wordSearch[line+2][column+2] == 'S': # check if letters correspond
                    numberOfXmas += 1

            # search 
            #  M S
            #   A
            #  M S
            if line <= len(wordSearch) - 3 and column <= len(wordSearch[line]) - 3: # check if there is enough space
                if wordSearch[line][column+2] == 'S' and wordSearch[line+1][column+1] == 'A' and wordSearch[line+2][column] == 'M' and wordSearch[line+2][column+2] == 'S': # check if letters correspond
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
         if reversedWordSearch[line][column] == 'M':
            print(f"M in {line} {column}")
            
            # search 
            #  M M
            #   A
            #  S S
            if line <= len(reversedWordSearch) - 3 and column <= len(reversedWordSearch[line]) - 3: # check if there is enough space
                if reversedWordSearch[line][column+2] == 'M' and reversedWordSearch[line+1][column+1] == 'A' and reversedWordSearch[line+2][column] == 'S' and reversedWordSearch[line+2][column+2] == 'S': # check if letters correspond
                    numberOfXmas += 1

            # search 
            #  M S
            #   A
            #  M S
            if line <= len(reversedWordSearch) - 3 and column <= len(reversedWordSearch[line]) - 3: # check if there is enough space
                if reversedWordSearch[line][column+2] == 'S' and reversedWordSearch[line+1][column+1] == 'A' and reversedWordSearch[line+2][column] == 'M' and reversedWordSearch[line+2][column+2] == 'S': # check if letters correspond
                    numberOfXmas += 1




print(f"numberOfXmas = {numberOfXmas}")


