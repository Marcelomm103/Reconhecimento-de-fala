# Programa para capturar áudio e salvar em arquivo.

import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('Pode começar a falar:')
    audio = rec.listen(microfone)

# Salvando o audio capturado em um arquivo wav, formatos suportados raw, wav, aiff, flac.

with open('audio.wav', 'wb') as arquivo:
    arquivo.write(audio.get_wav_data())

