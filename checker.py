
import lester 

tokens= lester.tokens# no estoy segur o de donde salen los tokens jajajja?



def verify_instruction(tokens):
    
    if not tokens:
        return True  #
    
    token = tokens.pop(0)  
    
    if token == "DEFVAR":
        #
        if tokens and tokens[0] == "NAME":
            tokens.pop(0)  
            if tokens and tokens[0] == "VAR":
                tokens.pop(0)  
                return verify_instruction(tokens)  
            else:
                return False  
        else:
            return False 
    
    elif token == "IF":
        
        return verify_instruction(tokens)  
    
    elif token == "LOOP":
        
        return verify_instruction(tokens) 
    
    else:
        
        return False
    
#pruebaaaa

tokens_example = ["DEFVAR", "NAME", "VAR", "IF", "LOOP"]
print(verify_instruction(tokens_example))
