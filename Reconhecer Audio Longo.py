# Programa para realizar reconhecimento de audios longos e encerrar a gravação com uma frase.

import speech_recognition as sr
import time

def tratar_audio(rec, audio):
    global acabou
    try:
        texto = rec.recognize_google(audio, language='pt-BR')
        print(texto)
        if 'encerrar gravação' in texto:
            acabou = True
    except:
        print('Não escutei')

acabou = False

rec = sr.Recognizer()

with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    rec.pause_threshold = 0.8
    rec.dynamic_energy_adjustment_ratio = 1.5
    print('Pode começar a falar:')

parar_ouvir = rec.listen_in_background(microfone, tratar_audio)

while True:
    time.sleep(0.1)
    if acabou == True:
        break

parar_ouvir(wait_for_stop=False)