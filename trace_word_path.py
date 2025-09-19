def scan_letters(matrix, letter, query) -> list: #this function returns a list with all the positions of the first query letter
    possible_starts = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == letter:
                possible_starts.append((row,col))
    if len(query) > (row+1)*(col+1):
        raise Exception(f"Query {query} longer than matrix dimensions") #I take care of this exception here 
                                                                #because I loop through all the matrix elements
    return possible_starts

def scan_around(matrix, positions, letter) -> list: 
#this function scans around the last position of the passed path and 
#returns compatible positions for the next query letter
    new_positions = []
    for x in range(-1,2):
        for y in range(-1,2):
            last_pos = positions[-1]
            row = last_pos[0] + x
            col = last_pos[1] + y
            try:
                if matrix[row][col] == letter and (row,col) not in positions and row >= 0 and col >= 0:
                    new_positions.append((row,col))
            except:
                pass #this simply prevents errors due to row or col out of range, it could be improved
                     #by adding flexible ranges in the scanning
    return new_positions


word_matrix = [
  ["B", "I", "T", "R"],
  ["I", "U", "A", "S"],
  ["S", "C", "V", "W"],
  ["D", "O", "N", "E"]
]
print(" " + str(["0","1","2","3"]))
for index in range(len(word_matrix)):
    print(str(index) + str(word_matrix[index]))

query = input("Insert the word you want to search in the word matrix:\n")
query = query.upper()

letter = query[0]
possible_starts = scan_letters(word_matrix, letter, query)
#the search begins only where there is the first query letter
possible_paths = []
for start in possible_starts:
    possible_paths.append([start])
correct_paths = []
for path in possible_paths:
    if len(path) == len(query):
        correct_paths.append(path) #saving the paths of the same length as the query (correct ones)
    else:
        new_positions = scan_around(word_matrix, path, query[len(path)]) #extending incomplete paths if possible
        for new in new_positions:
            new_path = list(path) #this is used to copy list to new memory address
            new_path.append(new)
            possible_paths.append(new_path) 
#print(possible_paths)
if len(correct_paths) != 0:
    print(f"The string {query} is located at {correct_paths}")
else:
    print(f"Could not find string {query} in word matrix")
