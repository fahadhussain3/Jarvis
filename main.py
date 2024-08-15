import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ",1)[1]
        link=music_library.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("Intializing Jarvis")
    while True:
         # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio)

            if(word.lower()=="jarvis"):
                speak("Yes")

                #now we will listn for the command:
                with sr.Microphone() as source:
                  print("Jarvis Active...")
                  audio = r.listen(source, timeout=5, phrase_time_limit=4)
                  command= r.recognize_google(audio)

                  processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))