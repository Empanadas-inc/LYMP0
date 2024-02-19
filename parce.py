import ply.lex 
import lester as lex


def readFile(file_name:str):
    all_phrases=[]
    phrases=[]
    file= open(file_name,"r",encoding="utf-8")
    
    line=file.readline()
    
    
    while line !="":
        line =line.replace("\n","")
        line=line.lower()
        phrases.append(line)
        line= file.readline()
    file.close()
    
    i=0
    bool_parser=True
    
    while i <len(phrases) and bool_parser:
        tokened_phrase=lex.tokenFile(phrases[i])
        all_phrases.append(tokened_phrase)# extend
        i+=1
        
    return all_phrases    

#[[], ['LPAREN', 'DEFVAR', 'VAR', 'NUMBER', 'RPAREN'], 
# ['LPAREN', 'DEFVAR', 'VAR', 'VAR', 'RPAREN']]


"""
VERIFICADOR 

"""
     



"""


FUNCIONES AUXILIARES 


"""        


def parser_condition(tokens):
    ans = False
    if tokens[0] != 'LPAREN':
        ans
    
    if tokens[1].value == 'facing?' and tokens[2] == 'ORIENTATION' and tokens[3] == 'RPAREN':
        ans = True
     
    elif tokens[1].value == 'blocked?' and tokens[2] == 'RPAREN':
        ans = True
    
    elif tokens[1].value == 'can-put?' and tokens[2] == 'ITEM' and tokens[3] == 'NUMBER' and tokens[4] == 'RPAREN':
        ans = True 
    
    elif tokens[1].value == 'can-pick?' and tokens[2] == 'ITEM' and tokens[3] == 'NUMBER' and tokens[4] == 'RPAREN':
        ans =  True
    
    elif tokens[1].value == 'can-move?' and tokens[2] == 'ORIENTATION' and tokens[3] == 'RPAREN':
        ans = True
    
    elif tokens[1].value == 'isZero?' and tokens[2] == 'NUMBER' or tokens[2] == 'IDENTIFIER' and tokens[3] == 'RPAREN':
        ans = True
    
    elif tokens[1].value == 'not' and tokens[2] == 'CONDITION' and tokens[-1] == 'RPAREN':
        
        tokens_arg = tokens[2:-1]
        return parser_condition(tokens_arg)
    
    return False


        
def parser_blocks(tokens):
    if tokens[0] != 'LPAREN':
        return False
    
    type = tokens[1]
    
    parser_function = keywords.get(type)
    
    if parser_function:
        return parser_function(tokens)
    else:
        return False
    
    
"""


    keywords 

"""
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


#FUNCIONES PARCHADAS 

def parser_defvar(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
    print(tokens[0])
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "DEFPAR":
            tokens.pop(0)
            if tokens[0] == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0] == "NUMBER":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 


def parser_assign(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "ASSIGN":
            tokens.pop(0)
            if tokens[0] == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0] == "NUMBER":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 


#TODO esta seguramente esta mal (loop)

def parser_loop(tokens):
    ans =False 
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "LOOP":
            tokens.pop(0)
            if tokens[-1] == "RPAREN":
                ans = True
        ans
    tokens_arg = tokens[2:-1]
    tokens_1, index = parser_blocks(tokens_arg)
    
    if parser_condition(tokens_1) == True:
        tokens_2 =tokens[2+ index: -1]
        return parser_blocks(tokens_2)
    
    return ans

def parser_move(tokens):
    ans = False
    if len(tokens) != 4:
         ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "MOVE":
            tokens.pop(0)
            if tokens[0] == "NUMBER":
                tokens.pop(0)
                if tokens[0] == "RPAREN":
                    ans = True
    return ans 
 
        
def parser_skip(tokens):
    ans = False
    if len(tokens) != 4:
        ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "SKIP":
            tokens.pop(0)
            if tokens[0] == "NUMBER" or tokens[0] == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0] == "RPAREN":
                    ans = True
    return ans 

def parser_turn(tokens):
    ans = False
    if len(tokens) != 4:
        ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "TURN":
            tokens.pop(0)
            if tokens[0] == "DIRECTIONS":
                tokens.pop(0)
                if tokens[0] == "RPAREN":
                    ans = True
    return ans 

def parser_face(tokens):
    ans = False
    if len(tokens) != 4:
        ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "FACE":
            tokens.pop(0)
            if tokens[0] == "ORIENTATION":
                tokens.pop(0)
                if tokens[0] == "RPAREN":
                    ans = True
    return ans 

def parser_put(tokens):
    ans = False
    if len(tokens) != 5:
        ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "PUT":
            tokens.pop(0)
            if tokens[0] == "ITEM":
                tokens.pop(0)
                if tokens[0] == "NUMBER":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 

def parser_pick(tokens):
    ans = False
    if len(tokens) != 5:
        ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "PICK":
            tokens.pop(0)
            if tokens[0] == "ITEM":
                tokens.pop(0)
                if tokens[0] == "NUMBER":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 

def parser_loop(tokens):
    ret=False
    if True:
        pass
    
    
    
    
def parser_pick(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "PICK":
            tokens.pop(0)
            if tokens[0] == "ITEM":
                tokens.pop(0)
                if tokens[0] == "NUMBER":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 

def parser_move_dir(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "MOVE_DIR":
            tokens.pop(0)
            if tokens[0] == "NUMBER":
                tokens.pop(0)
                if tokens[0] == "DIRECTIONS":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 

#TODO FALTA 
def p_run_dirs(tokens):
    if len(tokens) < 4: 
        return False
    
def parser_move_face(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "MOVE_FACE":
            tokens.pop(0)
            if tokens[0]== "NUMBER" or tokens[0] == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0] == "ORIENTATION":
                    tokens.pop(0)
                    if tokens[0] == "RPAREN":
                        ans = True
    return ans 

def parser_null(tokens):
    ans = False
    if len(tokens) != 3:
        return ans
        
    if tokens[0] == "LPAREN":
        tokens.pop(0)
        if tokens[0] == "NULL":
            tokens.pop(0)
            if tokens[0] == "RPAREN":
                ans = True
    return ans 




def parce_program(tokens):
    result = False  
    for row in tokens:

        if len(row) > 2:  
            
            token_type = row[1]  

            print(parser_defvar(tokens))
            if token_type == "DEFVAR" and parser_defvar(tokens): 
                print("aquitoy")
                result = True
            if token_type == "ASSIGN" and parser_assign(tokens):
                result = True
            if token_type == "MOVE" and parser_move(tokens):
                result = True
            if token_type == "SKIP" and parser_skip(tokens):
                result = True
            if token_type == "TURN" and parser_turn(tokens):
                result = True
            if token_type == "FACE" and parser_face(tokens):
                result = True
            if token_type == "PUT" and parser_put(tokens):
                result = True
            if token_type == "PICK" and parser_pick(tokens):
                result = True
            if token_type == "LOOP" and parser_loop(tokens):
                pass

    return result
            
print(parce_program(readFile("C:\\Users\\ROG FLOW\\Desktop\\LYMP0\\pruebas.txt")))

            