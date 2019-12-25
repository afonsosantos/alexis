import os
import random
import time
import webbrowser
from time import ctime

import playsound
import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='pt-PT')
        except sr.UnknownValueError:
            alexis_speak('Desculpe, não entendi o que disse.')
        except sr.RequestError:
            alexis_speak('Desculpe, o meu serviço de voz está offline.')
        return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='pt')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'nome' in voice_data:
        alexis_speak('O meu nome é Alexis')
    if 'data' in voice_data:
        alexis_speak(ctime())
    if 'pesquisar' in voice_data:
        search = record_audio('O que devo procurar?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Aqui está o que encontrei para ' + search)
    if 'localização' in voice_data:
        location = record_audio('Qual a localização?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Aqui está a localização de ' + location)
    if 'sair' in voice_data:
        exit()


time.sleep(1)
alexis_speak('Como o posso ajudar?')

while 1:
    voice_data = record_audio()
    respond(voice_data)
