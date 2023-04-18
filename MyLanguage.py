import re

# Define regular expressions for different token types
TOKEN_REGEX = [
    ("IF", r"if"),              # if keyword
    ("ELSE", r"else"),          # else keyword
    ("WHILE", r"while"),        # while keyword
    ("IDENTIFIER", r"(?!(if|else|while|True|False)\b)[a-zA-Z]+"),   # variable names
    ("BOOL", r"True|False"),    # boolean values
    ("OPERATOR", r"\+|\-|\*|\/|%|==|!=|=|>|<|<=|>="),   # arithmetic and comparison operators
    ("LOGICAL", r"and|or"),     # logical operators
    ("LPAREN", r"\("),          # left parentheses
    ("RPAREN", r"\)"),          # right parentheses
    ("NUMBER", r"\d+"),         # integer numbers
    ("SPACE", r"\s+"),          # whitespace
    ("COLON", r":"),            # colon symbol
]

# Combine all regex into a single pattern
PATTERN = "|".join("(?P<%s>%s)" % pair for pair in TOKEN_REGEX)

def lexer(file_path):
    """
    Split the contents of a file into a list of tokens using regular expressions.
    """
    with open(file_path, "r") as file:
        text = file.read()

    tokens = []
    for match in re.finditer(PATTERN, text):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type == "SPACE":
            continue
        tokens.append((token_type, token_value))
    return tokens


def parse(tokens):
    """
    Check if the given list of tokens matches the syntax of a simple subset of Python.
    Returns True if the syntax is correct, and False otherwise.
    """
    if len(tokens) == 0:
        return False

    # Check if the tokens are valid
    if tokens[0] not in ["IF", "WHILE", "IDENTIFIER"]:
        return False
    
    def checkID(i):
        if tokens[i+1] == "OPERATOR" and tokens[i+2] == "IDENTIFIER" or "NUMBER" or "BOOL":
            return True
        else:
            return False
            
    def checkBoolStm(i):
        if tokens[i] == "BOOL" or checkID(i) == True:
            return True
        else:
            return False


    def checkIf(i):
        if checkBoolStm(i+1) == True:
            return True
        else:
            return False

    def checkWhile(i):
        if checkBoolStm(i+1) == True:
            if tokens[i+2] == "COLON":
                return True
        else:
            return False
    
    def checkElse(i):
        if tokens[i+1] == "COLON":
            return True
        else:
            return False
    
    def checkColon(i):
        if tokens[i-1] == "IDENTIFIER" or "BOOL" or "NUMBER" or "ELSE":
            return True
        else:
            return False

    for i in range(len(tokens)):
        if tokens[i] == "IDENTIFIER":
            checkID(i)
        elif tokens[i] == "IF":
            checkIf(i)
        elif tokens[i] == "ELSE":
            checkElse(i)
        elif tokens[i] == "WHILE":
            checkWhile(i)
        elif tokens[i] == "COLON":
            checkColon(i)
        elif tokens[i] == "NUMBER" or "BOOL":
            return True
        else:
            return False


# driver code to test input
file_path = "test.txt"
tokens = lexer(file_path)

#prints tokens
for x in tokens:
    print(x)

typeTokens = [token[0] for token in tokens]

#checks if tokens is in language from parser
if parse(typeTokens) == True:
    print("Syntax is correct")
else:
    print("Syntax is incorrect")



