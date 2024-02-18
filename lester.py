import ply.lex as lex

#lista de tokens

tokens={
    
    "DEFVAR","NAME","VAR","MOVE","SKIP","TURND","FACE0","PUT","PICK","MOVEDIR","MOVE","RUNDIR","MOVEFACE",
    "NULL","MOVEFACE","DIM","MYXPOS","MYYPOS","MYCHIPS","MYBALLOONS","BALOONSHERE","CHIPSHERE",
    "SPACES","IF","LOOP","REPEAT","DEFUN","FACING","BLOCKED","CANPUT","CANPICK","CANMOVE","ISZERO",
    "NOT","NOTCOND","MOVE","RUN","DROP","LEFT","RIGHT","DOWN","UP"
}


#----Recognize cintrol structures-----#



#pruebas



#final pruebas 
def t_DEFVAR(t):
    r'defvar'
    return t

def t_MOVE(t):
    r'move'
    return t

def t_Name(t):
    r'name'
    return t

def t_SKIP(t):
    r'skip'
    return t

def t_TURND(t):
    r'turnd'
    return t

def t_FACE0(t):
    r'face0'
    return t

def t_PUT(t):
    r'put'
    return t

def t_PICK(t):
    r'pick'
    return t

def t_MOVEDIR(t):
    r'movedir'
    return t

def t_RUNDIR(t):
    r'front|right|left|back'
    return t

def t_MOVEFACE(t):
    r'moveface'
    return t

def t_NULL(t):
    r'null'
    return t

def t_DIM(t):
    r'dim'
    return t

def t_MYXPOS(t):
    r'myxpos'
    return t

def t_MYYPOS(t):
    r'myypos'
    return t

def t_MYCHIPS(t):
    r'mychips'
    return t

def t_MYBALLOONS(t):
    r'myballoons'
    return t

def t_BALLOONSHERE(t):
    r'balloonshere'
    return t

def t_CHIPSHERE(t):
    r'chipshere'
    return t

def t_IF(t):
    r'if'
    return t

def t_LOOP(t):
    r'loop'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_DEFUN(t):
    r'defun'
    return t

def t_FACING(t):
    r'facing'
    return t

def t_BLOCKED(t):
    r'blocked'
    return t

def t_CANPUT(t):
    r'canput'
    return t

def t_CANPICK(t):
    r'canpick'
    return t

def t_CANMOVE(t):
    r'canmove'
    return t

def t_ISZERO(t):
    r'iszero'
    return t

def t_NOT(t):
    r'not'
    return t

def t_NOTCOND(t):
    r'notcond'
    return t

def t_RUN(t):
    r'run'
    return t

def t_DROP(t):
    r'drop'
    return t

def t_LEFT(t):
    r'left'
    return t

def t_RIGHT(t):
    r'right'
    return t

def t_DOWN(t):
    r'down'
    return t

def t_UP(t):
    r'up'
    return t


#reconocer variables / numeros


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)




#crear lexer 

lexer = lex.lex()


def tokenFile(frase):
    tokens_line=[]
    
    lexer.input(frase)
    for t  in lexer:
        tokens_line.append(t.type)
        
    return tokens_line
        
        