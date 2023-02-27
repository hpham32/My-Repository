import re
regex = "/\\*(.*?)\\*/"
def check(string):
     if(re.fullmatch(regex, string)):
        print("Valid C++ Multiline comment")
     else:
        print("Invalid C++ Multiline comment")
if __name__ == '__main__':
	string = "/*dsadasd*/"
	check(string)