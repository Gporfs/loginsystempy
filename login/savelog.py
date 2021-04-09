import arquivos

def salvar(svduser, svdpwd):
    while True:
        try:
            arqsvd = 'saved.txt'
            if not arquivos.arquivoexiste(arqsvd):
                arquivos.criaraquivo(arqsvd)
            a = open(arqsvd, 'w')
            a.write(f'{svduser};{svdpwd}')
            a.close()
            
        except:
            print('Falhou :(')
        
        finally:
            break