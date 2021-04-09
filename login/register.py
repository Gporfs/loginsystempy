import arquivos

def registrar(user, pwd):
    arqlog = 'logs.txt'
    arqsen = 'senhas.txt'
    if not arquivos.arquivoexiste(arqlog):
        arquivos.criaraquivo(arqlog)
        arquivos.criaraquivo(arqsen)
    n = user
    s = pwd
    arquivos.cadastrar(arqlog, n)
    arquivos.cadastrar(arqsen, s) 
