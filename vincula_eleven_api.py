#Timestamp Unix é um valor numérico que representa o número de segundos desde a meia-noite UTC de 1º de janeiro de 1970 (época Unix). 

import requests
import datetime
import tkinter as tk


def get_eleven(api_input, caracteres_faltantes, data_renova, contador, contador_num):
    
        api_key = api_input.get("1.0", tk.END).strip()  # Obtém o texto digitado na ScrolledText
        
        

        headers = {
            'xi-api-key': api_key,
            'Content-Type': 'application/json'
        }

        # URL do endpoint para obter informações da conta
        account_info_url = "https://api.elevenlabs.io/v1/user/subscription"


        try:
        # Faz uma requisição GET para obter informações da conta
            response = requests.get(account_info_url, headers=headers)
            response.raise_for_status()  # Verifica se houve algum erro na resposta

        # Converte a resposta JSON em um dicionário
            account_info = response.json()

        # Acessa as variáveis de interesse
            character_count = account_info.get('character_count')
            character_limit = account_info.get('character_limit')
        
            caracteres_get = character_limit - character_count
            timestamp = account_info.get('next_character_count_reset_unix')
            data_reset = datetime.datetime.utcfromtimestamp(timestamp).strftime('%d/%m/%Y')

            caracteres_faltantes.config(text=f"Caracteres restantes: {caracteres_get}")
            caracteres_faltantes.grid(row=0, column=2, padx=0, pady=0, sticky=tk.W)
            data_renova.config(text=f"Próximo Reset: {data_reset}")
            data_renova.grid(row=0, column=3, padx=0, pady=0, sticky=tk.W)
            contador.grid(row=0, column=0, padx=(0,0), pady=0, sticky=tk.W)
            contador_num.grid(row=0, column=1, padx=0, pady=0, sticky=tk.W)
            #return caracteres_get, data_reset



        except requests.exceptions.RequestException as e:
               print(f"Erro ao acessar a API do ElevenLabs: {e}")
        
           
           


    

