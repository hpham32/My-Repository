import re

# Define regular expression patterns for each token
patterns = {
    'ADD': r'\+',
    'SUB': r'-',
    'MUL': r'\*',
    'DIV': r'/',
    'MOD': r'%',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'ASSIGN': r'=',
    'EQUAL': r'==',
    'LESS_THAN': r'<',
    'LESS_THAN_EQUAL': r'<=',
    'GREATER_THAN': r'>',
    'GREATER_THAN_EQUAL': r'>=',
    'LOGICAL_AND': r'&&',
    'LOGICAL_OR': r'\|\|',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'INTEGER_LITERAL': r'\d+',
    'FLOAT_LITERAL': r'\d*\.\d+',
}

# Combine all patterns into a single regular expression with named capture groups
token_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns.items()))

def lexer(filename):
    with open(filename, 'r') as file:
        input_string = file.read()
    tokens = []
    for match in token_regex.finditer(input_string):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))
    return tokens


filename = 'input.txt'

tokens = lexer(filename)
print(tokens)
