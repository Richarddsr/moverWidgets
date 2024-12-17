# Importação das bibliotecas Tkinter para criação de interfaces gráficas
import tkinter as tk
from tkinter import messagebox

# Criação da janela principal (root) usando Tkinter
root = tk.Tk()
root.title("Demonstração de Place Layout")
root.geometry("400x300")

def criar_interface_place():
    # Cria uma nova janela secundária (Toplevel) vinculada à janela principal
    # Place layout: Posiciona widgets usando coordenadas absolutas (x, y)
    janela_place = tk.Toplevel(root)
    janela_place.title("Gerenciador place() 📍")
    janela_place.geometry("300x300")

    # Criação de campos de entrada usando place()
    # Posicionamento absoluto permite controle preciso, mas menos responsivo
    tk.Label(janela_place, text="Nome:", font=('Arial', 10, 'bold')).place(x=50, y=50, width=80, height=30)
    nome_entry = tk.Entry(janela_place, width=20)
    nome_entry.place(x=140, y=50, width=150, height=30)

    tk.Label(janela_place, text="Email:", font=('Arial', 10, 'bold')).place(x=50, y=100, width=80, height=30)
    email_entry = tk.Entry(janela_place, width=20)
    email_entry.place(x=140, y=100, width=150, height=30)

    # Função de callback para processar dados inseridos
    def mostrar_dados():
        # Captura os dados dos campos de entrada
        nome = nome_entry.get()
        email = email_entry.get()
        
        # Validação de entrada com caixas de diálogo
        if nome and email:
            messagebox.showinfo("Dados Inseridos", f"Nome: {nome}\nEmail: {email}")
        else:
            messagebox.showwarning("Dados Incompletos", "Por favor, preencha todos os campos.")

    # Botões posicionados usando place()
    tk.Button(janela_place, text="Enviar", command=mostrar_dados).place(x=50, y=200, width=100, height=40)
    tk.Button(janela_place, text="Fechar", command=janela_place.destroy).place(x=160, y=200, width=100, height=40)

# Botão na janela principal para abrir a interface place
tk.Button(root, text="Abrir Place Layout", command=criar_interface_place).pack(padx=20, pady=20)

# Inicia o loop de eventos da aplicação Tkinter
root.mainloop()
