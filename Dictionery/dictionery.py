import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(search):
    search = search.lower()
    
    if search in data:
        return data[search]
    elif len(get_close_matches(search,data.keys())) > 0:
        yn= input("did you mean %s, yes press 'y' if no press 'n': "  % get_close_matches(search,data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(search,data.keys())[0]]
        elif yn == 'n':
            return "word doesnt exist"
        else:
            return "press only 'y' on 'n'"
        
    else:
        return "word not exist"


word=str(input("please input any word : "))

output = translate(word)

if output == list:
    for item in output:
        print(item)
else:
    print(output)

