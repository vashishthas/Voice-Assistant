# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

import pyttsx3
import datetime as dt
import speech_recognition as sr
# import pyaudio
import wikipedia
import webbrowser
import os

 
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=(dt.datetime.now().hour)
    # print(f"Hours {hour}")
    if hour>0 and hour <12:
        speak("Good Morning")
    elif hour <18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

def takeCommand():
    """
    It takes microphone input from the User and returns string
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query= r.recognize_google(audio, language="en-in")
        print(f"User said {query}")
    except Exception as e:
        print(e)
        return "none"
    return query


if __name__=="__main__":
    # speak("Hello. This is your voice assistant")
    wishMe()
    # print("Wish done")
    while(True):
        query=takeCommand().lower()
        # if query=="stop":
        #     break

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(f"Result: {result}")
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open('github.com')
        # elif 'play music' in query:
        #     music_dir="music_path"
        #     songs= os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        elif "time" in query:
            timeNow=dt.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {timeNow}")
            speak(timeNow)
        # elif 'open vscode':
        #     vsPath="file_path"
        #     os.startfile(vsPath)
            

            