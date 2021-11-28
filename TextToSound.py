from gtts import gTTS # pip install gTTS
from playsound import playsound # pip install playsound
import os
from text_to_speech import speak


# mytext = 'Welcome to Broadway Infosys'
mytext = input("Enter any string : ")# reading string from keyboard

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")
playsound('welcome.mp3')

speak("Hello World", "en", save=True, file="Hello-World.mp3")

