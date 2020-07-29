import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
from Dict import *




engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#ices)
engine.setProperty('voice', voices[0].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('emailid urs','password')
    server.sendmail('urs email id', to, content)
    server.close()

def wishme():
    hours= int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good Morning!")
        
    elif hours>=12 and hours<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir. I am Online how can i help you")
    

def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()
    
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print("User Said : \n"+ query + " \n")

        
    except Exception as e:
        
        speak("Say that again Please...")
        return "none"
    return query
    
if __name__ == "__main__":
    wishme()
    while True:
        query= takeCommand().lower()

        #play random musics
        if 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[8]))


        elif 'dictionary' in query:
            speak("Sir would you like to create a new Dictionary ?")
            create()

            
        
        
        #Wikipedia
        elif 'wikipedia' in query:
            speak('Searching wikipedia...')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
            
            #open from browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'quit' in query or 'bye' in query:
            speak("Qutting Sir,Thanks For your time")
            exit()
            
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strTime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
                  
                  
                
                  
        elif 'open code' in query:
            codepath = 'C:\\Users\\Tushar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'  #open app
            os.startfile(codepath)
                  
                  
        elif 'send mail' in query:
            try:
                  speak("please type the mail id you want to send...")
                  email = input("Email ID: ")
                  speak("What should i say...?")
                  content = takeCommand()
                  to = email
                  sendEmail(to, content)
                  speak("Email has been sent!")
                  
            except Exception as e:
                  print(e)
                  speak("Sorry Sir, Some Technical Problem")

            
            #timeme
                  
