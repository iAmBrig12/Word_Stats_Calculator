################################################################################ 
#
#       AUTHOR: 
#           Brigham Thornock 
#  DESCRIPTION: 
#           Reads in a text file, removes html tags and formatting codes,
#           normalizes text to lowercase, tokenizes the text, calculates 
#           word counts and frequencies, and displays calculations.
#
#           Adapted from Human Language Technologies Homework Assignment
# DEPENDENCIES: 
#           Created with Python 3.11.5 
#           re, collections
# 
################################################################################

import re
import collections

# read in file
f = open('text_news.txt', 'r')
corpus = f.read()
f.close()

# Normalize the text to all lowercase
corpus = corpus.lower()

# Remove any html tags or formatting codes
corpus = re.sub('<.*?>', '', corpus)
corpus = re.sub('@@\d{7}', '', corpus)
corpus = corpus.replace('@', '')
corpus = corpus.strip()

# Word tokenize the text
tokens = re.split('\W+', corpus)

# Calculate the word count and frequency percentage of each word/unigram
# For the top 20 most frequent words / unigrams, on each line display/print 
# the word form (lexeme), its count (integer number of instances in the text), 
# and frequency (float to exactly five decimal places). 
counter = collections.Counter(tokens)

counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print(f'   lexeme'.ljust(13) + f'count'.ljust(10) + f'frequency'.ljust(9))
i = 1
for w in counter[:20]:
    print(f'\n{i}'.ljust(4) + f'{w[0]}'.ljust(10) + f'{w[1]}'.ljust(10) + f'{w[1]/len(corpus):.5f}'.ljust(10))
    i += 1
