import pyttsx3 as p
import speech_recognition as sr
import webbrowser
import time
import os
import random
import randfacts
import wikipedia
import yagmail
from gtts import gTTS
from time import ctime
from news import *
from jokes import *

engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 180)
v =engine.getProperty('voices')
engine.setProperty('voice',v[2].id)

def spr(data):
    engine.say(data)
    engine.runAndWait()

r = sr.Recognizer()
spr("Hello, I'm your voice assistant!")

def myVoice(ask = False):
    with sr.Microphone() as source:
        if ask:
              spr(ask)
        r.adjust_for_ambient_noise(source)
        print("Listening..")
        audio = r.listen(source)
        data = ''
        data = r.recognize_google(audio)
        print(data)
        return data

def yourAnswer(data):
    if 'what is your name' in data:
        spr('My name is Zoya!')
        print('My name is Zoya!')

    if 'what time is it' in data:
        spr(ctime())
        print(ctime())

    if 'search' in data:
        search = myVoice('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        spr('Here is what i found for ' + search)

    if 'temperature' in data:
        climate = myVoice('Which city you want to know its weather?')
        url = 'https://www.google.com/search?q=google+weather' + climate
        webbrowser.get().open(url)
        spr('Here is the weather of' + climate)
    
    if 'Wikipedia' in data:
        w = myVoice('What do you want to search for on Wikipedia ')
        url = 'https://wikipedia.org/w?q=' + w
        webbrowser.get().open(url)
        spr('Here is what i found for ' + w)
    
    if 'find location' in data:
        location = myVoice('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        spr('Here is the location of ' + location)
    
            
    if 'send email' in data:
        reciever = input("Enter the receiver's email: ")
        message = myVoice("What is the message you want to send: ")
        sender = yagmail.SMTP('manalsoufi67@gmail.com')
        sender.send(to=reciever,subject='This is an automated mail',contents=message)
        spr('Your email is been sent successfully')
       
    if 'news' in data:
        print("Sure, I will read news for you now!")
        spr("Sure, I will read news for you now!")
        arr=news()
        for i in range(len(arr)):
            spr(arr[i])
            print(arr[i])

    if 'fact' in data:
        x=randfacts.getFact()
        print(x)
        spr("Did you know that, "+x)

    if 'joke' in data:
        spr("Sure! I will tell you a joke")
        arr=joke()
        print(arr[0])
        spr(arr[0])
        print(arr[1])
        spr(arr[1])

    if 'exit' in data:
        exit()

if __name__ == '__main__':
    spr("what can i do for you?")
    time.sleep(0.1)
    while 0.1:
        data = myVoice()
        yourAnswer(data)