import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print(f"Did you mean {get_close_matches(word , data.keys())[0]} ")
        decide = input("Press y for yes and n for no ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return "You have entered the wrong spelling please check again"
        else:
            return "You entered the worng choice"
    else:
        return "You have entered the wrong word please check again"


op = ""
while(op != "q"):
    word = input("Enter the word you wat to search ")
    output = find_meaning(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    op = input("Press q to exit ")