import sys

f = open("postfix_entry.txt", "r")
w = open('psevdocod.txt', 'w')

def parser():
    lex=[]   
    str = f.readline()  
    
    if len(str) == 0:
        return 0   

    for a in str:       
        if a == '\n':
            break
        if a == " ":
            continue
        if a == "=":
            lex.append('=')
            break
            
        lex += a
                
    return lex


def lab():
    oper = {'+':'ADD','-':'SUB','*':'MIL','/':'DIV','~':'NOT'}
    stack = []
    k = 1
    while(1):
        str = parser()
        if str == 0:
            break
        f = len(str)
        k = 1
        for i in range(1,f):
            if (str[i].isalpha()):
                stack.append('LOAD \n')
            elif(str[i].isdigit()):                
                stack.append(f"LIT {str[i]} \n")
            elif str[i] in oper:
                stack.append(f"{oper[str[i]]} \n")
            elif str[i] == '=':
                stack.append(f"STO {str[0]} \n")
                k+=1

        for elem in stack:
            w.write(elem)

        print(stack)
        str = ""
        stack = []
lab()