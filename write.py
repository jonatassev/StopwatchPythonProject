from dados import Dados
import csv
from tkinter import *

class Write():
    

    def save(self):
        print("Save!")
        
        dados = Dados(self.client, "Jonatas Silva", "00:00:00", self.action, self.description)
        print(dados.cliente, dados.nome, dados.data, dados.horas, dados.acao, dados.descricao)
        self.newWindow.destroy()
        
    def cancel(self):
        print("Cancelar!")
        self.newWindow.destroy()

    def __init__(self, label):

        self.newWindow = Tk()
        self.newWindow.title("Gravar")
        self.newWindow.geometry("400x300")
        Label(self.newWindow,text = "Gravar informações:",font=("Arial 20 bold")).pack(anchor = 'center',pady=20)
        Label(self.newWindow, text="Cliente", width=20,font=("bold",10)).pack()
        self.client = Entry(self.newWindow).pack()
        Label(self.newWindow, text="Ação", width=20,font=("bold",10)).pack()
        self.action = Entry(self.newWindow).pack()
        Label(self.newWindow, text="Descrição", width=20,font=("bold",10)).pack()
        self.description = Entry(self.newWindow).pack()
        self.bt1 = Button(self.newWindow,text="Salvar",command=self.save,font=("Arial 12 bold"),bg=("green"))
        self.bt2 = Button(self.newWindow,text="Cancelar",command=self.cancel,font=("Arial 12 bold"),bg=("red"))
        self.bt1.pack(side="right",pady=5)
        self.bt2.pack(side="right",pady=5)

