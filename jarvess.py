import os.path
import random

import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
import datetime
from config import apikey

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\nJarvis: "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write an email to submit doc"
            },
            {
                "role": "user",
                "content": chatStr
            }
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    reply = response['choices'][0]['message']['content']
    say(reply)
    chatStr += f"{reply}\n"

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt}\n***********\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write an email to submit doc"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    reply = response['choices'][0]['message']['content']
    say(reply)
    chatStr += f"{reply}\n"
    return reply

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"

if __name__ == '__main__':
    say("Hello, I'm Jarvis")
    while True:
        print("Listening.....")
        query = takeCommand()

        if 'open music' in query:
            music_dir = 'C:\\Users\\Dell\\Desktop\\python project\\jarves Ai\\music'  # replace with your music location
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'  # replace with your VS Code location
            os.startfile(codePath)

        elif 'using robot' in query:
            ai(prompt=query)




        else:
            chat(query)
