from libraries import *

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#ices)
engine.setProperty('voice', voices[0].id)

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
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('emailid urs','password')
    server.sendmail('urs email id', to, content)
    server.close()

def wishme():
    hours= int(datetime.datetime.now().hour)
    speak("Switching On........Our Survers\n.....................Connecting to Our Database...................\nLoading..Our Files.......we will be thier..............\n\njust a movement Sir...........")
    if hours>=0 and hours<12:
        speak("Good Morning!")
        
    elif hours>=12 and hours<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir. I am Online how can i help you")
    

def replace(string): 
    return string.replace(" ", "_")


def name():
    speak("ok sir, your command has been recieved. So What name you want to give for new Dictionary?")
    dicName = replace(takeCommand().lower())
    speak("is it '"+dicName.lower()+"' ?")


def create():
    crDic= takeCommand().lower()
    if "no" in crDic:
        speak("Do you want to select some other dictionary ?")
        b=takeCommand().lower()
        
        if "yes" in b:
            speak("Sir Program is under Working...")

        elif "no" in b:
            speak("Sir Program is under Working...")

    elif "yes" in crDic:

        name()
        a=takeCommand().lower()
        if "yes" in a:
            dicName = {}
            speak("your dictionary have been created please enter the values in form of Key and Values")
            # label .check
            speak("Enter the number of items you want to Add in dictionary  ")
            try:
                limit = takeCommand().lower()
            except Exception as e:
                # goto .check

            for i in range(int(limit)):
                speak("so what is the data of your number "+str(i+1)+" values type as follows")
                speak("Lable Key Please: ")
                keys = takeCommand().lower()
                speak("Lable values Please: ")
                values = takeCommand().lower()
                dicName[keys]=values
            speak("Here is your Dictionary Sir ")
            print("Here is your Dictionary Sir :\n")
            print(dicName)
           
            speak("Congratulations! Sir you created the new dictionary")
                    
        elif "no" in a:
            name()
            a=takeCommand().lower()

def TurnOff():
    speak("Disconnecting all Servers.........................Hope we meet soon......by.....sir...take..care..")
    exit()


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
                  

