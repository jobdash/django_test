punctuation = ('\'', '"', ',', '.', '?', '!')
word_cloud = {}

long_string = raw_input("Enter a string: ")
long_string = long_string.lower()


split_string = long_string.split()


for word in split_string:

	if word[0] in punctuation:  #checks for punctuation at the beginning of a word and removes it
		word = word[1: len(word)]

	if word[len(word) -1] in punctuation:  #checks for punctuation at the end of a word and removes it. Mostly for removing unnecessary punctuation 
		word = word[:len(word) - 1]

	if word in word_cloud.keys():
		word_cloud[word] += 1
	else:
		word_cloud[word] = 1

print word_cloud