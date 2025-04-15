import os
try:
    os.system('prom.py')
    os.system('routin.py')
    os.system('user_data.py')
except:
    pass
import psutil
import subprocess
import pygetwindow as gw
import pyautogui
import webbrowser
from googletrans import Translator
from datetime import date
import speech_recognition as sr
import pyttsx3
import pyautogui
import time


engine = pyttsx3.init()
engine.setProperty('rate',150)
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer = sr.Recognizer()

try:
    last_date = open('time.txt')
    last_date = last_date.read()
    today = date.today()
    if last_date != today:
        with open('time.txt','w') as file:
            file.write(today)
            file.close
            engine.say('Hi how are you ')
except:
    pass




edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def text_calculator(expression):

  
    result = eval(expression)
    return result


def close_app_by_name(process_name):
    # جستجو در لیست فرآیندها
    for process in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in process.info['name'].lower():  # مطابقت با نام فرآیند
            process_id = process.info['pid']
            psutil.Process(process_id).terminate()  # پایان دادن به فرآیند
            engine.say(f"{process_name} closed!")
            return
    engine.say(f"i didnt find{process_name} ")













while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    
        try:
            command = recognizer.recognize_google(audio, language="en-US")
            text = command
            

            
            if 'the' in text:
                text = text.replace('the','')
            if 'hello' in text:
                engine.say('hi')
            if 'hi' in text:
                engine.say('hi')
            if 'goodbye' in text:
                break
            if 'bye' in text:
                break
            if 'what is your name' in text:
                engine.say('im your freind crase')
            if 'play my song' in text:
                playlist_path = r"C:\Users\shaha\Music\Playlists\my favs.m3u8"
                os.startfile(playlist_path)
            if 'Open' in text:
                from AppOpener import open
                
                if 'fifa' in text:
                    open('FiFa19')
                else:
                    text = text.replace('open','')
                    open(text)
                
            if 'go to' in text:
                webbrowser.get('edge').open_new_tab("https://www.%s.com"%(text))

            if 'close' in text:
                from AppOpener import close
                if 'fifa' in text:
                    close_app_by_name('FiFa19')
                text = text.replace('close','')
                if ' ' in text:
                    text = text.replace(' ','')
                close_app_by_name(text)
            if 'volume down' in text:
                    pyautogui.press("volumedown")
                    time.sleep(0.2)
            if 'volume up':
                    pyautogui.press("volumeup")
                    time.sleep(0.1)
            if 'calculate' in text:
                if 'plus' in text:
                    text = text.replace('plus','+')
                if 'mines' in text:
                    text = text.replcae('mines','-')
                if 'mines' in text:
                    text = text.replcae('mines','-')
                text = text.replace('calculate','')
                expression = text
                engine.say(text_calculator(expression))


          
        except sr.UnknownValueError:
            engine.setProperty('rate', 120)
        except sr.RequestError as e:
            print(f"your call have disconection: {e}")

    engine.runAndWait()        
