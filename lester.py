import ply.lex as lex

#lista de tokens



tokens = [
    "DEFVAR", "NAME", "VAR", "MOVE", "SKIP", "TURND", "FACE0", "PUT", "PICK", "MOVEDIR", "RUNDIR",
    "NULL", "MOVEFACE", "DIM", "MYXPOS", "MYYPOS", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE",
    "SPACES", "IF", "LOOP", "REPEAT", "DEFUN", "FACING", "BLOCKED", "CANPUT", "CANPICK", "CANMOVE", "ISZERO",
    "NOT", "NOTCOND", "RUN", "DROP", "LEFT", "RIGHT", "DOWN", "UP", "NUMBER", "LPAREN", "RPAREN", "COLON",
]


#QUE ES ESTO XDDD
keywords = {
    'defvar': 'DEFVAR',
    'move': 'MOVE',
    'skip': 'SKIP',
    'turnd': 'TURND',
    'face0': 'FACE0',
    'put': 'PUT',
    'pick': 'PICK',
    'movedir': 'MOVEDIR',
    'rundir': 'RUNDIR',
    'null': 'NULL',
    'dim': 'DIM',
    'myxpos': 'MYXPOS',
    'myypos': 'MYYPOS',
    'mychips': 'MYCHIPS',
    'myballoons': 'MYBALLOONS',
    'balloonshere': 'BALLOONSHERE',
    'chipshere': 'CHIPSHERE',
    'if': 'IF',
    'loop': 'LOOP',
    'repeat': 'REPEAT',
    'defun': 'DEFUN',
    'facing': 'FACING',
    'blocked': 'BLOCKED',
    'canput': 'CANPUT',
    'canpick': 'CANPICK',
    'canmove': 'CANMOVE',
    'iszero': 'ISZERO',
    'not': 'NOT',
    'notcond': 'NOTCOND',
    'run': 'RUN',
    'drop': 'DROP',
    'left': 'LEFT',
    'right': 'RIGHT',
    'down': 'DOWN',
    'up': 'UP',
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

def t_NAME(t):
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
    r'balloonsHere:\s*\d+'
    
    t.value = int(t.value.split(":")[1].strip())  
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

#expresiones regulares tokens simples

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_ignore = ' \t'


#reconocer variables / numeros
def t_VAR(t):
    r'[a-zA-Z_$%^&()?+-:][a-zA-Z_0-9$%^&()?+-:]*'
    t.type = keywords.get(t.value, 'VAR')  # Verificar si es una palabra clave
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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
