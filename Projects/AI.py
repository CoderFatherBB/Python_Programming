import pywin32_system32
import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3
import pyaudio


# initializing the module
#engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query    


if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()
        
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        else:
            speak("Sorry sir, I did not understood. Can you repeat?")
        



 



#a = input ("What you want to speek a loud : ")
# .say() function is used to speak the text you have written 
# inside the function
#engine.say(a)


# this is used to process and run the program commands
#engine.runAndWait()
