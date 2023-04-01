import pyttsx3

engine=pyttsx3.init()

#See how many voices we have in the computer
for voice in engine.getProperty("voices"):
    print(voice)
    
#get the voices    
voices= engine.getProperty("voices")
#set the voice to engine
engine.setProperty("voices", voices[1].id)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()
    

text= input('Enter your text now: ')
Speak(text)
