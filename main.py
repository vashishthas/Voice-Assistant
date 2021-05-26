import pyttsx3
import datetime as dt
import speech_recognition as sr
# import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

 
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """
    Wishes according to the current time
    """
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
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold=500
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query= r.recognize_google(audio, language="en-in")
        print(f"User said {query}")
    except Exception as e:
        print(e)
        return "none"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def getCoordinates(weather):
    import geocoder
    g=geocoder.ip("me")
    lat=g.lat
    lng=g.lng
    if weather:
        getWeather(lat,lng)
    else:
        speak(f"The latituge is {lat} and longitude is {lng}")

def getWeather(lat,lng):
    print("Weather")

if __name__=="__main__":
    # speak("Hello. This is your voice assistant")
    wishMe()
    # print("Wish done")
    while(True):
        query=takeCommand().lower()
        if "stop" in query or "ok" in query :
            break
        
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
        #     music_dir="Enter music dir path"   #Correct path needed
        #     songs= os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        elif "time" in query:
            timeNow=dt.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {timeNow}")
            speak(timeNow)
        elif "date" in query:
            today=dt.date.today()
            d1=today.strftime("%B %d %Y")
            speak(f"Today is {d1}")
        elif "day" in "query":
            now=dt.datetime.now()
            day=now.strftime("%A")
            speak("Today is {day}")
        # elif 'open vscode':
        #     vsPath="Enter file path"  #Correct path needed
        #     os.startfile(vsPath)
        elif "location" in query:
            getCoordinates(False)
        elif "weather" in query:
            getCoordinates(True)
        elif "email" in query:
            try:
                to="emailAddress"
                speak("What's your message")
                content= takeCommand()
                sendEmail(to,content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry an error occured")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Vashishtha")
        elif "who are you" in query:
            speak("I am your virtual assistant created by Vashishtha")
        elif "who i am" in query:
            speak("If you talk then definately you are human.")
        elif "why you came to world" in query:
            speak("Thanks to Vashishtha, further it's a secret")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
 