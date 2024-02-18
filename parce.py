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

print(readFile("C:\\Users\\Juane\\OneDrive\\Escritorio\\lym\\p0\\prueba.txt")) # FUNCIONA



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
            #TODOjuan implementa las que faltan 
        elif token == "RUN":
            if not expect(tokens, "NAME"):
                return False
            if not expect_parentheses(tokens):
                return False
            if not expect(tokens, "DIRECTION"):
                return False
            if not expect(tokens, "DIRECTION"):
                return False
            #TODOSjuan implementa las que faltan 
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
        
  
        
        
        