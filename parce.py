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
        tokened
        all_phrases.appemd(tokened_phrase)# extend
        bool_parser = rules.general_analyzer(tokened_phrase)
        i+=1
        
    return bool_parser, all_phrases    
