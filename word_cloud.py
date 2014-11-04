punctuation = ('\'', '"', ',', '.', '?', '!')
word_cloud = {}

long_string = raw_input("Enter a string: ")
long_string = long_string.lower()


split_string = long_string.split()


for word in split_string:
	word_check = word  #word_check looks for punctuation, we are free to change word

	if word_check[0] in punctuation:  #checks for punctuation at the beginning of a word and removes it
		word_check = word_check[1: len(word_check)]

	if word_check[len(word_check) -1] in punctuation:  #checks for punctuation at the end of a word and removes it
		word_check = word_check[:len(word_check) - 1]

	if word_check in word_cloud.keys():
		word_cloud[word_check] += 1
	else:
		word_cloud[word_check] = 1

print word_cloud