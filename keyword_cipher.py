def remove_repeats(word) -> str: #this function removes repeated letters from a string returning the new string, keeping the order
	word = word.lower()
	new_word = ""
	for letter in word:
		if letter not in new_word:
			new_word = new_word + letter
	return new_word


def build_cipher(word) -> str: #this function returns the cipher alphabet obtained by joining the keyword and the missing alphabet letters
	cipher_alphabet = word + ""
	for letter in range(ord("a"),ord("z")):
		if chr(letter) not in word:
			cipher_alphabet = cipher_alphabet + chr(letter)
	return(cipher_alphabet)

def keyword_cipher(keyword, word) -> str: #this function returns the ciphred word as the word where each letter is replaced by the corresponding letter in the cipher alphabet 
	cipher_alphabet = build_cipher(remove_repeats(keyword))
	translated_word = ""
	word = word.lower()
	ord_a = ord("a")
	for letter in word:
		position = ord(letter) - ord_a
		translated_word = translated_word + cipher_alphabet[position]
	return(translated_word)
		

if __name__ == "__main__":
	print("TESTING:\n")
	print("Test 1")
	print(keyword_cipher("keyword", "abchij"))
	print("expected output: keyabc")

	print("\nTest 2")
	print(keyword_cipher("purplepineapple", "abc"))
	print("expected output: pur")

	print("\nTest 3")
	print(keyword_cipher("mubashir", "edabit"))
	print("expected output: samucq")

	print("\nTest 4")
	print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "abc"))
	print("expected output: eta")

	print("\nTest 5")
	print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "xyz"))
	print("expected output: qxz")

	print("\nTest 6")
	print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "aeiou"))
	print("expected output: eirfg")