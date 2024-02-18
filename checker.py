
import lester 

tokens= lester.tokens# no estoy segur o de donde salen los tokens jajajja?



def verify_program(tokens):
    def expect(tokens, expected):
        if tokens and tokens[0] == expected:
            tokens.pop(0)
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
            if not expect(tokens, "LPAREN"):
                return False
            if not expect(tokens, "CONDITION"):
                return False
            if not expect(tokens, "RPAREN"):
                return False
            if not expect(tokens, "THEN"):
                return False
            if not expect(tokens, "ACTION"):
                return False
        elif token == "LOOP":
            if not expect(tokens, "LPAREN"):
                return False
            if not expect(tokens, "CONDITION"):
                return False
            if not expect(tokens, "RPAREN"):
                return False
            if not expect(tokens, "DO"):
                return False
            if not expect(tokens, "ACTION"):
                return False
        else:
            return False
    return True
#pruebaaaa


