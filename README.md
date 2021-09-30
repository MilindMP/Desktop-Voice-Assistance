# JARVIS-Desktop-Voice-Assistance

import pyttsx3    # It converts text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random    # Generate random numbers
import smtplib  # for sending emails
import time
from pynotifier import Notification
import sports       # Gives live info about sports
import requests
import json
from pasw import psw


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("What is your name")
    name = takeCommond()
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f'Good Morning {name}')
    elif hour >= 12 and hour < 18:
        speak(f'Good afternoon {name}')
    else:
        speak(f'Good evening {name}')
    speak('i am Jarvis. Please tell me how may i help you')


def takeCommond():
    # it takes microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user="mppatil0103@gmail.com", password=psw)    #psw for password security
    server.sendmail('mppatil0103@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()

    while True:
        global name
        query = takeCommond().lower()
        if 'wikipedia' in query:
            speak("searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('sure')

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak('ok')

        elif 'open whatsapp web' in query:
            webbrowser.open("web.whatsapp.com")
            speak('sure')

        elif 'open google' in query:
            speak("what u want to search?")
            content = takeCommond()
            webbrowser.open(content)
            speak("here is your result")
            speak(content)

        elif 'play music' in query:
            music_lst = [i for i in range(40)]
            choice = random.choice(music_lst)
            music_dir = 'E:\\music\\my_music'  # here use \\ for escaping character
            songs = os.listdir(music_dir)
            speak('This is awesome')
            print(songs)
            os.startfile(os.path.join(music_dir, songs[choice]))

        elif 'play rap songs' in query:
            content = takeCommond()
            webbrowser.open('spotify.com')
            speak('This is cool')

        elif "what's the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
            print(strtime)

        elif 'what is the date' in query:
            strdate = datetime.date.today().strftime("%D")
            speak(f"MP, the date is {strdate}")
            print(strdate)

        elif 'open vs code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak('ok, its time for coding')

        elif 'open pycharm' in query:
            codepath1 = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(codepath1)
            speak('Lets some do python practise')

        elif 'send a mail' in query:
            try:
                speak("Enter the email ID of the person you want to send it to")
                to = input("Enter Email Id: ")

                speak("what should i say?")
                content = takeCommond()

                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry MP! I am not able to send this email")

        elif "today's news" in query:
            def speak(str):
                from win32com.client import Dispatch
                speaks = Dispatch("SAPI.SpVoice")
                speaks.Speak(str)

            if __name__ == '__main__':
                speak("News for today.. Lets begin")
                url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                for article in arts:
                    speak(article['title'])
                    print(article['title'])
                    speak("Moving on to the next news..Listen Carefully")

                speak("Thanks for listening...")

        elif 'set timer' in query:
            def speak(str):
                from win32com.client import Dispatch
                speaks = Dispatch("SAPI.SpVoice")
                speaks.Speak(str)

            def countdown(t):
                from win32com.client import Dispatch
                speaks = Dispatch("SAPI.SpVoice")
                speaks.Speak(str)
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1

                print("Time Out!!!")

            if __name__ == '__main__':
                speak("Enter the time in second:")
                t = int(input("Enter the time in second:"))

                countdown(t)
            speak("Time Out")

        elif 'goodbye' in query:
            speak("good bye")
            exit()
