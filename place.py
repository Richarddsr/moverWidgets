# Importação de bibliotecas essenciais do Tkinter
# tkinter: Biblioteca padrão para criação de interfaces gráficas em Python
# messagebox: Módulo para exibir caixas de diálogo de mensagens e alertas
import tkinter as tk
from tkinter import messagebox

# Criação da janela principal (root) - ponto de partida de qualquer aplicação Tkinter
# tk.Tk() inicializa a janela base que servirá como contêiner principal
root = tk.Tk()
# Define o título que aparecerá na barra de título da janela
root.title("Demonstração de Place Layout")
# Configura o tamanho inicial da janela (largura x altura)
root.geometry("400x300")

def criar_interface_place():
    # Cria uma janela secundária (Toplevel) vinculada à janela principal
    # Permite criar múltiplas janelas dentro da mesma aplicação
    # Diferente de criar uma nova janela com Tk(), Toplevel mantém conexão com janela principal
    janela_place = tk.Toplevel(root)
    janela_place.title("Gerenciador place() ")
    janela_place.geometry("300x300")

    # Demonstração do gerenciador de layout place()
    # CARACTERÍSTICAS DO PLACE():
    # - Posicionamento ABSOLUTO de widgets
    # - Controle preciso usando coordenadas x e y
    # - Menos flexível que grid() ou pack()
    # - Útil para layouts customizados ou designs específicos

    # Criação de Label para Nome
    # Parâmetros do place():
    # x: distância horizontal do canto superior esquerdo
    # y: distância vertical do canto superior esquerdo
    # width: largura do widget
    # height: altura do widget
    # font: estilo da fonte (família, tamanho, peso)
    tk.Label(janela_place, 
             text="Nome:", 
             font=('Arial', 10, 'bold')
             ).place(x=50, y=50, width=80, height=30)

    # Campo de entrada (Entry) para Nome
    # Posicionado ao lado da Label usando coordenadas precisas
    nome_entry = tk.Entry(janela_place, width=20)
    nome_entry.place(x=140, y=50, width=150, height=30)

    # Repetição do padrão para o campo de Email
    tk.Label(janela_place, 
             text="Email:", 
             font=('Arial', 10, 'bold')
             ).place(x=50, y=100, width=80, height=30)
    email_entry = tk.Entry(janela_place, width=20)
    email_entry.place(x=140, y=100, width=150, height=30)

    # Função interna (closure) para processar dados do formulário
    # Demonstra conceitos de:
    # 1. Escopo de função
    # 2. Acesso a variáveis externas
    # 3. Validação de entrada
    # 4. Uso de caixas de diálogo
    def mostrar_dados():
        # Método .get() recupera o texto dos campos de entrada
        # Captura os valores digitados pelo usuário
        nome = nome_entry.get()
        email = email_entry.get()
        
        # Validação simples de entrada
        # Verifica se ambos os campos estão preenchidos
        if nome and email:
            # messagebox.showinfo(): Exibe mensagem informativa
            # Mostra os dados inseridos em uma caixa de diálogo
            messagebox.showinfo(
                "Dados Inseridos", 
                f"Nome: {nome}\nEmail: {email}"
            )
        else:
            # messagebox.showwarning(): Exibe aviso quando dados estão incompletos
            # Alerta o usuário sobre o preenchimento incorreto
            messagebox.showwarning(
                "Dados Incompletos", 
                "Por favor, preencha todos os campos."
            )

    # Botões posicionados usando place()
    # Demonstra posicionamento preciso de widgets interativos
    tk.Button(
        janela_place, 
        text="Enviar", 
        command=mostrar_dados  # Vincula a função de callback ao botão
    ).place(x=50, y=200, width=100, height=40)

    tk.Button(
        janela_place, 
        text="Fechar", 
        command=janela_place.destroy  # Fecha a janela atual
    ).place(x=160, y=200, width=100, height=40)

# Botão na janela principal para abrir a interface place
# .pack(): Outro gerenciador de layout (diferente de place e grid)
# Posiciona o botão de forma simples e automática
tk.Button(
    root, 
    text="Abrir Place Layout", 
    command=criar_interface_place  # Chama a função para criar nova janela
).pack(padx=20, pady=20)

# Inicia o loop de eventos da aplicação Tkinter
# Mantém a janela aberta e responde a interações do usuário
# Essencial para aplicações com interface gráfica
root.mainloop()
