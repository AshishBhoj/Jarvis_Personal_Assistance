import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# For Male Voice
# print(voices[0].id)
# For Female Voice  
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning, Aashish")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Aashish")
    else:
        speak("Good Evening, Aashish")

def TakeCommand():
    # It takes microphone input from the user and return output as a string 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Litening.....')
        r.pause_threshold = 1
        audio = r.listen(source)
        # add r.adjust_for_ambient_noise(source) above audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Ashish said : {query}\n")
    
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    
    WishME()
    while True:
        query = TakeCommand().lower()

        # logic for executing tasks based on query
        if "how are you" in query:
            speak("I am fine")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoring to Wikipedia")
            print((results))
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Software\\songs\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            code_path = "C:\\Users\\MOHIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'how are you' in query: 
			speak("I am fine, Thank you") 
			speak("How are you, Sir") 

		elif 'fine' in query or "good" in query: 
			speak("It's good to know that your fine")  


		elif 'exit' in query: 
			speak("Thanks for giving me your time") 
			exit() 

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Mister Aashish") 

        elif "who i am" in query: 
			speak("If you talk then definately your human") 

		elif "why you came to world" in query: 
			speak("Even I don't know it") 

   






