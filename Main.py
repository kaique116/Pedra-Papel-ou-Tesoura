import random
import tkinter as tk
from tkinter import messagebox

def pedra_papel_tesoura():
    try:
        escolha_usuario = int(entrada.get())
        escolha_maquina = random.randint(1, 3)

        if escolha_maquina == 1:
            if escolha_usuario == 2:
                messagebox.showinfo(message="Você Ganhou! " + "A Máquina Escolheu Pedra!")
            elif escolha_usuario == 1:
                messagebox.showinfo(message="Empate! " + "A Máquina Escolheu Pedra!")
            elif escolha_usuario == 3:
                messagebox.showinfo(message="Você Perdeu! " + "A Máquina Escolheu Pedra!")
        
        if escolha_maquina == 2:
            if escolha_usuario == 2:
                messagebox.showinfo(message="Empate! " + "A Máquina Escolheu Papel!")
            elif escolha_usuario == 1:
                messagebox.showinfo(message="Você Perdeu! " + "A Máquina Escolheu Papel!")
            elif escolha_usuario == 3:
                messagebox.showinfo(message="Você Ganhou! " + "A Máquina Escolheu Papel!")
        
        if escolha_maquina == 3:
            if escolha_usuario == 2:
                messagebox.showinfo(message="Você Perdeu! " + "A Máquina Escolheu Tesoura!")
            elif escolha_usuario == 1:
                messagebox.showinfo(message="Você Ganhou! " + "A Máquina Escolheu Tesoura!")
            elif escolha_usuario == 3:
                messagebox.showinfo(message="Empate! " + "A Máquina Escolheu Tesoura!")

    except Exception as e:
        messagebox.showerror("Erro! " + f"{e}")

janela = tk.Tk()
janela.title("Pedra, Papel ou Tesoura")
janela.geometry("600x250")

tk.Label(janela, text="Pedra, Papel ou Tesoura!").pack()
tk.Label(janela, text="1 Para 'Pedra', 2 Para 'Papel' e 3 Para 'Tesoura'!").pack()
tk.Label(janela, text="Escolha um desses no campo abaixo!").pack()
tk.Label(janela, text="Vamos ver se você tem sorte!").pack()

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="CLIQUE AQUI APÓS ESCOLHER O NÚMERO CORRESPONDENTE A SUA ESCOLHA!", command=pedra_papel_tesoura).pack()

janela.mainloop()
            
