# JARVIS-Desktop-assistance
#It is my personal Desktop assistance like Google alexa
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib   #for sending emails

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning mp')
    elif hour >= 12 and hour <18:
        speak('Good afternoon mp!')
    else:
        speak('Good evening mp')
    speak('hi mp i am Jarvis. Please tell me how may i help you')


def takeCommond():
    # it takes microphone input from user and return dtring output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user="mppatil0103@gmail.com", password="milind@0103")
    server.sendmail('mppatil0103@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommond().lower()
        if 'wikipedia' in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open whatsapp web' in query:
            webbrowser.open("whatsapp web.com")

        elif 'open google' in query:
            webbrowser.open("codewithharry.com")


        elif 'play music' in query:
            music_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25]
            choice = random.choice(music_lst)
            music_dir = 'E:\\music\\my_music'  # here use \\ for escaping character
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[choice]))

        elif 'whats the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"MP,the time is {strtime}")
            print(strtime)

        elif 'open vs code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open pycharm' in query:
            codepath1 = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(codepath1)

        elif 'email to mp' in query:
            try:
                speak("what should i say?")
                content = takeCommond()
                to = "mppatil1106@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry MP! I am not able to send this email")


