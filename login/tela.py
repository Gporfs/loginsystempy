from windows import jlogin, janela2, jregist
from login import entrar, saved
from PySimpleGUI import PySimpleGUI as sg
from register import registrar
import arquivos
from savelog import salvar

#teste de usuario salvo
dado = saved()

#janela ao iniciar
try:
    jl, jres, jreg  = jlogin(dado[0],dado[1]), None, None
except:
    jl, jres, jreg  = jlogin(), None, None

#teste de existência dos arquivo
arqlog = 'logs.txt'
arqsen = 'senhas.txt'
if not arquivos.arquivoexiste(arqlog):
    arquivos.criaraquivo(arqlog)
    arquivos.criaraquivo(arqsen)

#Loop de eventos
while True:
    
    win, events, values = sg.read_all_windows()
  
    if win == jl  and events == sg.WINDOW_CLOSED:
        break
    if win == jres and events == 'Fechar':
        break
    if win == jres  and events == sg.WINDOW_CLOSED:
        break
    if win == jl and events == 'Entrar':
       jres = janela2(entrar(values['usuario'], values['senha']))
       jl.close()      
    if win == jres and events == 'Voltar':
        jres.close()
        try:
            jl, jres, jreg  = jlogin(dado[0],dado[1]), None, None
        except:
            jl, jres, jreg  = jlogin(), None, None
    if win == jl and events == 'Cadastrar':
        jl.close()
        jreg = jregist()
    if win == jreg and events == sg.WINDOW_CLOSED:
        break
    if win == jreg and events == "Cadastrar":
        jreg.close()
        try:
            jl, jres, jreg  = jlogin(dado[0],dado[1]), None, None
        except:
            jl, jres, jreg  = jlogin(), None, None
        registrar(values['user'], values['pwd'])
    if win == jreg and events == "Voltar":
        jreg.close()
        try:
            jl, jres, jreg  = jlogin(dado[0],dado[1]), None, None
        except:
            jl, jres, jreg  = jlogin(), None, None 
    if win == jl and values['save'] == True and events == 'Entrar':
        salvar(values['usuario'], values['senha'])
        jres = janela2(entrar(values['usuario'], values['senha']))
        jl.close()
    if win == jl and values['mostrar'] == True and events == 'reload':
        jl.close()
        try:
            jl = jlogin(dado[0],dado[1], True)
        except:
            jl = jlogin(m = True)
    if win == jreg and values['mostrar'] == True and events =='reload':
        jreg.close()
        jreg = jregist(m=True)
    if win == jl and values['mostrar'] == False and events=='reload':
            jl.close()
            try:
                jl = jlogin(dado[0],dado[1], False)
            except:
                jl = jlogin(m = False)
    if win == jreg and values['mostrar'] == False and events=='reload':
        jreg.close()
        jreg = jregist(m=False)
