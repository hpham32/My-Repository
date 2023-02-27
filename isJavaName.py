import re
regex = "^[a-zA-Z_$][a-zA-Z_$0-9]*$"
def check(string):
     if(re.fullmatch(regex, string)):
        print("Valid java name")
     else:
        print("Invalid java name")
if __name__ == '__main__':
	string = "anything"
	check(string)