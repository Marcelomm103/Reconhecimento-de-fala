# Programa para capturar áudio e transcrever para texto.

import speech_recognition as sr

# Criando um recognizer

rec = sr.Recognizer()

# Selecionando qual microfone utilizar

print(sr.Microphone().list_microphone_names())

# Tirando o ruído e ouvindo o audio do microfone

with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('Pode começar a falar:')
    audio = rec.listen(microfone)

    # Para demorar mais a finalizar o audio utilize a seguinte função:
    # rec.pause_threshold = 3

    # Reconhecimento do audio e tradução para texto
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
    except:
        print('Não peguei áudio nenhum')