from gtts import gTTS
import os

gTTS("ye hindi text to speech hai", lang="hi").save("hindi.mp3")
os.system("start hindi.mp3")
