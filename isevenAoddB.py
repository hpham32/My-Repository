import re
regex = "(b*ab*ab*)*((a*ba*ba*)*(a*ba*))(c | d)*|(cbadcbad)*"
def check(string):
     if(re.fullmatch(regex, string)):
        print("Valid evenAoddB")
     else:
        print("Invalid evenAoddB")
if __name__ == '__main__':
	string = "aab"
	check(string)