
from typing import AnyStr
from gtts import gTTS
import os
import speech_recognition as sr
import time

myText = 'Ton nom sale fdp ?'
language = 'fr'

myobj = gTTS(text=myText, lang=language, slow=False)
myobj.save('identity.mp3')
os.system('identity.mp3')

time.sleep(1)

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='fr-FR')
        print(text)
        if text == 'Vincent' or text == 'Manon':
            os.system('right.mp3')
        else:
            os.system('wrong.mp3')
    except:
        print('Désolé, pas de voix entrante')

