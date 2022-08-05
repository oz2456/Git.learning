import datetime
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty( 'voice' , voices[0].id)

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

    speak("Jarvis at your service Display Status report")

def takeCommand():
    #It takes microphone input from user and returns string output
  
  r = sr.Recognizer()
  with sr.Microphone() as source:
     print("Listening...")
     r.pause_threshold = 1
     audio = r.listen(source)

  try:
     print("Recognizing...")
     query = r.recognize_google(audio, Language='en-in')
     print(f"User said: {query}\n")

    

  except Exception as e:
    #print(e)
     print("Say that again please...")
     return "None"
  return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
    # query = takeCommand().lower()

    # #logic for executing based on query
    # if 'wikipedia' in query:
    #     speak('Searching Wikipedia...')
    #     query = query.replace("wikipedia", "")
    #     results = wikipedia.summary(query, sentences=2)
    #     speak('According to Wikipedia')
    #     speak(results)