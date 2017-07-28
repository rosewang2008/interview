def change(phrase, length):
	''' Method that changes all single spaces into '%20'
	Also given: length of string
	'''
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	phrase[::-1]
	start = 0
	next(letter for letter in phrase if letter in alphabet)

	new_phrase = ''
	for letter in range(start, len(phrase)):
		if phrase[letter] in alphabet:
			new_phrase += new_phrase[letter]
		elif phrase[letter] == ' ':
			new_phrase += '02%'

	return new_phrase[::-1]
		 
print(change('Mr John Smith        ', 10))
