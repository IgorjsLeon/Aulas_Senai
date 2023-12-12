import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#Função dos botões:
def funcao_clicar():
    print("Você clicou no botão")

def funcao_abrir():
    pass

#Caixas de Diálogo:
def mensagem():
    pass
    '''messagebox.showinfo('Título', 'Estou aprendendo Python!')'''

janela = tk.Tk()

#menu
menu_bar = tk.Menu()
janela.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Arquivo', menu=file_menu)
file_menu.add_command(label='Abrir', command=funcao_abrir())

#Cria o label usuario:
label = tk.Label(janela, text='Usuário')
label.pack()

#Criar uma area para inserir texto
entrada_txt = tk.Entry(janela, width=10)
entrada_txt.pack()

#Criando outro label:
lbl_senha = tk.Label(janela, text='Senha')
lbl_senha.pack()

#Criar uma area para inserir texto
txt_senha = tk.Entry(janela, width=10)
txt_senha.pack()

#Button Botão:
botao = tk.Button(janela, text='Login', command= funcao_clicar())
botao.pack()

estilo = ttk.Style()
estilo.configure('TButton',  foreground= 'green', padding=(10,10), font=('Arial', 12, 'bold'))

#Aplica estilo no label

'''estilo= ttk.Style()
estilo.configure('TLabel', foreground='green', padding=(10,10), font=('Arial', 12, 'bold'))'''


janela.mainloop()