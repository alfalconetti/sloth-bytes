keyboard_letters = {
	2: "abc",
	3: "def",
	4: "ghi",
	5: "jkl",
	6: "mno",
	7: "pqrs",
	8: "tuv",
	9: "wxyz"
}

def recursive_combination(strings_list,key) -> list: # This function creates a new list with the new combinations created with the next key 
	key = int(key)
	new_strings_list = []
	for letters in keyboard_letters[key]:
		for string in strings_list:
			new_strings_list.append(string + letters)
	return new_strings_list



def letter_combinations(num_keys: int) -> list: # Main function 
	# User input curation
	if len(num_keys) == 0:
		return []
	try:
		for key in num_keys:
			if int(key) not in list(range(2,10)):
				raise Exception("Your input contains a number not in range 2-9") 
	except:
		return "Your input must only contain numbers"

	strings_list = []
	for letter in keyboard_letters[int(num_keys[0])]:
		strings_list.append(letter)
	for key in num_keys[1:]:
		strings_list = recursive_combination(strings_list, key)
	strings_list.sort()
	return strings_list

def check_combinations_number(num_keys, strings_list): #this function checks if the number of created combinations is equal to the predicted one 
	if len(num_keys) == 0:
		number_combinations = 0
	else: 
		number_combinations = 1
		for key in num_keys:
			number_combinations *= len(keyboard_letters[int(key)])
	is_combinations_number_correct = number_combinations == len(strings_list)
	return is_combinations_number_correct


if __name__ == "__main__":
	print("TESTING:\n")
	print("Test 1")
	print(letter_combinations("23"))
	print('expected output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]')
	print(f"The number of combinations is {"Correct" if check_combinations_number("23",letter_combinations("23")) else "Incorrect"}")
	
	print("\nTest 2")
	print(letter_combinations(""))
	print('expected output: []')
	print(f"The number of combinations is {"Correct" if check_combinations_number("",letter_combinations("")) else "Incorrect"}")

	print("\nTest 3")
	print(letter_combinations("2"))
	print('expected output: ["a","b","c"]')
	print(f"The number of combinations is {"Correct" if check_combinations_number("",letter_combinations("")) else "Incorrect"}")

	print("\nTest 4")
	print(letter_combinations("27"))
	print('expected output: ["ap","aq","ar","as","bp","bq","br","bs","cp","cq","cr","cs"]')
	print(f"The number of combinations is {"Correct" if check_combinations_number("",letter_combinations("")) else "Incorrect"}")

	print("\nTest 5")
	print(letter_combinations("234"))
	print('''expected output: [
    "adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
    "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
    "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"
]''')
	print(f"The number of combinations is {"Correct" if check_combinations_number("",letter_combinations("")) else "Incorrect"}")

	print("\nTest 6")
	print(letter_combinations("79"))
	print('expected output: [ "pw","px","py","pz","qw","qx","qy","qz", "rw","rx","ry","rz", "sw","sx","sy","sz"]')
	print(f"The number of combinations is {"Correct" if check_combinations_number("",letter_combinations("")) else "Incorrect"}")

	
