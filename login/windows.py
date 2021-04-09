from PySimpleGUI import PySimpleGUI as sg 
from login import saved
# Layout

def jlogin(user='usuário',pwd = 'senha', m = False):
    sg.theme("Reddit")
    if m == False:
        layout = [
            [sg.Text('Usuário'), sg.Input(user,key= 'usuario')],
            [sg.Text("Senha"), sg.Input(pwd, key= 'senha', password_char='*')],
            [sg.Checkbox('Salvar login?', key='save'), sg.Checkbox('Mostrar senha', key='mostrar')],
            [sg.Button('Cadastrar'), sg.Button('Entrar')],
            [sg.Button("reload", key='reload')]
        ]     
    else:
        layout = [
            [sg.Text('Usuário'), sg.Input(user,key= 'usuario')],
            [sg.Text("Senha"), sg.Input(pwd, key= 'senha')],
            [sg.Checkbox('Salvar login?', key='save'), sg.Checkbox('Mostrar senha', key='mostrar')],
            [sg.Button('Cadastrar'), sg.Button('Entrar')],
            [sg.Button("reload", key='reload')]
        ]
    return sg.Window('Login',layout= layout, finalize = True)
        

def jregist(m = False):
    sg.theme("Reddit")
    if m == False:
        layout = [
            [sg.Text("Registre-se!")],
            [sg.Text("User:"), sg.Input(key='user')],
            [sg.Text("Senha:"), sg.Input(key='pwd', password_char='*')],
            [sg.Checkbox('Mostrar senha', key='mostrar'), sg.Button("reload", key='reload')],
            [sg.Button("Cadastrar"), sg.Button("Voltar")]
        ]
    else:
        layout = [
            [sg.Text("Registre-se!")],
            [sg.Text("User:"), sg.Input(key='user')],
            [sg.Text("Senha:"), sg.Input(key='pwd')],
            [sg.Checkbox('Mostrar senha', key='mostrar'), sg.Button("reload", key='reload')],
            [sg.Button("Cadastrar"), sg.Button("Voltar")]
        ]        
    return sg.Window('Cadastro', layout = layout, finalize = True)


def janela2(txt):
    sg.theme("Reddit")
    layout = [
        [sg.Text(txt)],
        [sg.Button('Voltar'), sg.Button('Fechar')]
    ]
    return sg.Window('Resultado',layout= layout, finalize = True)
