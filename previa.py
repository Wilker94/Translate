    
import os
import tkinter as tk
from tkinter import messagebox,ttk
from elevenlabs import save, Voice, VoiceSettings
from elevenlabs.client import *
import json
import pygame
pygame.mixer.init()



def previa_voz(api_input, texto_traducao_input):
    
    

    pygame.mixer.music.stop()
    pygame.mixer.init()

    def play_audio():
        pygame.mixer.music.load(audio_file_path.get())
        pygame.mixer.music.play()

    def pause_audio():
        pygame.mixer.music.pause()
    
    
    textos = texto_traducao_input.get("1.0", "end-1c")
    api = api_input.get("1.0", "end-1c")
    save_filename = "previa.mp3"



    if not api:
        messagebox.showerror("erro", "Por favor, insira a API do Elevenlabs.")
        return
    
    
    
    with open('config.json', 'r') as file:
    
        config = json.load(file)

        voice_system = config.get('default_name')
        stability_system = config.get('stability')
        similarity_system = config.get('similarity_boost')
        style_system = config.get('style')
        boost_system = config.get('boost')


        client = ElevenLabs(api_key=api)
    
    

    # Escolhe a voz baseada no nome fornecido
    voice = None
    voices = client.voices.get_all()
    for voz in voices.voices:
        if voice_system in voz.name:
            voice = voz.voice_id
            break

    if not voice:
        print(f"Voz '{voice_system}' não encontrada.")
        return
    
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    
    # Parar o áudio e encerrar o mixer do Pygame antes de sobrescrever o arquivo
    
    
 
    """
    # Configurações Ideais
    stability = 0.5
    similarity_boost = 0.8
    style = 0
    boost = True"""

    # Configurações opcionais original
    #stability = 0.35
    #similarity_boost = 0.4
    #style = 0.55
    #boost = False

    # Gera o áudio com a API do Eleven Labs
    audio = client.generate(
        text=textos,
        voice=Voice(voice_id=voice,
                    settings=VoiceSettings(stability=stability_system,
                                           similarity_boost=similarity_system,
                                           style=style_system,
                                           use_speaker_boost=boost_system)),
        model='eleven_multilingual_v2'
    )

    # Salva o áudio em um arquivo com o nome fornecido
    audios_folder = os.path.join("C:\\","audiotemp")
    os.makedirs(audios_folder, exist_ok=True)
    os.makedirs(audios_folder, exist_ok=True)
    
    filename = os.path.join(audios_folder, save_filename)

    save(audio=audio, filename=filename)
    
    pygame.mixer.init()

 
    
    # Configuração da interface Tkinter
    root = tk.Tk()
    root.title("Reprodutor de Áudio")
    

    # Defina o caminho automático para o arquivo "previa.mp3" em C:\audiotempo
    audio_file_path = tk.StringVar()
    audio_file_path.set(r"C:\audiotemp\previa.mp3")

    
    tk.Button(root, text="Tocar", command=play_audio).pack()
    tk.Button(root, text="Pausar", command=pause_audio).pack()
    
    
    # Centraliza a janela
    root.update_idletasks()  # Atualiza as dimensões da janela
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    root.mainloop()
    
    
    
    



