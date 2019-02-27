#first, load the json data into a dictionary

import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def getDefinition (keyword):

	# Account for case in intput
	keyword = keyword.lower()
	if keyword in data:
		return data[keyword]
	#check to see if you can make a fuzzy match of the term
	elif len( get_close_matches(keyword, data.keys(),cutoff=0.8)) > 0:
		return "That word is not in the dictionary. Did you mean: %s?" % get_close_matches(keyword, data.keys(),cutoff=0.8)[0]
	else:
		return "This word is not in the dictionary. Please double check it."


# Take input and return definition for entered term
keyword = input("Enter a word:")
print(getDefinition(keyword))
