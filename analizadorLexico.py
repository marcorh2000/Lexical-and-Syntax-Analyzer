from re import T
import ply.lex as lex
import sys

#Lista de tokens
tokens = ['id', 'fibo', 'd', 'suma', 'resta' , 'if', 'else', 'PARIZQ', 'PARDER' , 'LLAIZQ' , 'LLADER', 'PUNTOCOMA', 'ASIGNAR', 'return', 'int' ,'newline', 'BARRAVER']

#Definicion de tokens
def t_suma(t):
    r'\+'
    return t

def t_int(t):
    r'int'
    return t

def t_if(t):
    r'if'
    return t

def t_else(t):
    r'else'
    return t

def t_resta(t):
    r'\-'
    return t

def t_fibo(t):
    r'fibo'
    return t

def t_PARIZQ(t):
    r'\('
    return t

def t_PARDER(t):
    r'\)'
    return t

def t_LLAIZQ(t):
    r'\{'
    return t

def t_LLADER(t):
    r'\}'
    return t

def t_ASIGNAR(t):
    r'\='
    return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_d(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_return(t):
    r'return'
    return t

def t_id(t):
    r'\w+(_\d\w)*'
    return t

def t_error(t):
    print("Caracter invalido: " + t.value)
    t.lexer.skip(1)

t_ignore  = ' \t'
t_PUNTOCOMA = ';'
t_BARRAVER = r"\|"

#Diccionario de tokens
diccionario_tokens = {'id':'id', 'fibo':'fibo', 'd':'d', 'suma':'+', 'resta':'-', 'if': 'if', 'else':'else', 'PARIZQ':
'(', 'PARDER':')' , 'LLAIZQ':'{' , 'LLADER':'}', 'PUNTOCOMA':';', 'ASIGNAR':'=', 'return':'return', 'int':'int','newline':'newline', 'BARRAVER':'l'}

#Leemos el codigo
resultado = ""
pal_sinta = ""
valor_dic = ""
codigo = open("codigo.txt")
analizador = lex.lex()

with codigo as fp:
    for linea in fp:
        try:
            analizador.input(linea)
            for token in analizador:
                resultado += "" + str(token.type) + " "

                #Cambiamos cada token por su signo
                valor_dic = diccionario_tokens.get(token.type)
                pal_sinta += "" + str(valor_dic) + " "

        except EOFError:
            break

#Este archivo es con los tokens que dio
file = open("Code-tokens.txt", "w")
file.write(resultado)
file.close()

#Este otro es para que se pueda meter al analizador sintactico
file = open("Code-tokens-sin.txt","w")
file.write(pal_sinta)
file.close()