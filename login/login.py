def entrar(user, pswd):
    ru = False
    rs = False

    with open('logs.txt', 'r') as f:
        lu = 1
        for text in f:
            if user == text.strip(): 
                ru = True
                break
            lu += 1

    with open('senhas.txt', 'r') as f:
        ls = 1
        for text in f:
            if pswd == text.strip(): 
                rs = True
                break
            ls += 1

    if ls == lu and rs and ru:
        return('Login APROVADO!')
    else:
        return("Os dados não conferem.")  

def saved():
    arqsvd = 'saved.txt'
    dado = ''
    try:
        a = open(arqsvd, 'r')
   
    except:
        a = open(arqsvd, 'wt+')
    else:
        for linha in a:
            dado = linha.split(';')
        print(dado)
    finally:
        a.close()
        return dado
        
