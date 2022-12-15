lexems = {"Var": "20", "Begin": "30", "End": "40", ";": "4", ",": "5", "+": "6", "-": "6", "*": "7", "/": "7", "(": "8",
        ")": "9", ":": "10", "=": "11", "~":"12"}


error = {0: "Такого символа не существует",
         1: "Отсутвует идент",
         2: "Пропущена запятая",
         3: "Отсутствует ;",
         4: "Отсутствует открывающая скобка (",
         5: "Отсутствует закрывающая скобка )",
         6: "Не хватает символа присваивания",
         7: "Отсутствует ключевое слово",
         8: "Нет пробела",
         9: "используется не обьявленный идентификатор"
         }
list_var = []
pos_un_oper = []

def A(str, file, n):
        if str[n['n']].split()[1] == "20":
            res.write(str[n['n']])
            n['n'] += 1
            while str[n['n']].split()[1] != "30":
                if (str[n['n']].split()[1] == "ident") or (miss_ident == True):

                    if (str[n['n']].split()[1] == "ident"):
                        list_var.append(str[n['n']].split()[0])
                    res.write(str[n['n']])
                    n['n'] += 1
                    if (str[n['n']].split()[1] == "5"): 
                        res.write(str[n['n']])
                        n['n'] += 1
                        miss_ident = False
                    elif str[n['n']].split()[1] == "30":
                        break
                    else:
                        print(f"ОШИБКА: __ {error[2]} ошибка на строке {str[n['n']].split()[2]} __")
                        res.write(str[n['n']])
                        n['n'] += 1
                else:
                    miss_ident = True
                    print(f"ОШИБКА: __ {error[1]} ошибка на строке {str[n['n']].split()[2]} __")
                    res.write(str[n['n']])
                    n['n'] += 1

                    if (str[n['n']].split()[1] == "5"): 
                        res.write(str[n['n']])
                        n['n'] += 1
                        miss_ident = False
                    elif str[n['n']].split()[0] == "Begin":
                        break
                    else:
                        print(f"ОШИБКА: __ {error[2]} ошибка на строке {str[n['n']].split()[2]} __")
                        res.write(str[n['n']])
                        n['n'] += 1

        else:
            print(f"ОШИБКА: __ {error[7]} - Var ошибка на строке {str[n['n']].split()[2]} __")
        
        print("список переменных :" , list_var)

        B(str, list_var, n) 
   
  
def B(str, list_var , n):
    if str[n['n']].split()[0] == "Begin":
        res.write(str[n['n']])
        n['n'] += 1
        while (str[n['n']].split()[1] != "13") and (str[n['n']].split()[1] != "40"):
            E(str, list_var, n)
            if (str[n['n']].split()[1] == "10"):
                print(f"ОШИБКА:__ {error[5]} на строке {str[n['n']].split()[2]}")
                res.write(str[n['n']])
                n['n'] += 1

        if (str[n['n']].split()[1] == "13") or (str[n['n']].split()[1] == "40"):
            print("To finish -B-")            

def E(str, list_var, n):
    if (str[n['n']].split()[1] == "ident") and (str[n['n']].split()[0] in list_var):
        res.write(str[n['n']])
        n['n'] += 1
        if str[n['n']].split()[1] == "12":
            res.write(str[n['n']])
            n['n'] += 1
            F(str, list_var, n)
        else:
            print(f"ОШИБКА: __ {error[6]}  - = - , ошибка на строке {str[n['n']].split()[2]}")
            miss_str(str, n)
    else:
        print(f"ОШИБКА:__ {error[9]} на строке {str[n['n']].split()[2]}")
        miss_str(str, n)


def miss_str(str, n):
    pos = str[n['n']].split()[2]
    while (str[n['n']].split()[2] == pos) and (str[n['n']].split()[1] != "40"):
        res.write(str[n['n']])
        n['n'] += 1

#+
def F(str, file, n):
    if str[n['n']].split()[1] == "14":
        pos_un_oper.append(n['n'])
        str[n['n']].split()[0] == "~"
        res.write(f"~ {str[n['n']].split()[1]} {str[n['n']].split()[2]}\n")
        n['n'] += 1
        G(str, file, n)
    else:
        G(str, file, n)
    
def G(str, file, n):
    if str[n['n']].split()[1] == "9":
        res.write(str[n['n']])
        n['n'] += 1
        F(str, file, n)
        if str[n['n']].split()[1] == "10":
            res.write(str[n['n']])
            n['n'] += 1
            if (str[n['n']].split()[1] == "6") or (str[n['n']].split()[1] == "7"):
                res.write(str[n['n']])
                n['n'] += 1
                F(str, file, n)
            elif (str[n['n']].split()[0] == "End"):
                res.write(str[n['n']])
                n['n'] += 1
        
        else:
            print(f"ОШИБКА:__ {error[5]} на строке {str[n['n']].split()[2]}")
            miss_str(str, n)




    elif str[n['n']].split()[1] == "ident":
        if (str[n['n']].split()[0] in list_var):
            res.write(str[n['n']])
            n['n'] += 1
            if (str[n['n']].split()[1] == "6") or (str[n['n']].split()[1] == "7"):
                res.write(str[n['n']])
                n['n'] += 1
                G(str, file, n)
            elif str[n['n']].split()[0] == "End":
                res.write(str[n['n']])
                n['n'] += 1
        elif (str[n['n']].split()[0] not in list_var):
            print(f"ОШИБКА: __ {error[6]}  - = - , ошибка на строке {str[n['n']].split()[2]}")
            miss_str(str, n)
       
    elif str[n['n']].split()[1] == "digit":
        res.write(str[n['n']])
        n['n'] += 1
        
        if (str[n['n']].split()[1] == "6") or (str[n['n']].split()[1] == "7"):
            res.write(str[n['n']])
            n['n'] += 1

            G(str, file, n)
        elif str[n['n']].split()[0] == "End":
            res.write(str[n['n']])
            n['n'] += 1
    
    else:
        print(f"Отсутсвует выражение после `=` ошибка на строке {str[n['n']].split()[2]}")

        print("Прошли выражение")
        

res = open('relust_syntactical_analizer.txt', 'w', encoding='utf-8')

with open('result_lexem.txt', 'r+', encoding='utf-8') as file:
    str = file.readlines()
    n = {'n' : 0}
    A(str, file, n)
    
res.close()