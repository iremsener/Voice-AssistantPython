import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

kayit = sr.Recognizer()

def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""

        try:
            ses = kayit.recognize_google(mikrofon, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistn: Sistem çalışmıyor.")


        return ses

def konusma(metin):
    tts = gTTS(text=metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound("konusma.mp3")
    os.remove(ses)

def yanit(ses):
    if "merhaba" in ses:
            konusma("Hoşgeldiniz size nasıl yardımcı olabilirm")
    if "neler yapıyorsun" in ses:
            konusma("kendim hakkında bilgi vermekten hoşlanmıyorum biliyorsun, yine de teşekkür ederim nezaketin için. beni anlayacağını düşünüyorum")
        
    if "çıkış" in ses:
        konusma("Çıkış yapılıyor")
        quit()
    
        

konusma("Merhaba")
print("Başlatıldı...")

while True:
    ses = dinleme()
    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanit(ses)
