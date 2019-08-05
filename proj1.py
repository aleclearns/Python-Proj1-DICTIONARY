import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print("*********************\nDICTIONARY\n********************* \nto end type stop() or exit() ")
x = 0
while x < 1:
    user_input = str(input("Search >>>"))

    if user_input.lower() == "stop()" or user_input.lower() == "exit()":
        x = x+1
        print("***END")
    elif user_input.title() in data:
        print("***Upon searching in the database, the word you typed returned: \n{}".format(data[user_input.title()]))
        break
    elif user_input.upper() in data:
        print("***Upon searching in the database, the word you typed returned: \n{}".format(data[user_input.upper()]))
        break
    elif user_input.lower() not in data:
        print("***Not in database, did you mean...{} ".format(get_close_matches(user_input.lower(),data.keys())[0:3]))
    else:
        print("***Upon searching in the database, the word you typed returned: \n{}".format(data[user_input.lower()]))
