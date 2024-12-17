# Importação de bibliotecas Tkinter para criação de interfaces gráficas
# tkinter: Biblioteca padrão do Python para desenvolvimento de interfaces gráficas de usuário (GUI)
# messagebox: Módulo para exibir caixas de diálogo de mensagens e alertas
import tkinter as tk
from tkinter import messagebox

# Criação da janela principal (root) usando Tkinter
# tk.Tk() inicializa a janela base de toda aplicação GUI
root = tk.Tk()
# Define o título da janela principal
root.title("Demonstração de Grid Layout")

# Função para criar uma interface demonstrativa usando o gerenciador de layout grid()
# Grid layout: Organiza widgets em uma grade (linhas e colunas), similar a uma planilha
def criar_interface_grid():
    # Cria uma nova janela secundária (Toplevel) vinculada à janela principal
    # Isso permite criar janelas adicionais independentes da janela principal
    janela_grid = tk.Toplevel(root)
    janela_grid.title("Gerenciador grid() 📐")
    # Define o tamanho inicial da janela (largura x altura)
    janela_grid.geometry("400x400")

    # Demonstração de widgets usando o layout grid()
    # Cada widget é posicionado especificando sua linha (row) e coluna (column)

    # Label e Entry para Nome
    # 'sticky' alinha o widget dentro da célula da grade
    # 'e' significa alinhamento à direita (east)
    # 'padx' e 'pady' adicionam espaçamento externo
    tk.Label(janela_grid, text="Nome:", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky='e')
    nome_entry = tk.Entry(janela_grid, width=20)
    nome_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label e Entry para Email
    tk.Label(janela_grid, text="Email:", font=('Arial', 10, 'bold')).grid(row=1, column=0, padx=5, pady=5, sticky='e')
    email_entry = tk.Entry(janela_grid, width=20)
    email_entry.grid(row=1, column=1, padx=5, pady=5)

    # Labels coloridas para demonstrar posicionamento na grade
    # Cada label ocupa uma célula específica com cores de fundo diferentes
    # 'bg' define a cor de fundo, 'fg' define a cor do texto
    tk.Label(janela_grid, text="Row 0, Col 0", bg="red", fg="white").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 0, Col 1", bg="green", fg="white").grid(row=2, column=1, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 1, Col 0", bg="blue", fg="white").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 1, Col 1", bg="purple", fg="white").grid(row=3, column=1, padx=5, pady=5)

    # Função de callback para processar dados inseridos
    # Demonstra como capturar e validar entrada de usuário
    def mostrar_dados():
        # .get() recupera o texto dos campos de entrada
        nome = nome_entry.get()
        email = email_entry.get()
        
        # Validação de entrada com caixas de diálogo
        if nome and email:
            # messagebox.showinfo(): Exibe mensagem informativa
            messagebox.showinfo("Dados Inseridos", f"Nome: {nome}\nEmail: {email}")
        else:
            # messagebox.showwarning(): Exibe aviso quando dados estão incompletos
            messagebox.showwarning("Dados Incompletos", "Por favor, preencha todos os campos.")

    # Botões usando grid layout
    # 'columnspan=2' faz o botão ocupar duas colunas
    # 'command' define a função a ser chamada quando o botão é clicado
    tk.Button(janela_grid, text="Enviar", command=mostrar_dados).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(janela_grid, text="Fechar", command=janela_grid.destroy).grid(row=5, column=0, columnspan=2, pady=10)

# Botão na janela principal para abrir a interface grid
# .pack() é outro gerenciador de layout (diferente de .grid())
tk.Button(root, text="Abrir Grid Layout", command=criar_interface_grid).pack(padx=20, pady=20)

# Inicia o loop de eventos da aplicação Tkinter
# Mantém a janela aberta e responde a interações do usuário
root.mainloop()