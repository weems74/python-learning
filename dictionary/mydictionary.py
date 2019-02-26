#first, load the json data into a dictionary

import json
data = json.load(open("data.json"))

def getDefinition (keyword):
	keyword = keyword.lower()
	if keyword in data:
		return data[keyword]
	else:
		return "This word is not in the dictionary. Please double check it."


# test ability to return keyword
keyword = input("Enter a word:")
print(getDefinition(keyword))
