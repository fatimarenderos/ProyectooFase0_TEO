from tokenizador.lexer import lex_source_file
from tokenizador.type import Type

tokens = lex_source_file('./Prueba.kt')
print("=============================================")
print("|               PROYECTO FASE 0             |")
print("=============================================")
print("|                TOKENIZADOR                |")
print("=============================================")
print("|    LEXEMA     |            TOKEN          |")
print("---------------------------------------------")
for token in tokens: 
    if token.type not in [Type.T_SPACE, Type.T_NEW_LINE, Type.T_LINE_COMMENT, Type.T_BLOCK_COMMENT]:
        print(token)


