import tkinter as tk



def checkbox_selecionada(translate_portugues, translate_portugues_text, translate_ingles, translate_ingles_text, 
                         translate_espanhol, translate_espanhol_text, translate_frances, translate_frances_text,
                         translate_alemao, translate_alemao_text, translate_italiano, translate_italiano_text,
                         translate_arabe, translate_arabe_text, translate_holandes, translate_holandes_text,
                         translate_polones, translate_polones_text, translate_bulgaro, translate_bulgaro_text,
                         translate_croata, translate_croata_text, translate_esloveno, translate_esloveno_text,
                         translate_eslovaco, translate_eslovaco_text, translate_filipino, translate_filipino_text,
                         translate_grego, translate_grego_text, translate_lituano, translate_lituano_text,
                         translate_tailandes, translate_tailandes_text, translate_vietnam, translate_vietnam_text,
                         translate_bengali, translate_bengali_text, translate_hungaro, translate_hungaro_text,
                         translate_indonesio, translate_indonesio_text, translate_sueco, translate_sueco_text,
                         translate_servio, translate_servio_text, translate_tcheco, translate_tcheco_text,
                         translate_romeno, translate_romeno_text, translate_turco, translate_turco_text,
                         translate_russo, translate_russo_text, translate_ucraniano, translate_ucraniano_text,
                         translate_malaio, translate_malaio_text, translate_urdu, translate_urdu_text,
                         translate_hindi, translate_hindi_text, translate_hebraico, translate_hebraico_text, 
                         translate_chines, translate_chines_text, contador_num):
   

    # Lista para armazenar os idiomas selecionados e seus respectivos textos
        idiomas_selecionados = []
    
    # Verifica cada idioma e seu respectivo texto
        if translate_portugues.get():
           idiomas_selecionados.append((translate_portugues_text.cget('text').strip()))
    
        if translate_ingles.get():
           idiomas_selecionados.append((translate_ingles_text.cget('text').strip()))
           
        if translate_espanhol.get():
           idiomas_selecionados.append((translate_espanhol_text.cget('text').strip()))

        if translate_alemao.get():
           idiomas_selecionados.append((translate_alemao_text.cget('text').strip()))
           
        if translate_frances.get():
           idiomas_selecionados.append((translate_frances_text.cget('text').strip()))
           
        if translate_italiano.get():
           idiomas_selecionados.append((translate_italiano_text.cget('text').strip()))
           
        if translate_arabe.get():
           idiomas_selecionados.append((translate_arabe_text.cget('text').strip()))
    
        if translate_holandes.get():
           idiomas_selecionados.append((translate_holandes_text.cget('text').strip()))
           
        if translate_polones.get():
           idiomas_selecionados.append((translate_polones_text.cget('text').strip()))

        if translate_bulgaro.get():
           idiomas_selecionados.append((translate_bulgaro_text.cget('text').strip()))
           
        if translate_croata.get():
           idiomas_selecionados.append((translate_croata_text.cget('text').strip()))
           
        if translate_esloveno.get():
           idiomas_selecionados.append((translate_esloveno_text.cget('text').strip()))
           
        
        if translate_eslovaco.get():
            idiomas_selecionados.append(translate_eslovaco_text.cget('text').strip())
        
        if translate_filipino.get():
            idiomas_selecionados.append(translate_filipino_text.cget('text').strip())
        
        if translate_grego.get():
            idiomas_selecionados.append(translate_grego_text.cget('text').strip())
        
        if translate_lituano.get():
              idiomas_selecionados.append(translate_lituano_text.cget('text').strip())
        
        if translate_tailandes.get():
              idiomas_selecionados.append(translate_tailandes_text.cget('text').strip())
        
        if translate_hindi.get():
              idiomas_selecionados.append(translate_hindi_text.cget('text').strip())
        
        if translate_vietnam.get():
              idiomas_selecionados.append(translate_vietnam_text.cget('text').strip())
        
        if translate_bengali.get():
              idiomas_selecionados.append(translate_bengali_text.cget('text').strip())
        
        if translate_hungaro.get():
              idiomas_selecionados.append(translate_hungaro_text.cget('text').strip())
        
        if translate_indonesio.get():
              idiomas_selecionados.append(translate_indonesio_text.cget('text').strip())
        
        if translate_sueco.get():
              idiomas_selecionados.append(translate_sueco_text.cget('text').strip())
        
        if translate_servio.get():
              idiomas_selecionados.append(translate_servio_text.cget('text').strip())
        
        if translate_tcheco.get():
              idiomas_selecionados.append(translate_tcheco_text.cget('text').strip())
        
        if translate_romeno.get():
              idiomas_selecionados.append(translate_romeno_text.cget('text').strip())
        
        if translate_turco.get():
              idiomas_selecionados.append(translate_turco_text.cget('text').strip())
        
        if translate_russo.get():
              idiomas_selecionados.append(translate_russo_text.cget('text').strip())
        
        if translate_ucraniano.get():
              idiomas_selecionados.append(translate_ucraniano_text.cget('text').strip())
        
        if translate_malaio.get():
              idiomas_selecionados.append(translate_malaio_text.cget('text').strip())
        
        if translate_urdu.get():
              idiomas_selecionados.append(translate_urdu_text.cget('text').strip())
              
        if translate_hebraico.get():
            idiomas_selecionados.append(translate_hebraico_text.cget('text').strip())
            
        if translate_chines.get():
            idiomas_selecionados.append(translate_chines_text.cget('text').strip())
        


   
    # Calcula o número total de caracteres
        total_caracteres = sum(len(texto) for texto in idiomas_selecionados)

    
    # Atualiza o contador com o total de caracteres encontrados
        contador_num.config(text=total_caracteres)