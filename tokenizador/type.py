from enum import Enum

class Type(Enum):
    T_PALABRA_RESERVADA = "\\b(fun|class|if|else|while|lateinit|const|println|return|null|do|println|import|main)\\b.*"
    T_MOD_ACCESO = "(?<![a-zA-Z\d._])(public|private|protected|internal)(?![a-zA-Z\d._])"
    T_VARIABLE_MUTABLE = "\\b(var)\\b.*"
    T_VARIABLE_INMUTABLE = "\\b(val)\\b.*"
    T_OPERADOR_LOGICO   =  "\\b(\|\||\&\&|(!(?!=)))\\b.*"
    T_OPERADOR_RELACIONAL = "(==|!=|>=|<=|<|>)"
    # Tipos de datos
    T_DOUBLE_CONSTANT = "\\b(\\d{1,9}\\.\\d{1,32})\\b.*"
    T_INT_CONSTANT = "\\b(\\d{1,9})\\b.*"
    T_INT = "\\b(Int)\\b.*"
    T_DOUBLE = "\\b(Double)\\b.*"
    T_BOOLEAN = "\\b(Boolean)\\b.*"
    T_STRDENNG = "\\b(String)\\b.*"
    T_CHAR = "\\b(Char)\\b.*"
    T_FLOAT = "\\b(Float)\\b.*"
    T_BYTE = "\\b(Byte)\\b.*"
    T_LONG = "\\b(Long)\\b.*"
    T_SHORT = "\\b(Short)\\b.*"
    # Identificadores
    T_IDENTIFICADOR = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"
    # Cadenas de texto
    T_STRING_LITERAL = '\"(\\.|[^\\"])*\"'
    T_CHARACTER_LITERAL = r"\'(\\.|[^\\'])\'"
    # Comentarios
    T_BLOCK_COMMENT = "(/\\*.*?\\*/).*"
    T_LINE_COMMENT = "(//(.*?)[\r$]?\n).*"

    T_PARENTESIS_ABRIR = "(\\().*"
    T_PARENTESIS_CERRAR = "(\\)).*"
    T_SEPARADOR = "(,).*"
    T_INICIO_BLOQUE = "(\\{).*"
    T_CIERRE_BLOQUE = "(\\}).*"
    T_CORCHETE_ABIERTO = "(\\[).*"
    T_CORCHETE_CERRADO = "(\\]).*"
    T_PUNTO = "(\\.).*"
    T_PUNTO_COMA = "(\\;).*"
    T_TIPO_EXPLICITO = "(:).*"
    # Operadores
    T_PLUS = "(\\+{1}).*"
    T_NOT_NULL = "(!!).*"
    T_MINUS = "(\\-{1}).*"
    T_MULTIPLY = "(\\*).*"
    T_DIVIDE = "(/).*"
    T_ASSIGNMENT = "(=).*"
    # Excepciones
    T_SPACE = "( ).*"
    T_NEW_LINE = "(\\n).*"
    T_TAB = "(\\t).*"
    # Lexico Incorrecto
    T_LEXICO_INCORRECTO = "(sdfgsd).*"
