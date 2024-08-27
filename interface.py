import tkinter as tk
from tkinter import scrolledtext, messagebox
from audio_download import *
from translate import traduz_texto, selecionar_tudo, desmarcar_tudo  # Importa a função do arquivo translate.py
from vincula_eleven_api import get_eleven
from contador_checkbox import checkbox_selecionada
from config_system import config_gerais 
from previa import previa_voz
import json

#Wonka1 be00df312290494f3d432b0af6f9bc6c
#NSEW = CIMA BAIXO DIREITA ESQUERDA


def telas (tela):
    
    def topo ():
        
        global contador_num, caracteres_faltantes, data_renova, contador
        
        #Sistema irá carregar o arquivo Json, r como leitura, e vai declará-lo em file
        with open('config.json', 'r') as file:
            #json load irá carregar as informações de file, irá converter e armazenar em config
            config = json.load(file)
        
        #config.get permite puxar alguma info do arquivo. Nesse caso, o nome
        voz_sistema = config.get('default_name')
        
        
        frame_topo = tk.Frame(tela)
        frame_topo.grid(row=0, column=0, columnspan=6, padx=(15,0), pady=10, sticky=tk.W)

        # Contador de caracteres
        contador = tk.Label(frame_topo, text="Contador:")
        contador.grid(row=0, column=0, padx=(0,0), pady=0, sticky=tk.W)
        
        #Variavel
        contador_num = tk.Label(frame_topo, text="0")
        contador_num.grid(row=0, column=1, padx=0, pady=0, sticky=tk.W)
                    
        #Caracteres faltantes conta
        caracteres_faltantes = tk.Label(frame_topo, text="Caracteres restantes:", width=30)
        caracteres_faltantes.grid(row=0, column=2, padx=0, pady=0, sticky=tk.W)

        #Prox data de renovação
        data_renova = tk.Label(frame_topo, text="Próximo Reset:", width=30)
        data_renova.grid(row=0, column=3, padx=0, pady=0, sticky=tk.W)
        
        voz_atual = tk.Label(frame_topo, text=(f"Voz atual - {voz_sistema}"))
        voz_atual.grid(row=0, column=4, padx=(60,0), sticky=tk.E)
        

        
        
        #Botão Configurações
        config_button = tk.Button(frame_topo, text="CONFIG", height=1, command=lambda: config_gerais(voz_atual))
        config_button.grid(row=0, column=6, padx=(130,0), pady=2, sticky=tk.E)
             
        #caracteres_faltantes.grid_remove()
        #data_renova.grid_remove()
    
    def inputs_user ():
        global api_input, texto_traducao_input      
        
        
        #Frame Responsivo
        frame_campos = tk.Frame(tela)
        frame_campos.grid(row=1, column=0, columnspan=6, padx=(15,0), pady=10, sticky=tk.W)
        
        # Campo de entrada para a API elevenlabs
        api_eleven = tk.Label(frame_campos, text="Digite a API do Elevenlabs:")
        api_eleven.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
        #Input
        api_input = scrolledtext.ScrolledText(frame_campos, width=32, height=1)
        api_input.grid(row=1, column=0, padx=0, pady=0, sticky=tk.W)
        #Botão Buscar Api
        api_buscar = tk.Button(frame_campos, text="Vincular", width=20, command=lambda: get_eleven(api_input, caracteres_faltantes, data_renova, contador, contador_num))
        api_buscar.grid(row=2, column=0, columnspan=2, padx=15, pady=2, sticky=tk.E)

        # Titulo da solicitação de texto
        texto_traducao = tk.Label(frame_campos, text="Digite o texto que deseja traduzir:")
        texto_traducao.grid(row=0, column=2, padx=(10,0), pady=0, sticky=tk.W)
        
        #Input
        texto_traducao_input = scrolledtext.ScrolledText(frame_campos, width=82, height=2)
        texto_traducao_input.grid(row=1, column=2, padx=(10,0), pady=0, sticky=tk.W)
        
        previa_button = tk.Button(frame_campos, text="Prévia", width=7, command=lambda: previa_voz(api_input, texto_traducao_input))
        previa_button.grid(row=1, column=3, padx=15, pady=2, sticky=tk.E)
        
        
        
        

        def botoes ():
        
            #Botão Traduzir
            translate_button = tk.Button(frame_campos, text="Traduzir", width=32, command=lambda: traduz_texto(select_all, unselect_all, texto_traducao_input, checkbox_portugues, translate_portugues_label, translate_portugues_text, 
                 checkbox_ingles, translate_ingles_label, translate_ingles_text, checkbox_espanhol, translate_espanhol_label, translate_espanhol_text, 
                 checkbox_frances, translate_frances_label, translate_frances_text, checkbox_alemao, translate_alemao_label, translate_alemao_text,
                 checkbox_italiano, translate_italiano_label, translate_italiano_text, checkbox_arabe, translate_arabe_label, translate_arabe_text,
                 checkbox_holandes, translate_holandes_label, translate_holandes_text, checkbox_polones, translate_polones_label, translate_polones_text, 
                 checkbox_bulgaro, translate_bulgaro_label, translate_bulgaro_text, checkbox_croata, translate_croata_label, translate_croata_text,
                 checkbox_esloveno, translate_esloveno_label, translate_esloveno_text, checkbox_eslovaco, translate_eslovaco_label, translate_eslovaco_text,
                 checkbox_filipino, translate_filipino_label, translate_filipino_text, checkbox_grego, translate_grego_label, translate_grego_text,
                 checkbox_lituano, translate_lituano_label, translate_lituano_text, checkbox_tailandes, translate_tailandes_label, translate_tailandes_text, 
                 checkbox_vietnam, translate_vietnam_label, translate_vietnam_text, checkbox_bengali, translate_bengali_label, translate_bengali_text,
                 checkbox_hungaro, translate_hungaro_label, translate_hungaro_text, checkbox_indonesio, translate_indonesio_label, translate_indonesio_text,
                 checkbox_sueco, translate_sueco_label, translate_sueco_text, checkbox_servio, translate_servio_label, translate_servio_text,
                 checkbox_tcheco, translate_tcheco_label, translate_tcheco_text, checkbox_romeno, translate_romeno_label, translate_romeno_text,
                 checkbox_turco, translate_turco_label, translate_turco_text, checkbox_russo, translate_russo_label, translate_russo_text,
                 checkbox_ucraniano, translate_ucraniano_label, translate_ucraniano_text, checkbox_malaio, translate_malaio_label, translate_malaio_text,
                 checkbox_urdu, translate_urdu_label, translate_urdu_text, checkbox_hindi, translate_hindi_label, translate_hindi_text, checkbox_hebraico, 
                 translate_hebraico_label, translate_hebraico_text, checkbox_chines, translate_chines_label, translate_chines_text))
            translate_button.grid(row=2, column=2, padx=15, pady=2, sticky=tk.E)
                 
        botoes()
            
    def idiomas_traduzidos():
               
        #frame_textos = tk.Frame(tela)
        #frame_textos.grid(row=6, columnspan=6, padx=(15,0), pady=10, sticky=tk.W)
        
            # Criando o frame com barra de rolagem
        frame_canvas = tk.Frame(tela)
        frame_canvas.grid(row=3, column=0, columnspan=6, padx=10, pady=(40, 10), sticky='nsew')
 
        
        canvas = tk.Canvas(frame_canvas, height=500)
        canvas.grid(row=0, column=0, sticky='nsew')

        scrollbar = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
 
        canvas.configure(yscrollcommand=scrollbar.set)

        frame_textos = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_textos, anchor='nw')

        # Atualizando a geometria do canvas para acompanhar o tamanho do frame_textos
        frame_textos.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Certifique-se de que o frame_canvas expanda corretamente
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        
        def linha_zero():
            
            global select_all, unselect_all
            
            select_all = tk.Button(frame_textos, text="Selecionar Tudo", command=lambda: selecionar_tudo(translate_portugues, translate_ingles, translate_espanhol, translate_alemao, translate_frances, 
                                                                                                translate_italiano, translate_arabe, translate_holandes, translate_polones, translate_bulgaro, 
                                                                                                translate_croata, translate_esloveno, translate_eslovaco, translate_filipino, translate_grego, 
                                                                                                translate_urdu, translate_lituano, translate_tailandes, translate_hindi, translate_vietnam, 
                                                                                                translate_bengali, translate_hungaro, translate_indonesio, translate_sueco, translate_servio, 
                                                                                                translate_tcheco, translate_romeno, translate_turco, translate_russo, translate_ucraniano, 
                                                                                                translate_malaio, translate_hebraico, translate_chines))
            select_all.grid(row=5, column=0, padx=(0,2), pady=(0,30))

            unselect_all = tk.Button(frame_textos, text="Desmarcar Tudo", command=lambda: desmarcar_tudo(translate_portugues, translate_ingles, translate_espanhol, translate_alemao, translate_frances, 
                                                                                                translate_italiano, translate_arabe, translate_holandes, translate_polones, translate_bulgaro, 
                                                                                                translate_croata, translate_esloveno, translate_eslovaco, translate_filipino, translate_grego, 
                                                                                                translate_urdu, translate_lituano, translate_tailandes, translate_hindi, translate_vietnam, 
                                                                                                translate_bengali, translate_hungaro, translate_indonesio, translate_sueco, translate_servio, 
                                                                                                translate_tcheco, translate_romeno, translate_turco, translate_russo, translate_ucraniano, 
                                                                                                translate_malaio, translate_hebraico, translate_chines))
            unselect_all.grid(row=5, column=1, padx=(0,2), pady=(0,30))

            select_all.grid(row=5, column=0, padx=(0,2), pady=(0,30))
            unselect_all.grid(row=5, column=1, padx=(0,2), pady=(0,30))
            
            select_all.grid_remove()
            unselect_all.grid_remove()
            
               
        def linha_um():
            
            global translate_portugues, checkbox_portugues, translate_portugues_label, translate_portugues_text
            global translate_ingles, checkbox_ingles, translate_ingles_label, translate_ingles_text
            global translate_espanhol, checkbox_espanhol, translate_espanhol_label, translate_espanhol_text
            global translate_frances, checkbox_frances, translate_frances_label, translate_frances_text
            global translate_alemao, checkbox_alemao, translate_alemao_label, translate_alemao_text
            global translate_italiano, checkbox_italiano, translate_italiano_label, translate_italiano_text
            
            # Português
            translate_portugues = tk.BooleanVar(frame_textos)
            translate_portugues.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_portugues = tk.Checkbutton(frame_textos, variable=translate_portugues)
            checkbox_portugues.grid(row=6, column=0, padx=(10,0), pady=0, sticky=tk.W)
            translate_portugues_label = tk.Label(frame_textos, text="")
            translate_portugues_label.grid(row=6, column=1, padx=(0,0), pady=2, sticky=tk.W)
            translate_portugues_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_portugues_text.grid(row=7, column=0, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Inglês
            translate_ingles = tk.BooleanVar(frame_textos)
            translate_ingles.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_ingles = tk.Checkbutton(frame_textos, variable=translate_ingles)
            checkbox_ingles.grid(row=6, column=2, padx=(10,0), pady=0, sticky=tk.W)
            translate_ingles_label = tk.Label(frame_textos, text="")
            translate_ingles_label.grid(row=6, column=3, padx=(0,0), pady=2, sticky=tk.W)
            translate_ingles_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_ingles_text.grid(row=7, column=2, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            # Espanhol
            translate_espanhol = tk.BooleanVar(frame_textos)
            translate_espanhol.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_espanhol = tk.Checkbutton(frame_textos, variable=translate_espanhol)
            checkbox_espanhol.grid(row=6, column=4, padx=(10,0), pady=0, sticky=tk.W)
            translate_espanhol_label = tk.Label(frame_textos, text="")
            translate_espanhol_label.grid(row=6, column=5, padx=(0,0), pady=2, sticky=tk.W)
            translate_espanhol_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_espanhol_text.grid(row=7, column=4, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            #Francês
            translate_frances = tk.BooleanVar(frame_textos)
            translate_frances.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_frances = tk.Checkbutton(frame_textos, variable=translate_frances)
            checkbox_frances.grid(row=6, column=6, padx=(10,0), pady=0, sticky=tk.W)
            translate_frances_label = tk.Label(frame_textos, text="")
            translate_frances_label.grid(row=6, column=7, padx=(0,0), pady=2, sticky=tk.W)
            translate_frances_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_frances_text.grid(row=7, column=6, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            # Alemão
            translate_alemao = tk.BooleanVar(frame_textos)
            translate_alemao.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_alemao = tk.Checkbutton(frame_textos, variable=translate_alemao)
            checkbox_alemao.grid(row=6, column=8, padx=(10,0), pady=0, sticky=tk.W)
            translate_alemao_label = tk.Label(frame_textos, text="")
            translate_alemao_label.grid(row=6, column=9, padx=(0,0), pady=2, sticky=tk.W)
            translate_alemao_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_alemao_text.grid(row=7, column=8, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            # Italiano
            translate_italiano = tk.BooleanVar(frame_textos)
            translate_italiano.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_italiano = tk.Checkbutton(frame_textos, variable=translate_italiano)
            checkbox_italiano.grid(row=6, column=10, padx=(10,0), pady=0, sticky=tk.W)
            translate_italiano_label = tk.Label(frame_textos, text="")
            translate_italiano_label.grid(row=6, column=11, padx=(0,0), pady=2, sticky=tk.W)
            translate_italiano_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_italiano_text.grid(row=7, column=10, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
            
            checkbox_portugues.grid_remove()
            checkbox_ingles.grid_remove()
            checkbox_espanhol.grid_remove()
            checkbox_frances.grid_remove()
            checkbox_alemao.grid_remove()
            checkbox_italiano.grid_remove()
        
        def linha_dois ():

            global translate_arabe, checkbox_arabe, translate_arabe_label, translate_arabe_text
            global translate_holandes, checkbox_holandes, translate_holandes_label, translate_holandes_text
            global translate_polones, checkbox_polones, translate_polones_label, translate_polones_text
            global translate_bulgaro, checkbox_bulgaro, translate_bulgaro_label, translate_bulgaro_text
            global translate_croata, checkbox_croata, translate_croata_label, translate_croata_text
            global translate_esloveno, checkbox_esloveno, translate_esloveno_label, translate_esloveno_text
            
            
             # Árabe
            translate_arabe = tk.BooleanVar(frame_textos)
            translate_arabe.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_arabe = tk.Checkbutton(frame_textos, variable=translate_arabe)
            checkbox_arabe.grid(row=8, column=0, padx=(10,0), pady=0, sticky=tk.W)
            translate_arabe_label = tk.Label(frame_textos, text="")
            translate_arabe_label.grid(row=8, column=1, padx=(0,0), pady=2, sticky=tk.W)
            translate_arabe_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_arabe_text.grid(row=9, column=0, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            # Holandês
            translate_holandes = tk.BooleanVar(frame_textos)
            translate_holandes.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_holandes = tk.Checkbutton(frame_textos, variable=translate_holandes)
            checkbox_holandes.grid(row=8, column=2, padx=(10,0), pady=0, sticky=tk.W)
            translate_holandes_label = tk.Label(frame_textos, text="")
            translate_holandes_label.grid(row=8, column=3, padx=(0,0), pady=2, sticky=tk.W)
            translate_holandes_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_holandes_text.grid(row=9, column=2, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            # Polonês
            translate_polones = tk.BooleanVar(frame_textos)
            translate_polones.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_polones = tk.Checkbutton(frame_textos, variable=translate_polones)
            checkbox_polones.grid(row=8, column=4, padx=(10,0), pady=0, sticky=tk.W)
            translate_polones_label = tk.Label(frame_textos, text="")
            translate_polones_label.grid(row=8, column=5, padx=(0,0), pady=2, sticky=tk.W)
            translate_polones_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_polones_text.grid(row=9, column=4, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            #Búlgaro
            translate_bulgaro = tk.BooleanVar(frame_textos)
            translate_bulgaro.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_bulgaro = tk.Checkbutton(frame_textos, variable=translate_bulgaro)
            checkbox_bulgaro.grid(row=8, column=6, padx=(10,0), pady=0, sticky=tk.W)
            translate_bulgaro_label = tk.Label(frame_textos, text="")
            translate_bulgaro_label.grid(row=8, column=7, padx=(0,0), pady=2, sticky=tk.W)
            translate_bulgaro_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_bulgaro_text.grid(row=9, column=6, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
    
            # Croata
            translate_croata = tk.BooleanVar(frame_textos)
            translate_croata.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_croata = tk.Checkbutton(frame_textos, variable=translate_croata)
            checkbox_croata.grid(row=8, column=8, padx=(10,0), pady=0, sticky=tk.W)
            translate_croata_label = tk.Label(frame_textos, text="")
            translate_croata_label.grid(row=8, column=9, padx=(0,0), pady=2, sticky=tk.W)
            translate_croata_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_croata_text.grid(row=9, column=8, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
            
            # Esloveno
            translate_esloveno = tk.BooleanVar(frame_textos)
            translate_esloveno.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_esloveno = tk.Checkbutton(frame_textos, variable=translate_esloveno)
            checkbox_esloveno.grid(row=8, column=10, padx=(10,0), pady=0, sticky=tk.W)
            translate_esloveno_label = tk.Label(frame_textos, text="")
            translate_esloveno_label.grid(row=8, column=11, padx=(0,0), pady=2, sticky=tk.W)
            translate_esloveno_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_esloveno_text.grid(row=9, column=10, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)

            checkbox_arabe.grid_remove()
            checkbox_holandes.grid_remove()
            checkbox_polones.grid_remove()
            checkbox_bulgaro.grid_remove()
            checkbox_croata.grid_remove()
            checkbox_esloveno.grid_remove()
             
        def linha_tres():
            global translate_eslovaco, checkbox_eslovaco, translate_eslovaco_label, translate_eslovaco_text
            global translate_filipino, checkbox_filipino, translate_filipino_label, translate_filipino_text
            global translate_grego, checkbox_grego, translate_grego_label, translate_grego_text
            global translate_urdu, checkbox_urdu, translate_urdu_label, translate_urdu_text
            global translate_lituano, checkbox_lituano, translate_lituano_label, translate_lituano_text
            global translate_tailandes, checkbox_tailandes, translate_tailandes_label, translate_tailandes_text
  
            # Eslovaco
            translate_eslovaco = tk.BooleanVar(frame_textos)
            translate_eslovaco.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_eslovaco = tk.Checkbutton(frame_textos, variable=translate_eslovaco)
            checkbox_eslovaco.grid(row=10, column=0, padx=(10,0), pady=0, sticky=tk.W)
            translate_eslovaco_label = tk.Label(frame_textos, text="")
            translate_eslovaco_label.grid(row=10, column=1, padx=(0,0), pady=2, sticky=tk.W)
            translate_eslovaco_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_eslovaco_text.grid(row=11, column=0, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
  
            # Filipino (tagalo)
            translate_filipino = tk.BooleanVar(frame_textos)
            translate_filipino.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_filipino = tk.Checkbutton(frame_textos, variable=translate_filipino)
            checkbox_filipino.grid(row=10, column=2, padx=(10,0), pady=0, sticky=tk.W)
            translate_filipino_label = tk.Label(frame_textos, text="")
            translate_filipino_label.grid(row=10, column=3, padx=(0,0), pady=2, sticky=tk.W)
            translate_filipino_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_filipino_text.grid(row=11, column=2, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)              
            # Grego
            translate_grego = tk.BooleanVar(frame_textos)
            translate_grego.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_grego = tk.Checkbutton(frame_textos, variable=translate_grego)
            checkbox_grego.grid(row=10, column=4, padx=(10,0), pady=0, sticky=tk.W)
            translate_grego_label = tk.Label(frame_textos, text="")
            translate_grego_label.grid(row=10, column=5, padx=(0,0), pady=2, sticky=tk.W)
            translate_grego_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_grego_text.grid(row=11, column=4, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)              

            
            
            # Urdu
            translate_urdu = tk.BooleanVar(frame_textos)
            translate_urdu.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_urdu = tk.Checkbutton(frame_textos, variable=translate_urdu)
            checkbox_urdu.grid(row=10, column=6, padx=(10,0), pady=0, sticky=tk.W)
            translate_urdu_label = tk.Label(frame_textos, text="")
            translate_urdu_label.grid(row=10, column=7, padx=(0,0), pady=2, sticky=tk.W)
            translate_urdu_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_urdu_text.grid(row=11, column=6, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
            

           

            # Lituano
            translate_lituano = tk.BooleanVar(frame_textos)
            translate_lituano.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_lituano = tk.Checkbutton(frame_textos, variable=translate_lituano)
            checkbox_lituano.grid(row=10, column=8, padx=(10,0), pady=0, sticky=tk.W)
            translate_lituano_label = tk.Label(frame_textos, text="")
            translate_lituano_label.grid(row=10, column=9, padx=(0,0), pady=2, sticky=tk.W)
            translate_lituano_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_lituano_text.grid(row=11, column=8, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)              
            # Tailandês
            translate_tailandes = tk.BooleanVar(frame_textos)
            translate_tailandes.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_tailandes = tk.Checkbutton(frame_textos, variable=translate_tailandes)
            checkbox_tailandes.grid(row=10, column=10, padx=(10,0), pady=0, sticky=tk.W)
            translate_tailandes_label = tk.Label(frame_textos, text="")
            translate_tailandes_label.grid(row=10, column=11, padx=(0,0), pady=2, sticky=tk.W)
            translate_tailandes_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_tailandes_text.grid(row=11, column=10, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
            
            checkbox_eslovaco.grid_remove()
            checkbox_filipino.grid_remove()
            checkbox_grego.grid_remove()
            checkbox_lituano.grid_remove()
            checkbox_tailandes.grid_remove()
            checkbox_urdu.grid_remove()
        
        def linha_quatro():
            #global translate_chines, checkbox_chines, translate_chines_label, translate_chines_text
            global translate_hindi, checkbox_hindi, translate_hindi_label, translate_hindi_text
            global translate_vietnam, checkbox_vietnam, translate_vietnam_label, translate_vietnam_text
            global translate_bengali, checkbox_bengali, translate_bengali_label, translate_bengali_text
            global translate_hungaro, checkbox_hungaro, translate_hungaro_label, translate_hungaro_text
            global translate_indonesio, checkbox_indonesio, translate_indonesio_label, translate_indonesio_text
            global translate_sueco, checkbox_sueco, translate_sueco_label, translate_sueco_text       
            
            
            # Vietnamita
            
                                

            # Híndi
            translate_hindi = tk.BooleanVar(frame_textos)
            translate_hindi.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_hindi = tk.Checkbutton(frame_textos, variable=translate_hindi)
            checkbox_hindi.grid(row=12, column=0, padx=(10,0), pady=0, sticky=tk.W)
            translate_hindi_label = tk.Label(frame_textos, text="")
            translate_hindi_label.grid(row=12, column=1, padx=(0,0), pady=2, sticky=tk.W)
            translate_hindi_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_hindi_text.grid(row=13, column=0, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
                    
                    
            translate_vietnam = tk.BooleanVar(frame_textos)
            translate_vietnam.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_vietnam = tk.Checkbutton(frame_textos, variable=translate_vietnam)
            checkbox_vietnam.grid(row=12, column=2, padx=(10,0), pady=0, sticky=tk.W)
            translate_vietnam_label = tk.Label(frame_textos, text="")
            translate_vietnam_label.grid(row=12, column=3, padx=(0,0), pady=2, sticky=tk.W)
            translate_vietnam_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_vietnam_text.grid(row=13, column=2, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)       
            # Bengali
            translate_bengali = tk.BooleanVar(frame_textos)
            translate_bengali.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_bengali = tk.Checkbutton(frame_textos, variable=translate_bengali)
            checkbox_bengali.grid(row=12, column=4, padx=(10,0), pady=0, sticky=tk.W)
            translate_bengali_label = tk.Label(frame_textos, text="")
            translate_bengali_label.grid(row=12, column=5, padx=(0,0), pady=2, sticky=tk.W)
            translate_bengali_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_bengali_text.grid(row=13, column=4, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)       
            # Húngaro
            translate_hungaro = tk.BooleanVar(frame_textos)
            translate_hungaro.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_hungaro = tk.Checkbutton(frame_textos, variable=translate_hungaro)
            checkbox_hungaro.grid(row=12, column=6, padx=(10,0), pady=0, sticky=tk.W)
            translate_hungaro_label = tk.Label(frame_textos, text="")
            translate_hungaro_label.grid(row=12, column=7, padx=(0,0), pady=2, sticky=tk.W)
            translate_hungaro_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_hungaro_text.grid(row=13, column=6, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)       
            # Indonésio
            translate_indonesio = tk.BooleanVar(frame_textos)
            translate_indonesio.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_indonesio = tk.Checkbutton(frame_textos, variable=translate_indonesio)
            checkbox_indonesio.grid(row=12, column=8, padx=(10,0), pady=0, sticky=tk.W)
            translate_indonesio_label = tk.Label(frame_textos, text="")
            translate_indonesio_label.grid(row=12, column=9, padx=(0,0), pady=2, sticky=tk.W)
            translate_indonesio_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_indonesio_text.grid(row=13, column=8, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)       
            # Sueco
            translate_sueco = tk.BooleanVar(frame_textos)
            translate_sueco.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_sueco = tk.Checkbutton(frame_textos, variable=translate_sueco)
            checkbox_sueco.grid(row=12, column=10, padx=(10,0), pady=0, sticky=tk.W)
            translate_sueco_label = tk.Label(frame_textos, text="")
            translate_sueco_label.grid(row=12, column=11, padx=(0,0), pady=2, sticky=tk.W)
            translate_sueco_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_sueco_text.grid(row=13, column=10, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)       

            
            checkbox_vietnam.grid_remove()
            checkbox_bengali.grid_remove()
            checkbox_hungaro.grid_remove()
            checkbox_indonesio.grid_remove()
            checkbox_sueco.grid_remove()
            checkbox_hindi.grid_remove()

        def linha_cinco():
            global translate_servio, checkbox_servio, translate_servio_label, translate_servio_text
            global translate_tcheco, checkbox_tcheco, translate_tcheco_label, translate_tcheco_text
            global translate_romeno, checkbox_romeno, translate_romeno_label, translate_romeno_text
            global translate_turco, checkbox_turco, translate_turco_label, translate_turco_text
            global translate_russo, checkbox_russo, translate_russo_label, translate_russo_text
            global translate_ucraniano, checkbox_ucraniano, translate_ucraniano_label, translate_ucraniano_text
        
            # Sérvio
            translate_servio = tk.BooleanVar(frame_textos)
            translate_servio.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_servio = tk.Checkbutton(frame_textos, variable=translate_servio)
            checkbox_servio.grid(row=14, column=0, padx=(10,0), pady=0, sticky=tk.W)
            translate_servio_label = tk.Label(frame_textos, text="")
            translate_servio_label.grid(row=14, column=1, padx=(0,0), pady=2, sticky=tk.W)
            translate_servio_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_servio_text.grid(row=15, column=0, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Tcheco
            translate_tcheco = tk.BooleanVar(frame_textos)
            translate_tcheco.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_tcheco = tk.Checkbutton(frame_textos, variable=translate_tcheco)
            checkbox_tcheco.grid(row=14, column=2, padx=(10,0), pady=0, sticky=tk.W)
            translate_tcheco_label = tk.Label(frame_textos, text="")
            translate_tcheco_label.grid(row=14, column=3, padx=(0,0), pady=2, sticky=tk.W)
            translate_tcheco_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_tcheco_text.grid(row=15, column=2, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Romeno
            translate_romeno = tk.BooleanVar(frame_textos)
            translate_romeno.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_romeno = tk.Checkbutton(frame_textos, variable=translate_romeno)
            checkbox_romeno.grid(row=14, column=4, padx=(10,0), pady=0, sticky=tk.W)
            translate_romeno_label = tk.Label(frame_textos, text="")
            translate_romeno_label.grid(row=14, column=5, padx=(0,0), pady=2, sticky=tk.W)
            translate_romeno_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_romeno_text.grid(row=15, column=4, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Turco
            translate_turco = tk.BooleanVar(frame_textos)
            translate_turco.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_turco = tk.Checkbutton(frame_textos, variable=translate_turco)
            checkbox_turco.grid(row=14, column=6, padx=(10,0), pady=0, sticky=tk.W)
            translate_turco_label = tk.Label(frame_textos, text="")
            translate_turco_label.grid(row=14, column=7, padx=(0,0), pady=2, sticky=tk.W)
            translate_turco_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_turco_text.grid(row=15, column=6, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Russo
            translate_russo = tk.BooleanVar(frame_textos)
            translate_russo.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_russo = tk.Checkbutton(frame_textos, variable=translate_russo)
            checkbox_russo.grid(row=14, column=8, padx=(10,0), pady=0, sticky=tk.W)
            translate_russo_label = tk.Label(frame_textos, text="")
            translate_russo_label.grid(row=14, column=9, padx=(0,0), pady=2, sticky=tk.W)
            translate_russo_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_russo_text.grid(row=15, column=8, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Ucraniano
            translate_ucraniano = tk.BooleanVar(frame_textos)
            translate_ucraniano.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_ucraniano = tk.Checkbutton(frame_textos, variable=translate_ucraniano)
            checkbox_ucraniano.grid(row=14, column=10, padx=(10,0), pady=0, sticky=tk.W)
            translate_ucraniano_label = tk.Label(frame_textos, text="")
            translate_ucraniano_label.grid(row=14, column=11, padx=(0,0), pady=2, sticky=tk.W)
            translate_ucraniano_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_ucraniano_text.grid(row=15, column=10, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            # Remove previous checkboxes
            checkbox_servio.grid_remove()
            checkbox_tcheco.grid_remove()
            checkbox_romeno.grid_remove()
            checkbox_turco.grid_remove()
            checkbox_russo.grid_remove()
            checkbox_ucraniano.grid_remove()
            
        def linha_seis():
            global translate_malaio, checkbox_malaio, translate_malaio_label, translate_malaio_text
            global translate_hebraico, checkbox_hebraico, translate_hebraico_label, translate_hebraico_text
            global translate_chines, checkbox_chines, translate_chines_label, translate_chines_text
        
            # Malaio
            translate_malaio = tk.BooleanVar(frame_textos)
            translate_malaio.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_malaio = tk.Checkbutton(frame_textos, variable=translate_malaio)
            checkbox_malaio.grid(row=16, column=0, padx=(10,0), pady=0, sticky=tk.W)
            translate_malaio_label = tk.Label(frame_textos, text="")
            translate_malaio_label.grid(row=16, column=1, padx=(0,0), pady=2, sticky=tk.W)
            translate_malaio_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_malaio_text.grid(row=17, column=0, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
            
            # Hebraico
            translate_hebraico = tk.BooleanVar(frame_textos)
            translate_hebraico.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_hebraico = tk.Checkbutton(frame_textos, variable=translate_hebraico)
            checkbox_hebraico.grid(row=16, column=2, padx=(10,0), pady=0, sticky=tk.W)
            translate_hebraico_label = tk.Label(frame_textos, text="")
            translate_hebraico_label.grid(row=16, column=3, padx=(0,0), pady=2, sticky=tk.W)
            translate_hebraico_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_hebraico_text.grid(row=17, column=2, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)  
            
            # Chinês
            translate_chines = tk.BooleanVar(frame_textos)
            translate_chines.trace_add("write", lambda *args: checkbox_selecionada(translate_portugues, translate_portugues_text,
            translate_ingles, translate_ingles_text, translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
            translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text, translate_arabe, translate_arabe_text, 
            translate_holandes, translate_holandes_text, translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text, 
            translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text, translate_eslovaco, translate_eslovaco_text, 
            translate_filipino, translate_filipino_text, translate_grego, translate_grego_text, translate_lituano, translate_lituano_text, translate_tailandes,
            translate_tailandes_text, translate_vietnam, translate_vietnam_text, translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
            translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text, translate_servio, translate_servio_text,
            translate_tcheco, translate_tcheco_text, translate_romeno, translate_romeno_text, translate_turco, translate_turco_text, translate_russo,
            translate_russo_text, translate_ucraniano, translate_ucraniano_text, translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
            translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, translate_chines, translate_chines_text, contador_num))
            checkbox_chines = tk.Checkbutton(frame_textos, variable=translate_chines)
            checkbox_chines.grid(row=16, column=4, padx=(10,0), pady=0, sticky=tk.W)
            translate_chines_label = tk.Label(frame_textos, text="")
            translate_chines_label.grid(row=16, column=5, padx=(0,0), pady=2, sticky=tk.W)
            translate_chines_text = tk.Label(frame_textos, text="", wraplength=120, width=22)
            translate_chines_text.grid(row=17, column=4, columnspan=2, padx=(10,0), pady=(2,30), sticky=tk.W)
        
            checkbox_malaio.grid_remove()            
            checkbox_hebraico.grid_remove()          
            checkbox_chines.grid_remove()          
        
        
        
        linha_zero()
        linha_um()
        linha_dois()
        linha_tres()
        linha_quatro()
        linha_cinco()
        linha_seis()
        
    def rodape():
        
        frame_rodape = tk.Frame(tela)
        frame_rodape.grid(row=4, column=0, columnspan=6, padx=(15,0), pady=10, sticky=tk.E)
        
        #Botão Baixar Audio
        translate_button = tk.Button(frame_rodape, text="Baixar Áudios", height=3, command=lambda: baixa_audio(api_input, 
                                        translate_portugues, translate_portugues_text, translate_portugues_label,
                                        translate_ingles, translate_ingles_text, translate_ingles_label,
                                        translate_espanhol, translate_espanhol_text, translate_espanhol_label,
                                        translate_alemao, translate_alemao_text, translate_alemao_label,
                                        translate_frances, translate_frances_text, translate_frances_label,
                                        translate_italiano, translate_italiano_text, translate_italiano_label,
                                        translate_arabe, translate_arabe_text, translate_arabe_label,
                                        translate_holandes, translate_holandes_text, translate_holandes_label,
                                        translate_polones, translate_polones_text, translate_polones_label,
                                        translate_bulgaro, translate_bulgaro_text, translate_bulgaro_label,
                                        translate_croata, translate_croata_text, translate_croata_label,
                                        translate_esloveno, translate_esloveno_text, translate_esloveno_label,
                                        translate_eslovaco, translate_eslovaco_text, translate_eslovaco_label,
                                        translate_filipino, translate_filipino_text, translate_filipino_label,
                                        translate_grego, translate_grego_text, translate_grego_label,
                                        translate_urdu, translate_urdu_text, translate_urdu_label,
                                        translate_lituano, translate_lituano_text, translate_lituano_label,
                                        translate_tailandes, translate_tailandes_text, translate_tailandes_label,
                                        translate_hindi, translate_hindi_text, translate_hindi_label,
                                        translate_vietnam, translate_vietnam_text, translate_vietnam_label,
                                        translate_bengali, translate_bengali_text, translate_bengali_label,
                                        translate_hungaro, translate_hungaro_text, translate_hungaro_label,
                                        translate_indonesio, translate_indonesio_text, translate_indonesio_label,
                                        translate_sueco, translate_sueco_text, translate_sueco_label,
                                        translate_servio, translate_servio_text, translate_servio_label,
                                        translate_tcheco, translate_tcheco_text, translate_tcheco_label,
                                        translate_romeno, translate_romeno_text, translate_romeno_label,
                                        translate_turco, translate_turco_text, translate_turco_label,
                                        translate_russo, translate_russo_text, translate_russo_label,
                                        translate_ucraniano, translate_ucraniano_text, translate_ucraniano_label,
                                        translate_malaio, translate_malaio_text, translate_malaio_label,
                                        translate_hebraico, translate_hebraico_text, translate_hebraico_label, 
                                        translate_chines, translate_chines_text, translate_chines_label))
        translate_button.grid(row=0,  column=3, padx=(20,0), pady=2)
        
        seleciona_tudo = tk.Button(frame_rodape, text="Select All", height=3, command=lambda: baixa_audio(
                                        translate_portugues, translate_ingles,translate_espanhol, translate_alemao, translate_frances, translate_italiano, 
                                        translate_arabe, translate_holandes, translate_polones, translate_bulgaro, translate_croata, translate_esloveno, 
                                        translate_eslovaco, translate_filipino, translate_grego, translate_urdu, translate_lituano, translate_tailandes, 
                                        translate_hindi, translate_vietnam, translate_bengali, translate_hungaro, translate_indonesio, translate_sueco, 
                                        translate_servio, translate_tcheco, translate_romeno, translate_turco, translate_russo, translate_ucraniano, 
                                        translate_malaio, translate_hebraico, translate_chines_label))
        translate_button.grid(row=0,  column=0, padx=(20,0), pady=2)
        
        

        
    topo()
    inputs_user()    
    idiomas_traduzidos()
    rodape()
    
    #idiomas_traduzidos()


    
    
 
        
        
        

    
    

    