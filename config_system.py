import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


"""selected_name = None
combobox = None  # Declarar combobox como global
stability = 0.5
similarity_boost = 0.8
style = 0
boost = True"""


# Função para exibir o valor selecionado e armazená-lo na variável global
def mostrar_selecao(event):
    global selected_name
    
    selected_name = combobox.get()
    
    
def salvar_selecao(voz_atual, config):
    global selected_name, default_name, stability, similarity_boost, style, boost
    selected_name = combobox.get()
    stability = slider_stability.get()
    similarity_boost = slider_similarity_boost.get()
    style = slider_style.get()
    boost = bool(boost_var.get())
    boost = boost_var.get() == "True"
    voz_atual.config(text=f"Voz atual - {selected_name}")

    
    
    
    
    
    config_data = {
        "default_name": selected_name,
        "stability": stability,
        "similarity_boost": similarity_boost,
        "style": style,
        "boost": boost
    }
    with open('config.json', 'w') as f:
        json.dump(config_data, f)
    messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")
    config.destroy()



def config_gerais(voz_atual):
    
    global combobox, default_name, stability, similarity_boost, style, boost, slider_stability, slider_similarity_boost, slider_style, boost_var  # Declarar variáveis como global

    # Carregar o valor padrão do JSON, se existir

    with open('config.json', 'r') as f:
        config_data = json.load(f)
        default_name = config_data.get('default_name')
        stability = config_data.get('stability')
        similarity_boost = config_data.get('similarity_boost')
        style = config_data.get('style')
        boost = config_data.get('boost', True)
        
        """config_data = json.load(f)
        default_name = config_data.get("default_name", "")
        stability = config_data.get("stability", 0.5)
        similarity_boost = config_data.get("similarity_boost", 0.8)
        style = config_data.get("style", 0)
        boost = config_data.get("boost", True)"""
    
    config = tk.Tk()
    config.title("Configurações do sistema")

    screen_width = config.winfo_screenwidth()
    screen_height = config.winfo_screenheight()

    window_width = 400  # Largura da janela
    window_height = 400  # Altura da janela

    # Calculando a posição para centralizar a janela
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)


    config.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Lista de nomes
    nomes = ["Sarah", "Laura", "Charlie", "George", "Callum", "Liam", "Charlotte", "Alice", "Matilda", "Will", "Jessica", "Eric", "Chris", "Brian", "Daniel", "Lily", "Bill"]
    
    camada_cima = tk.Label(config)
    camada_cima.grid(row=0, column=0, pady=10)
    
    camada_esquerda = tk.Label(config)
    camada_esquerda.grid(row=1, column=0, padx=15)
    
    # Criação da label "Voz atual"
    label_voz_atual = tk.Label(config, text="Voz atual:")
    label_voz_atual.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

    # Variável tkinter associada à combobox
    var_combobox = tk.StringVar(value=voz_atual)

    combobox = ttk.Combobox(config, textvariable=var_combobox, state='readonly')
    combobox['values'] = nomes
    
    # Definir o valor padrão na combobox
    combobox.set(default_name)

    # Definir o valor padrão a partir do JSON
    var_combobox.set(default_name)

    # Definir o comportamento ao selecionar um item
    combobox.bind("<<ComboboxSelected>>", mostrar_selecao)

    # Posicionamento da combobox na janela
    combobox.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
    
    
    # Criação das barras deslizantes para stability, similarity_boost e style
    tk.Label(config, text="Stability:").grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)
    slider_stability = tk.Scale(config, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
    slider_stability.set(stability)
    slider_stability.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

    tk.Label(config, text="Similarity Boost:").grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)
    slider_similarity_boost = tk.Scale(config, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
    slider_similarity_boost.set(similarity_boost)
    slider_similarity_boost.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W)

    tk.Label(config, text="Style:").grid(row=4, column=1, padx=10, pady=10, sticky=tk.E)
    slider_style = tk.Scale(config, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
    slider_style.set(style)
    slider_style.grid(row=4, column=2, padx=10, pady=10, sticky=tk.W)

    """# Criação da caixa de seleção para boost
    tk.Label(config, text="Boost:").grid(row=5, column=1, padx=10, pady=10, sticky=tk.E)
    boost_var = tk.BooleanVar(value=boost)  # Usando BooleanVar para valores booleanos
    boost_checkbox = ttk.Checkbutton(config, variable=boost_var, onvalue=True, offvalue=False)
    boost_checkbox.grid(row=5, column=2, padx=10, pady=10, sticky=tk.W)"""
    
    
    tk.Label(config, text="Boost:").grid(row=5, column=1, padx=10, pady=10, sticky=tk.E)
    boost_var = ttk.Combobox(config, values=["True", "False"], state='readonly')
    boost_var.set("True" if boost else "False")
    boost_var.grid(row=5, column=2, padx=10, pady=10, sticky=tk.W)
    
    """boost_atual = tk.Label(config, text=f"Boost Atual: {boost}")
    boost_atual.grid(row=6, column=1, columnspan=2)"""
    
    
    # Criação do botão "Salvar"
    btn_salvar = tk.Button(config, text="Salvar", command=lambda: salvar_selecao(voz_atual, config))
    btn_salvar.grid(row=7, column=1, columnspan=2, pady=(20, 0))


    config.mainloop()
    


