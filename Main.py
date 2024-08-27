import tkinter as tk
#from atualizador import set_window_position
from interface import *



inicial = tk.Tk()
inicial.title("Tradutor de Texto")
#set_window_position(inicial)


screen_width = inicial.winfo_screenwidth()
screen_height = inicial.winfo_screenheight()

window_width = 1100  # Largura da janela
window_height = 800  # Altura da janela

# Calculando a posição para centralizar a janela
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)


inicial.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


telas(inicial)
inicial.mainloop()


#proxsteps
#pasta nome arquivo
#copiar embaixo de texto
#ctrl z, tab
#adicionar opcional +1 em final nome caso exista ou substituir
#Adicionar diretorio em config


#pendencias
#corrigir vozes - check
#Carregar voz atual em lista - check



#Inserir local a ser salvo em config
#Inserir nome da pasta
#Inserir player pré reprodução
#telinha com progresso de downloads.


#WK 797ccf834e6e157ff1354554b2e93f12
#Wonka1 be00df312290494f3d432b0af6f9bc6c
#NSEW = CIMA BAIXO DIREITA ESQUERDA
#Y= CIMA/BAIXO
#X= DIREITA ESQUERDA

#pip install pyinstaller
#pyinstaller --onefile --noconsole main.py
#pyinstaller --onefile --noconsole --add-data "config.json;." main.py


####################################
#parei em pré visualizador de audio
#arquivos "previa" e "reprodutor_audio"

#Em interface:
"""previa_button = tk.Button(frame_campos, text="Prévia", width=7, command=lambda: previa_voz(api_input,texto_traducao_input))
        previa_button.grid(row=1, column=3, padx=15, pady=2, sticky=tk.E)"""

"""previa_audio = tk.Label(frame_rodape, text="AUSHUISHIUHSUIAH")
        previa_audio.grid(row=0, column=0, columnspan=3, padx=0, pady=0)"""        
        
#Os dois são responsaveis por disponibilizar a opção ao user e tb em adicionar o reprodutor no rodapé.
        
















