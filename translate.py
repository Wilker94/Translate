from deep_translator import GoogleTranslator
import tkinter as tk


def traduz_texto(select_all, unselect_all, texto_traducao_input, checkbox_portugues, translate_portugues_label, translate_portugues_text, 
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
                 checkbox_urdu, translate_urdu_label, translate_urdu_text, checkbox_hindi, translate_hindi_label, translate_hindi_text,
                 checkbox_hebraico, translate_hebraico_label, translate_hebraico_text, checkbox_chines, translate_chines_label, translate_chines_text):
       
    select_all.grid(row=5, column=0, padx=(0,2), pady=(0,30))
    unselect_all.grid(row=5, column=1, padx=(0,2), pady=(0,30))
        
    textos = texto_traducao_input.get("1.0", tk.END)  # Obtém o texto digitado na ScrolledText   
    #translator2 = Translator()    
    
    
    translate_portugues_label.config(text="Português")
    checkbox_portugues.grid(row=6, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translate_portugues_text.config(text=textos)

    #Inglês en               
    translate_ingles_label.config(text="Inglês")
    checkbox_ingles.grid(row=6, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='en')
    translation = translator.translate(textos)
    translate_ingles_text.config(text=translation)
    
    #Espanhol es
    translate_espanhol_label.config(text="Espanhol")
    checkbox_espanhol.grid(row=6, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='es')
    translation = translator.translate(textos)
    translate_espanhol_text.config(text=translation)
        
    #frances fr
    translate_frances_label.config(text="Francês")
    checkbox_frances.grid(row=6, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='fr')
    translation = translator.translate(textos)
    translate_frances_text.config(text=translation)
    
    #alemão de        
    translate_alemao_label.config(text="Alemão")
    checkbox_alemao.grid(row=6, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='de')
    translation = translator.translate(textos)
    translate_alemao_text.config(text=translation)

    #Italiano it
    translate_italiano_label.config(text="Italiano")
    checkbox_italiano.grid(row=6, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='it')
    translation = translator.translate(textos)
    translate_italiano_text.config(text=translation)

    #Árabe AR
    translate_arabe_label.config(text="Árabe")
    checkbox_arabe.grid(row=8, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ar')
    translation = translator.translate(textos)
    translate_arabe_text.config(text=translation)
    
    #Holandes NL
    translate_holandes_label.config(text="Holandês")
    checkbox_holandes.grid(row=8, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='nl')
    translation = translator.translate(textos)
    translate_holandes_text.config(text=translation)
        
    #Polones PL
    translate_polones_label.config(text="Polonês")
    checkbox_polones.grid(row=8, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='pl')
    translation = translator.translate(textos)
    translate_polones_text.config(text=translation)
    
    #Búlgaro BG        
    translate_bulgaro_label.config(text="Búlgaro")
    checkbox_bulgaro.grid(row=8, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='bg')
    translation = translator.translate(textos)
    translate_bulgaro_text.config(text=translation)

    #Croata HR
    translate_croata_label.config(text="Croata")
    checkbox_croata.grid(row=8, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='hr')
    translation = translator.translate(textos)
    translate_croata_text.config(text=translation)

    #Esloveno SL
    translate_esloveno_label.config(text="Esloveno")
    checkbox_esloveno.grid(row=8, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sl')
    translation = translator.translate(textos)
    translate_esloveno_text.config(text=translation)
    
    # Eslovaco
    translate_eslovaco_label.config(text="Eslovaco")
    checkbox_eslovaco.grid(row=10, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sk')
    translation = translator.translate(textos)
    translate_eslovaco_text.config(text=translation)
    
    # Filipino (Tagalo)
    translate_filipino_label.config(text="Filipino")
    checkbox_filipino.grid(row=10, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='tl')
    translation = translator.translate(textos)
    translate_filipino_text.config(text=translation)
    
    # Grego
    translate_grego_label.config(text="Grego")
    checkbox_grego.grid(row=10, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='el')
    translation = translator.translate(textos)
    translate_grego_text.config(text=translation)
      
    # Urdu
    translate_urdu_label.config(text="Urdu")
    checkbox_urdu.grid(row=10, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ur')
    translation = translator.translate(textos)
    translate_urdu_text.config(text=translation)
    
    # Lituano
    translate_lituano_label.config(text="Lituano")
    checkbox_lituano.grid(row=10, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='lt')
    translation = translator.translate(textos)
    translate_lituano_text.config(text=translation)
    
    # Tailandês
    translate_tailandes_label.config(text="Tailandês")
    checkbox_tailandes.grid(row=10, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='th')
    translation = translator.translate(textos)
    translate_tailandes_text.config(text=translation)
    
    # Híndi
    translate_hindi_label.config(text="Híndi")
    checkbox_hindi.grid(row=12, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='hi')
    translation = translator.translate(textos)
    translate_hindi_text.config(text=translation)
    
    # Vietnamita
    translate_vietnam_label.config(text="Vietnamita")
    checkbox_vietnam.grid(row=12, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='vi')
    translation = translator.translate(textos)
    translate_vietnam_text.config(text=translation)
    
    # Bengali
    translate_bengali_label.config(text="Bengali")
    checkbox_bengali.grid(row=12, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='bn')
    translation = translator.translate(textos)
    translate_bengali_text.config(text=translation)
    
    # Húngaro
    translate_hungaro_label.config(text="Húngaro")
    checkbox_hungaro.grid(row=12, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='hu')
    translation = translator.translate(textos)
    translate_hungaro_text.config(text=translation)
    
    # Indonésio
    translate_indonesio_label.config(text="Indonésio")
    checkbox_indonesio.grid(row=12, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='id')
    translation = translator.translate(textos)
    translate_indonesio_text.config(text=translation)
    
    # Sueco
    translate_sueco_label.config(text="Sueco")
    checkbox_sueco.grid(row=12, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sv')
    translation = translator.translate(textos)
    translate_sueco_text.config(text=translation)
    
    # Sérvio
    translate_servio_label.config(text="Sérvio")
    checkbox_servio.grid(row=14, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sr')
    translation = translator.translate(textos)
    translate_servio_text.config(text=translation)
    
    # Tcheco
    translate_tcheco_label.config(text="Tcheco")
    checkbox_tcheco.grid(row=14, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='cs')
    translation = translator.translate(textos)
    translate_tcheco_text.config(text=translation)
    
    # Romeno
    translate_romeno_label.config(text="Romeno")
    checkbox_romeno.grid(row=14, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ro')
    translation = translator.translate(textos)
    translate_romeno_text.config(text=translation)
    
    # Turco
    translate_turco_label.config(text="Turco")
    checkbox_turco.grid(row=14, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='tr')
    translation = translator.translate(textos)
    translate_turco_text.config(text=translation)
    
    # Russo
    translate_russo_label.config(text="Russo")
    checkbox_russo.grid(row=14, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ru')
    translation = translator.translate(textos)
    translate_russo_text.config(text=translation)
    
    # Ucraniano
    translate_ucraniano_label.config(text="Ucraniano")
    checkbox_ucraniano.grid(row=14, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='uk')
    translation = translator.translate(textos)
    translate_ucraniano_text.config(text=translation)
    
    # Malaio
    translate_malaio_label.config(text="Malaio")
    checkbox_malaio.grid(row=16, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ms')
    translation = translator.translate(textos)
    translate_malaio_text.config(text=translation)
       
    """translate_hebraico_label.config(text="Hebraico")
    checkbox_hebraico.grid(row=16, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translation2 = translator2.translate(textos, dest='he').text
    translate_hebraico_text.config(text=translation2)
    
    translate_chines_label.config(text="Chinês Tradicional")
    checkbox_chines.grid(row=16, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translation2 = translator2.translate(textos, dest='zh-tw').text
    translate_chines_text.config(text=translation2)"""
    
        # Malaio
    translate_hebraico_label.config(text="Hebraico")
    checkbox_hebraico.grid(row=16, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='iw')
    translation = translator.translate(textos)
    translate_hebraico_text.config(text=translation)
    
        # Malaio
    translate_chines_label.config(text="Chinês")
    checkbox_chines.grid(row=16, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='chinese (traditional)')
    translation = translator.translate(textos)
    translate_chines_text.config(text=translation)
    
    
def selecionar_tudo(translate_portugues, translate_ingles, translate_espanhol, translate_alemao, translate_frances, 
                    translate_italiano, translate_arabe, translate_holandes, translate_polones, translate_bulgaro, 
                    translate_croata, translate_esloveno, translate_eslovaco, translate_filipino, translate_grego, 
                    translate_urdu, translate_lituano, translate_tailandes, translate_hindi, translate_vietnam, 
                    translate_bengali, translate_hungaro, translate_indonesio, translate_sueco, translate_servio, 
                    translate_tcheco, translate_romeno, translate_turco, translate_russo, translate_ucraniano, 
                    translate_malaio, translate_hebraico, translate_chines):

    translate_portugues.set(True), translate_ingles.set(True), translate_espanhol.set(True), translate_frances.set(True), translate_alemao.set(True), translate_italiano.set(True),
    translate_arabe.set(True), translate_holandes.set(True), translate_polones.set(True), translate_bulgaro.set(True), translate_croata.set(True), translate_esloveno.set(True), 
    translate_eslovaco.set(True), translate_filipino.set(True), translate_grego.set(True), translate_urdu.set(True), translate_lituano.set(True), translate_tailandes.set(True), 
    translate_hindi.set(True), translate_vietnam.set(True), translate_bengali.set(True), translate_hungaro.set(True), translate_indonesio.set(True), translate_sueco.set(True), 
    translate_servio.set(True), translate_tcheco.set(True), translate_romeno.set(True), translate_turco.set(True), translate_russo.set(True), translate_ucraniano.set(True), 
    translate_malaio.set(True), translate_hebraico.set(True), translate_chines.set(True)
    
def desmarcar_tudo(translate_portugues, translate_ingles, translate_espanhol, translate_alemao, translate_frances, 
                    translate_italiano, translate_arabe, translate_holandes, translate_polones, translate_bulgaro, 
                    translate_croata, translate_esloveno, translate_eslovaco, translate_filipino, translate_grego, 
                    translate_urdu, translate_lituano, translate_tailandes, translate_hindi, translate_vietnam, 
                    translate_bengali, translate_hungaro, translate_indonesio, translate_sueco, translate_servio, 
                    translate_tcheco, translate_romeno, translate_turco, translate_russo, translate_ucraniano, 
                    translate_malaio, translate_hebraico, translate_chines):
    
    translate_portugues.set(False), translate_ingles.set(False), translate_espanhol.set(False), translate_frances.set(False), translate_alemao.set(False), translate_italiano.set(False),
    translate_arabe.set(False), translate_holandes.set(False), translate_polones.set(False), translate_bulgaro.set(False), translate_croata.set(False), translate_esloveno.set(False), 
    translate_eslovaco.set(False), translate_filipino.set(False), translate_grego.set(False), translate_urdu.set(False), translate_lituano.set(False), translate_tailandes.set(False), 
    translate_hindi.set(False), translate_vietnam.set(False), translate_bengali.set(False), translate_hungaro.set(False), translate_indonesio.set(False), translate_sueco.set(False), 
    translate_servio.set(False), translate_tcheco.set(False), translate_romeno.set(False), translate_turco.set(False), translate_russo.set(False), translate_ucraniano.set(False), 
    translate_malaio.set(False), translate_hebraico.set(False), translate_chines.set(False)
    

