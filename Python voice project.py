# pip install gtts
from gtts import gTTS

# pip install playsound
from playsound import playsound

while 4:
#enter audio file name with .mp3 extension
    
 audio = input('speech.mp3')
 language = 'en'
 sp= gTTS(text = input("enter your text which u want to convert into audio file"), lang = language, slow=False)
 sp.save(audio)
 playsound(audio)
         
         
