import re
regex = r'([0-9] | [[1-9] [0-9]* | [0-7]+ | 0[xX][0-9a-fA-F]+)(i64 | I64 I u | U | l | L)?b'
def check(string):
     if(re.fullmatch(regex, string)):
        print("Valid integer constant")
    else:
        print("Invalid integer constant")
if __name__ == '__main__':
	string = “anything”
	check(string)
