__author__ = 'Travis Nelson'

import re
from collections import Counter

mystr = 'After beating the eggs, Dana read the next step'
wordList = re.sub("[^\w]", " ", mystr).split()

print(Counter(wordList))