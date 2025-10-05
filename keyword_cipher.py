def remove_repeats(word):
	word = word.lower()
	new_word = ""
	for letter in word:
		if letter not in new_word:
			new_word = new_word + letter
	return new_word


def build_cipher(word):
	cipher_alphabet = word + ""
	for letter in range(ord("a"),ord("z")):
		if chr(letter) not in word:
			cipher_alphabet = cipher_alphabet + chr(letter)
	return(cipher_alphabet)

def keyword_cipher(keyword, word):
	cipher_alphabet = build_cipher(remove_repeats(keyword))
	translated_word = ""
	word = word.lower()
	ord_a = ord("a")
	for letter in word:
		position = ord(letter) - ord_a
		translated_word = translated_word + cipher_alphabet[position]
	return(translated_word)
		

print(keyword_cipher("mubashir", "edabit"))