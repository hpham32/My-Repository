import re
regex = r'([+-]?[0-9]*.[0-9] | [0-9]+.)([eE][+-]?[0-9]+)?[LlFf]? | [+-]?[0-9]+[eE][+-]?[0-9]+[LlFf]?b'
def check(string):
     if(re.fullmatch(regex, string)):
        print("Valid Floating point")
    else:
        print("Invalid Floating point")
if __name__ == '__main__':
	string = "anything"
	check(string)

