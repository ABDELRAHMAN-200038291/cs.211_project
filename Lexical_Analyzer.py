import re 

keyWords = ["int","float","if","else","while","for","char","return"]

def is_keyword(token):
    return token in keyWords

def is_identifier(token):
    return re.match(r'[a-z.A-z_]\w*$',token)

def is_integer(token):
    return re.match(r'^\d+$', token)

def is_float(token):
    return re.match(r'^\d+\.\d+$', token)

def is_operator (token):
    return token in ["+","-","*","/","!=","<",">","<=",">=","==","=","++","--","**"]

def is_punctuation (token):
    return token in ["," , ";" ,"(" ,")","{","}","[","]"]


operator_tokens = {"+": "plus_operator",
    "-": "sub_operator",
    "*": "Multiply_operator",
    "/": "Division_operator",
    "!=": "not_equal_operator",
    ">": "greater_than_operator",
    "<": "less_than_operator",
    "<=": "LE_comparison",
    ">=": "GE_comparison",
    "=": "assignment_operator",
    "==": "equal_operator",
    "++": "increment_operator",
    "--": "decrement_operator",
    "**": "exp_operator"}


punctuation_tokens = {
    ",": "Comma",
    ";": "Semicolon",
    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE",
    "}": "RBRACE",
    "[": "LBracket",
    "]": "RBracket"
}


keyWords_tokens = {
    "for":"for",
    "while" : "while",
    "if" : "if",
    "return":"return",
    "char" :  "reserved_word",
    "else" : "else",
    "float" : "reserved_word",
    "int" : "reserved_word",
}



def LexicalAnalyzer(code):
    tokens = re.findall(r'\w+\.\w+|\w+|==|!=|<=|>=|\+\+|--|\*\*|[=+\-*/<>{}();,\[\]]', code)
    
    for token in tokens:
        if is_keyword(token):
            print(f"{token} => {keyWords_tokens[token]}")

        elif is_integer(token):
            print(f"{token} => int_literal")

        elif is_float(token):
            print(f"{token} => float_literal")

        elif is_operator(token):
            print(f"{token} => {operator_tokens[token]}")

        elif is_punctuation(token):
            print(f"{token} => {punctuation_tokens[token]}")

        elif is_identifier(token):
            print(f"{token} => identifier")

        else:
            print(f"{token} => UNKNOWN")

code = "result = old_sum - value / 100;"

LexicalAnalyzer(code)

print("                             ")



print ("Made by Abdulrahmn mohamed")
print ("iD: 200038291")
