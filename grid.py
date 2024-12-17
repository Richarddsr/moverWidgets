import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Demonstração de Grid Layout")

def criar_interface_grid():
    janela_grid = tk.Toplevel(root)
    janela_grid.title("Gerenciador grid() 📐")
    janela_grid.geometry("400x400")

    # Demonstração de diferentes tipos de widgets
    tk.Label(janela_grid, text="Nome:", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky='e')
    nome_entry = tk.Entry(janela_grid, width=20)
    nome_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela_grid, text="Email:", font=('Arial', 10, 'bold')).grid(row=1, column=0, padx=5, pady=5, sticky='e')
    email_entry = tk.Entry(janela_grid, width=20)
    email_entry.grid(row=1, column=1, padx=5, pady=5)

    # Labels coloridas como no exemplo original
    tk.Label(janela_grid, text="Row 0, Col 0", bg="red", fg="white").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 0, Col 1", bg="green", fg="white").grid(row=2, column=1, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 1, Col 0", bg="blue", fg="white").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 1, Col 1", bg="purple", fg="white").grid(row=3, column=1, padx=5, pady=5)

    # Botão com função de callback
    def mostrar_dados():
        nome = nome_entry.get()
        email = email_entry.get()
        if nome and email:
            messagebox.showinfo("Dados Inseridos", f"Nome: {nome}\nEmail: {email}")
        else:
            messagebox.showwarning("Dados Incompletos", "Por favor, preencha todos os campos.")

    tk.Button(janela_grid, text="Enviar", command=mostrar_dados).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(janela_grid, text="Fechar", command=janela_grid.destroy).grid(row=5, column=0, columnspan=2, pady=10)

# Botão na janela principal para abrir a interface grid
tk.Button(root, text="Abrir Grid Layout", command=criar_interface_grid).pack(padx=20, pady=20)

root.mainloop()