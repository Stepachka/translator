import sys

file_read = open('result_syntactical_analizer.txt', 'r')
w = open('postfix_entry.txt', 'w')
n = {'n' : 0}

str = file_read.readlines()



def parser(n):
    if str[n['n']].split()[1] == "40":
        return 0
    lex = []
    if n['n'] == 0:
        while str[n['n']].split()[1] != "30":
            n['n'] += 1
    if str[n['n']].split()[1] == "30":
        n['n'] += 1

    pos = str[n['n']].split()[2]
    while str[n['n']].split()[2] == pos:
        lex.append(str[n['n']].split()[0])
        n['n'] += 1
        
    return lex

def opz(lexems):
    #list_token = ['Var','Begin','End']
    dop_mas=[]
    digitIndent=[]
    oper=["+","-","*","/","(",")","~"]
    init=''
    Flag = 0
    
    for lexem in lexems:
        if lexem=="(":
            dop_mas=[lexem]+dop_mas
        elif lexem == '=':
            init +=lexem
        elif lexem in oper:
            if dop_mas==[]:
                dop_mas=[lexem]
            elif lexem==")":
                while(True):
                    q=dop_mas[0]
                    dop_mas=dop_mas[1:]
                    if q=="(":
                        break
                    digitIndent+=[q]
            elif prioritets(dop_mas[0]) < prioritets(lexem):
                dop_mas=[lexem]+dop_mas
            else:
                while(True):
                    if dop_mas==[]:
                        break
                    q=dop_mas[0]
                    digitIndent+=[q]
                    dop_mas=dop_mas[1:]
                    if prioritets(q)==prioritets(lexem):
                        break
                dop_mas=[lexem]+dop_mas
        else:
            if Flag == 1:                
                Flag = 0
            elif lexem == ',' or lexem == '\n' or lexem == ' ' or lexem == ';':
                continue
            digitIndent+=[lexem]

    dop_mas.append(init)
    while(dop_mas != []):        
        q=dop_mas[0]
        digitIndent+=[q]
        dop_mas=dop_mas[1:]
    
    
    return digitIndent
 
def prioritets(o):
    if o=="+" or o=="-" or o=="~":
        return 1
    elif o=="*" or o=="/":
        return 2
    elif o=="(":
        return 0    
                    
def main():
    
    while(True):
        lexems = parser(n)
        if lexems == 0:
            break
        g = opz(lexems)
        if g == "Exit":
            sys.exit()
        for i in range(len(g)):
            w.write(g[i]+" ")  
        w.write("\n")
        g.clear()
main()
sys.exit(1)
        
        

    





 

