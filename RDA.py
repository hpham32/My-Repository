class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def match(self, expected):
        if self.current_token == expected:
            self.advance()
        else:
            raise ValueError(f"Expected {expected}, but got {self.current_token}")

    def parse(self):
        try:
            self.stmt_list()
            self.match(None)  # make sure we consumed all tokens
            return True
        except ValueError:
            return False

    def stmt_list(self):
        while self.current_token is not None:
            self.stmt()
            self.match(';')

    def stmt(self):
        if self.current_token == 'if':
            self.if_stmt()
        elif self.current_token == 'while':
            self.while_loop()
        else:
            self.expr()

    def if_stmt(self):
        self.match('if')
        self.match('(')
        self.bool_expr()
        self.match(')')
        self.stmt_or_block()
        if self.current_token == 'else':
            self.match('else')
            self.stmt_or_block()

    def while_loop(self):
        self.match('while')
        self.match('(')
        self.bool_expr()
        self.match(')')
        self.stmt_or_block()

    def stmt_or_block(self):
        if self.current_token == '{':
            self.block()
        else:
            self.stmt()
            self.match(';')
        if self.current_token == 'else':
            self.match('else')
            if self.current_token == '{':
                self.block()
            else:
                self.stmt()
                self.match(';')
        elif self.current_token == '}':
            self.match('}')

    def block(self):
        self.match('{')
        self.stmt_list()
        self.match('}')

    def expr(self):
        self.term()
        while self.current_token in {'+', '-', '*', '/', '%'}:
            self.match(self.current_token)
            self.term()

    def term(self):
        self.fact()
        while self.current_token in {'*', '/', '%'}:
            self.match(self.current_token)
            self.fact()

    def fact(self):
        if self.current_token == 'ID':
            if self.index + 1 < len(self.tokens) and self.tokens[self.index + 1] == '=':
                self.match('ID')
                self.match('=')
                self.expr()
            else:
                self.match('ID')
        elif self.current_token in {'INT_LIT', 'FLOAT_LIT'}:
            self.match(self.current_token)
        elif self.current_token == '(':
            self.match('(')
            self.expr()
            self.match(')')
        else:
            raise ValueError(f"Unexpected token: {self.current_token}")


    def bool_expr(self):
        self.bterm()
        while self.current_token in {'>', '<', '>=', '<=', '==', '!='}:
            self.match(self.current_token)
            self.bterm()

    def bterm(self):
        self.band()
        while self.current_token in {'==', '!='}:
            self.match(self.current_token)
            self.band()

    def band(self):
        self.bor()
        while self.current_token == '&&':
            self.match('&&')
            self.bor()

    def bor(self):
        self.expr()
        while self.current_token == '||':
            self.match('||')
            self.expr()


tokens = ['if', '(', 'ID', '>', 'INT_LIT', ')', '{', 'ID', '=', 'INT_LIT', ';', '}', 'else', '{', 'ID', '=', 'INT_LIT', ';', '}']
parser = Parser(tokens)
result = parser.parse()
print(result) # result should be false
