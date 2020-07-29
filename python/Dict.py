from jarvis import *



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



    
    name()
    a=takeCommand().lower()
    if "yes" in a:
        dicName = {}
        speak("your dictionary have been created please enter the values in form of Key and Values")
        speak("Enter the no. of items you want to Add in dictionary  ")
        limit = takeCommand().lower()
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



        






