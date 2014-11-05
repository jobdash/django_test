import sys
def wordcloud(filepath):
	#file=open(sys.argv[0],"r+")
	text = 'dana ate the cookie in the cookie jar'
	wordcloud={}
	#with open(filepath, 'r') as text:
	for word in text.split():
	    if word in wordcloud:
	      wordcloud[word] += 1
	    else:
	      wordcloud[word] = 1
	for key in wordcloud.keys():
	 	print ("%s %s" %(key , wordcloud[key]))
	#file.close();



