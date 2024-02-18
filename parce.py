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

print(readFile("C:\Users\ROG FLOW\Desktop\p1 lym\preubas.txt")) 
#TODO realmente no se si esto funciona se que el retorno tiene que ser una lista de otkens por linea
#porfa resuelvelo tambine 


"""
def verify_program(tokens):
    def expect(tokens, expected):
        if tokens and tokens[0] == expected:
            tokens.pop(0)
            return True
        return False

    def expect_parentheses(tokens):
        if not tokens:
            return False
        if tokens[0] == "LPAREN":
            tokens.pop(0)
            if not expect(tokens, "CONDITION"):
                return False
            if not expect(tokens, "RPAREN"):
                return False
            return True
        return False

    while tokens:
        token = tokens.pop(0)
        if token == "DEFVAR":
            if not tokens:
                return False
            if tokens.pop(0) != "NAME":
                return False
            if not tokens or tokens.pop(0) not in ["NUMBER", "STRING"]:
                return False
        elif token == "IF":
            if not expect_parentheses(tokens):
                return False
            if not expect(tokens, "THEN"):
                return False
            if not expect_parentheses(tokens):
                return False
        elif token == "LOOP":
            if not expect_parentheses(tokens):
                return False
            if not expect(tokens, "DO"):
                return False
            if not expect_parentheses(tokens):
                return False
        elif token == "DEFUN":
            if not expect(tokens, "NAME"):
                return False
            if not expect_parentheses(tokens):
                return False
            if not expect(tokens, "PARAM"):
                return False
            if not expect(tokens, "PARAM"):
                return False
            
        elif token == "RUN":
            if not expect(tokens, "NAME"):
                return False
            if not expect_parentheses(tokens):
                return False
            if not expect(tokens, "DIRECTION"):
                return False
            if not expect(tokens, "DIRECTION"):
                return False
            
        else:
            return False
    return True




def Hayparentesis(tokens):
    if tokens and (tokens[0] == "RPAREN" or tokens[0] == "LPAREN"):
        tokens.pop(0)
        if tokens and (tokens[0] == "DEFVAR" or tokens[0] == "IF"):
            tokens.pop(0)
            if tokens and (tokens[0] == "NOT" or tokens[0] == "null"):
                tokens.pop(0)
                if tokens and (tokens[0] == "DEFUN" or tokens[0] == "PUT"):
                    Hayparentesis(tokens)
    else:
        return False
        
  
        """
#fuck this shit

def parce_program(tokens:list):
    #TODO si la condición retorna falso tambien las otras condiciones retornan falso,
    #Falta remplazarlo porfaaaa, esta implementación funcionara siempre y cuando el lester sea una stack

    for token in tokens:
        if token[1].type == "DEFVAR" and not ("aca va la función del token"):
            return False 
        if token[1].type == "ASSIGN" and not ("aca va la función del token"):
            return False 
        if token[1].type == "MOVE" and not ("aca va la función del token"):
            return False 
        if token[1].type == "SKIP" and not ("aca va la función del token"):
            return False 
        if token[1].type == "TURN" and not ("aca va la función del token"):
            return False 
        if token[1].type == "FACE" and not ("aca va la función del token"):
            return False 
        if token[1].type == "PUT" and not ("aca va la función del token"):
            return False 
        if token[1].type == "PICK" and not ("aca va la función del token"):
            return False 
        if token[1].type == "MOVE_DIR" and not ("aca va la función del token"):
            return False 
        if token[1].type == "RUNS_DIRS" and not ("aca va la función del token"):
            return False 
        if token[1].type == "MOVE_FACE" and not ("aca va la función del token"):
            return False 
        if token[1].type == "NULL" and not ("aca va la función del token"):
            return False 
        if token[1].type == "REPEAT" and not ("aca va la función del token"):
            return False 
        if token[1].type == "DEFVAR" and not ("aca va la función del token"):
            return False 
        
        
        
        
        
        
"""


FUNCIONES AUXILIARES 


"""        


def parser_condition(tokens):
    ans = False
    if tokens[0].type != 'LPAREN':
        ans
    
    if tokens[1].value == 'facing?' and tokens[2].type == 'ORIENTATION' and tokens[3].type == 'RPAREN':
        ans = True
     
    elif tokens[1].value == 'blocked?' and tokens[2].type == 'RPAREN':
        ans = True
    
    elif tokens[1].value == 'can-put?' and tokens[2].type == 'ITEM' and tokens[3].type == 'NUMBER'and tokens[4].type == 'RPAREN':
        ans = True 
    
    elif tokens[1].value == 'can-pick?'and tokens[2].type == 'ITEM' and tokens[3].type == 'NUMBER' and tokens[4].type == 'RPAREN':
        ans =  True
    
    elif tokens[1].value == 'can-move?' and tokens[2].type == 'ORIENTATION'and tokens[3].type == 'RPAREN':
        ans = True
    
    elif tokens[1].value == 'isZero?' and tokens[2].type == 'NUMBER' or tokens[2].type == 'IDENTIFIER' and tokens[3].type == 'RPAREN':
        ans = True
    
    elif tokens[1].value == 'not'and tokens[2].type == 'CONDITION' and tokens[-1].type == 'RPAREN':
        
        tokens_arg = tokens[2:-1]
        return parser_condition(tokens_arg)
    
    return False
        
def parser_blocks(tokens):
    if tokens[0].type != 'LPAREN':
        return False
    
    type = tokens[1].type
    
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
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "DEFPAR":
            tokens.pop(0)
            if tokens[0].type == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0].type == "NUMBER":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
                        ans = True
    return ans 


def parser_assign(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "ASSIGN":
            tokens.pop(0)
            if tokens[0].type == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0].type == "NUMBER":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
                        ans = True
    return ans 


#TODO esta seguramente esta mal (loop)

def parser_loop(tokens):
    ans =False 
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "LOOP":
            tokens.pop(0)
            if tokens[-1].type == "RPAREN":
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
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "MOVE":
            tokens.pop(0)
            if tokens[0].type == "NUMBER":
                tokens.pop(0)
                if tokens[0].type == "RPAREN":
                    ans = True
    return ans 
 
        
def parser_skip(tokens):
    ans = False
    if len(tokens) != 4:
        ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "SKIP":
            tokens.pop(0)
            if tokens[0].type == "NUMBER" or tokens[0].type == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0].type == "RPAREN":
                    ans = True
    return ans 

def parser_turn(tokens):
    ans = False
    if len(tokens) != 4:
        ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "TURN":
            tokens.pop(0)
            if tokens[0].type == "DIRECTIONS":
                tokens.pop(0)
                if tokens[0].type == "RPAREN":
                    ans = True
    return ans 

def parser_face(tokens):
    ans = False
    if len(tokens) != 4:
        ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "FACE":
            tokens.pop(0)
            if tokens[0].type == "ORIENTATION":
                tokens.pop(0)
                if tokens[0].type == "RPAREN":
                    ans = True
    return ans 

def parser_put(tokens):
    ans = False
    if len(tokens) != 5:
        ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "PUT":
            tokens.pop(0)
            if tokens[0].type == "ITEM":
                tokens.pop(0)
                if tokens[0].type == "NUMBER":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
                        ans = True
    return ans 

def parser_pick(tokens):
    ans = False
    if len(tokens) != 5:
        ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "PICK":
            tokens.pop(0)
            if tokens[0].type == "ITEM":
                tokens.pop(0)
                if tokens[0].type == "NUMBER":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
                        ans = True
    return ans 

def parser_pick(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "PICK":
            tokens.pop(0)
            if tokens[0].type == "ITEM":
                tokens.pop(0)
                if tokens[0].type == "NUMBER":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
                        ans = True
    return ans 

def parser_move_dir(tokens):
    ans = False
    if len(tokens) != 5:
        return ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "MOVE_DIR":
            tokens.pop(0)
            if tokens[0].type == "NUMBER":
                tokens.pop(0)
                if tokens[0].type == "DIRECTIONS":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
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
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "MOVE_FACE":
            tokens.pop(0)
            if tokens[0].type == "NUMBER" or tokens[0].type == "IDENTIFIER":
                tokens.pop(0)
                if tokens[0].type == "ORIENTATION":
                    tokens.pop(0)
                    if tokens[0].type == "RPAREN":
                        ans = True
    return ans 

def parser_null(tokens):
    ans = False
    if len(tokens) != 3:
        return ans
        
    if tokens[0].type == "LPAREN":
        tokens.pop(0)
        if tokens[0].type == "NULL":
            tokens.pop(0)
            if tokens[0].type == "RPAREN":
                ans = True
    return ans 