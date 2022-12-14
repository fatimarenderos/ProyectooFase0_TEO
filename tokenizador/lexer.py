from tokenizador.type import Type
from tokenizador.token import Token
import re

class LexicalError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def lex_source_file(fd):
    with open(fd, 'r') as file:
        data = file.read()
    return lex_source_string(data)


def lex_source_string(string):
    tokens = list()
    index = 0
    while index < len(string):
        token = separate_token(string, index)
        if token is None:
            break
        index = token.end
        tokens.append(token)
    return tokens


def separate_token(string, begin):
    if begin < 0 or begin >= len(string):
        raise IndexError(string, 'Index out of bounds: ' + begin)
    for type in Type:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, string, re.DOTALL)
        if match:
            end = match.end(1)
            if type == Type.T_STRING_LITERAL or type == Type.T_CHARACTER_LITERAL:
                end += 1
            return Token(begin, end, string[begin:end], type)
    else:
        return Token(begin, begin+1, string[begin:begin+1], Type.T_LEXICO_INCORRECTO)
    return None
