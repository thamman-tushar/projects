import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk,Image
from jarvis import *
import numpy as np
#import cv2

def TurnOn():
    

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
                  


root=tk.Tk()
canvas = tk.Canvas(root,height = 300,width=700,bg="black")
canvas.pack()

start=tk.Button(root,text = "Turn On Jarvis",padx=10,pady=5,fg="Sky Blue",bg="black",command = TurnOn )
start.pack()

root.mainloop()