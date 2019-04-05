# Basic CLI dictionary application

#first, load the json data into a dictionary
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def getDefinition (keyword):

	# Account for case in intput
	if keyword.istitle() == "False":
		keyword = keyword.lower()
	elif keyword in data:
		return data[keyword]
	#check to see if you can make a fuzzy match of the term
	elif len( get_close_matches(keyword, data.keys(),cutoff=0.8)) > 0:
		response = input ("That word is not in the dictionary. Did you mean: %s? Enter Y for yes:" % get_close_matches(keyword, data.keys(),cutoff=0.8)[0])
		if response.upper() == "Y":
			return data[get_close_matches(keyword,data.keys(),cutoff=0.8)[0]]
		else:
			return "The word is not in the dictionary. Please double check it."
	else:
		return "This word is not in the dictionary. Please double check it."


# Take input and return definition for entered term
keyword = input("Enter a word:")
defs = getDefinition(keyword)

# if you get a valid response from the dictionary, it will be a list, so print out the enumerated definitions
if type(defs) == list:
	x=1
	for definition in defs:
		print ("{} : {}".format(str(x),definition))
		x+=1
# if you get a string (error messages) then just output the string.
else:
	print(defs)