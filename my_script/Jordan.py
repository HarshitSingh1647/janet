import pyttsx3
import os
import speech_recognition as sr
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from scripts import chartmaker as ch
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image
try:
    from last1query import lastquery
except Exception as noquer:
    print("hi")
try:
    from settings import * 
except Exception as nosettings:
    sys.exit()


    



window = Tk()
window.geometry("1300x700")
global var
global var1
global languagejordan
global talkorchat
global whichvoice
whichvoice = voice
talkorchat = chattalk
languagejordan = languagejors




var = StringVar()
var1 = StringVar()
def speakerror(texterror,voiceid):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voiceid].id)
    engine.say(texterror)
    engine.runAndWait()

def speak(audio):
    if talkorchat == "chat":
        var.set(audio)
        window.update()
        time.sleep(2)
    if talkorchat == "talk" and whichvoice == "pyttsf":
        speakerror(audio,1)
    elif talkorchat == "talk" and whichvoice == "pyttsxm":
        speakerror(audio,0)
    elif talkorchat == "talk" and whichvoice == "gttsf":
        r1 = random.randint(1, 10000000)
        r2 = random.randint(1, 10000000)
        randfile = "text\ "+str(r2) + "randomtext" + str(r1) + ".mp3"
        tts = gTTS(text=audio, lang="en-IN", slow=False)
        tts.save(randfile)
        playsound(randfile)
        os.remove(randfile)
    else:
        sys.exit()


def offlinescreen():
    
    gif_label.pack_forget()

    label1.pack_forget()

    l.pack_forget()
    l.place_forget()
    button89.pack_forget()
    button89.place_forget()
    btn2.pack_forget()
    btn2.place_forget()
    settingsbutton.pack_forget()
    settingsbutton.place_forget()
    acount.pack_forget()
    acount.place_forget()
    gamebtn.pack_forget()
    gamebtn.place_forget()





try:
    import pywhatkit
    from gtts import gTTS
except Exception as ooointer:
    speakerror("coudn\'t conect please check your internet connection",0)
    speakerror("make sure your computer is connected to any wifi or modem",0)
    offlinescreen()

import random

import json
import datetime

import wikipedia
import webbrowser

import roman
import pyautogui
import wolframalpha

from playsound import playsound
from urllib.request import urlopen
import urllib

numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}





if usergender == "Male" or usergender == "male":
    mamsir = "sir"
if usergender == "Female" or usergender == "female":
    mamsir = "mam"


def wishme():
    speak(f"hello {mamsir} how may i help you?")


def takeCommand():



    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language="en-IN")


    except Exception as exeblah:
        query=takeCommand().lower()

    var1.set(query)
    window.update()

    return query

    

def opensettings():
    os.startfile("interse.py")


def games():
    gamebtn['state'] = 'disabled'

    speak("which game would you like to play?  FlappyBird  chessgame or snake game")
    whichgame = takeCommand().lower()
    if whichgame == "flappy bird" or whichgame == "flappybird":
        os.startfile("games/flappy/FlappyBird.exe")
    if whichgame == "chessgame" or whichgame == "chess game":
        os.startfile("./games/chess/MasterChess.exe")
    if whichgame == "snakegame" or whichgame == "snake game":
        os.startfile("games/snake/SnakeGame.exe")


def openweb(myurl):
    if defaultbrowser == "qweb":
        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl(myurl))
                self.setCentralWidget(self.browser)
                self.showMaximized()
                navbar = QToolBar()
                self.addToolBar(navbar)

                back_btn = QAction('Back', self)
                back_btn.triggered.connect(self.browser.back)
                navbar.addAction(back_btn)

                forward_btn = QAction('Forward', self)
                forward_btn.triggered.connect(self.browser.forward)
                navbar.addAction(forward_btn)

                reload_btn = QAction('Reload', self)
                reload_btn.triggered.connect(self.browser.reload)
                navbar.addAction(reload_btn)

                home_btn = QAction('Home', self)
                home_btn.triggered.connect(self.navigate_home)
                navbar.addAction(home_btn)
                self.url_bar = QLineEdit()

                self.url_bar.returnPressed.connect(self.navigate_to_url)
                navbar.addWidget(self.url_bar)

                self.browser.urlChanged.connect(self.update_url)

            def navigate_home(self):
                self.browser.setUrl(QUrl('https://www.google.com/'))

            def navigate_to_url(self):
                url = self.url_bar.text()
                self.browser.setUrl(QUrl(url))

            def update_url(self, q):
                self.url_bar.setText(q.toString())

        app = QApplication(sys.argv)
        QApplication.setApplicationName('Qweb')
        browserwin = MainWindow()
        app.exec_()


    else:

        webbrowser.open(myurl)


def play():
    btn2['state'] = 'disabled'
    button89['state'] = 'disabled'



    wishme()
    while True:
        query = takeCommand().lower()
        with open("last1query.py","w") as querywrite:
            querywrite.write(f"lastquery = \'{query}\'")
        if "pardon" in query:
            query = lastquery
            
        if "jordan" in query:
            query=query.replace("jordan","")
            needmorerules=True

        if "hey jordan" in query:
            query=query.replace("hey jordan","")
            needmorerules=True
        if "ok jordan" in query:
            query=query.replace("ok jordan","")
            needmorerules=True

        if 'search' in query:
            query = query.replace("search","")
            speak("searching")
            try:

                client = wolframalpha.Client("EHJKX5-5QREEVWWT8")
                res = client.query(query)
                ans = next(res.results).text
                print(ans)
                speak(ans)
            except Exception as failserch:

                speak("retrying")
                try:

                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
                except Exception as blahexcept:
                    try:
                        webbrowser.open('https://google.com/?#q='+query)
                    except:
                        print("It is weird but I got nothing try re-running the program")
                        speak("It is weird but I got nothing try re-running the program")
            needmorerules=False
        else:
            needmorerules=True
            print("")
        button89.configure(bg='orange')

        if needmorerules == True:




            if 'exit' == query:
                var.set("Bye sir")
                button89.configure(bg='#5C85FB')
                btn2['state'] = 'normal'
                button89['state'] = 'normal'
                window.update()
                speak("Bye sir")
                break

            elif 'open youtube' == query:
                var.set('opening Youtube')
                window.update()
                speak('opening Youtube')
                openweb("https://www.youtube.com/")

            if 'open whatsapp' == query:

                openweb('https://web.whatsapp.com/')
                speak('opening whatsapp sir')
                var.set('opening whatsapp')
                window.update()


            elif 'open course era' == query or 'open coursera' == query:
                var.set('opening course era')
                window.update()
                speak('opening course era')
                openweb("https://www.coursera.org/")

            elif 'open google' == query:
                var.set('opening google')
                window.update()
                speak('opening google')
                openweb("https://www.google.co.in/")

            elif 'hello' == query or "hello sam" == query:
                var.set('hello sir,how may i help you?')
                window.update()
                speak("hello sir,how may i help you?")

            elif 'open stackoverflow' == query:
                var.set('opening stackoverflow')
                window.update()
                speak('opening stackoverflow')
                openweb('https://stackoverflow.com')
            elif 'take screenshot' == query:
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save("./scripts/try.png")

            elif 'send a whatsapp message' == query:
                speak('to whom you want to send whatsapp message sir?')
                number = takeCommand()
                number = "+91" + number
                speak("what you want to send sir?")
                msg = takeCommand()
                speak("at what hour sir")
                inthour = int(takeCommand())
                speak("and at what minutes sir?")
                inmin = int(takeCommand())
                pywhatkit.sendwhatmsg(number, msg, inthour, inmin)
                pyautogui.press('enter')

            elif 'What\'s the time' == query or "what is the time" == query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                var.set("Sir the time is %s" % strtime)
                window.update()
                speak("Sir the time is %s" % strtime)

            elif 'what is today\'s date' == query:
                strdate = datetime.datetime.today().strftime("%d %m %y")
                var.set("Sir today's date is %s" % strdate)
                window.update()
                speak("Sir today's date is %s" % strdate)
            if 'open instagram' in query:
                var.set("opening instagram")
                window.update()
                speak('opening instagram')
                openweb('https://www.instagram.com/')

            elif 'what are you doing' == query:
                var.set("just waiting for your command sir")
                window.update()
                speak("just waiting for your command sir")


            elif 'thank you' == query:
                var.set("Welcome Sir")
                window.update()
                speak("Welcome Sir")
            elif 'open facebook' == query:
                var.set("opening facebook")
                window.update()
                speak('opening facebook')
                openweb('https://www.facebook.com/')
            elif 'what can you do for me' == query:
                var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
                window.update()
                speak(
                    'I can do multiple tasks for you sir like open websites , set alarms,search wikipedia,ETC. tell me whatever you want to perform sir')

            elif 'How old are you' == query:
                var.set("sir i am nearly of 3 days")
                window.update()
                speak("sir i am nearly of 3 days")



            elif 'what\'s your name' == query or 'what is your name' == query:
                var.set("Myself erico Sir")
                window.update()
                speak('myself erio sir')

            elif 'who created you' == query:
                var.set('My Creator is sir Team_erico')
                window.update()
                speak('My Creator is Team Erico')

            elif 'say hello' == query:
                var.set('Hello Everyone! My self Erico')
                window.update()
                speak('Hello Everyone! My self Erico')


            elif 'open browser' == query:
                var.set("Opening browser")
                window.update()
                speak("Opening browser")
                try:
                    os.startfile(chromepath)
                except:
                    try:
                    
                        webbrowser.open("https://google.com")
                    except:
                        speak("sir for better results set system or other installed browser as default browser")
                        var.set("sir for better results set system or other installed browser as default browser")
            elif 'open googlemeet' == query or 'open google meet' == query or 'open meet' == query:

                var.set("opening google meet")
                window.update()
                speak("ok sir opening google meet")
                openweb('https://meet.google.com/')

            if ("set alarm" == query):
                speak("at what Hour you want the alarm to ring")
                alarmh = int(takeCommand())
                speak("and at what minutes sir?")
                alarmin = int(takeCommand())

                arushmotu = True
                while arushmotu == True:
                    if (alarmh == int(datetime.datetime.today().strftime("%H")) and alarmin == int(
                            datetime.datetime.today().strftime("%M"))):
                        boretimepass = "hi"
                        while boretimepass == "hi":
                            print("alarm")
                            playsound('lib/alarm.mp3')
                            oo23 = Text(window, text="stop alarm? ( y / n )")
                            oo23.pack()
                            if (oo23 == "y"):
                                arushmotu = False
            if "open q web" == query or "open qweb" == query:

                    os.startfile("browser.py")

            if 'bye' == query or "sleep" == query:

                speak("bye sir have a good day")
                sys.exit()

            elif "where is" == query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                openweb("https://www.google.co.in/maps/place/" + location + "")


            if 'who are you' == query:

                var.set(''' sir i am Jordan,a voice assistant developed by Q Bot.
                    Sir i can perform various task like searching anything with wikipedia,
                                open famous websites,set alarm, ETC''')
                window.update()

                speak(
                    " sir i am jordan ,a voice assistant developed by Q BOT. Sir i can perform various task like searching anything with wikipedia,open famous websites,set alarm, ETC")
            else:
                print("hi")


def mainwindow():
    label2.pack()
    
    gif_label.pack()

    animation(count)
    label1.pack()

    l.pack()
    l.place(x=1100, y=0)
    button89.pack()
    button89.place(x=670, y=600)
    btn2.pack()
    btn2.place(x=607, y=640)
    settingsbutton.pack()
    settingsbutton.place(x=1230, y=0)
    acount.pack()
    acount.place(x=1050, y=0)
    gamebtn.pack()
    gamebtn.place(x=630, y=600)
    gamebtn['state'] = 'normal'


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Calibri", 20))
var.set('Welcome')


def exitjordan():
    speak("ok bye sir,have a nice day")
    window.destroy()


file = "lib/jordantry.gif"
info = Image.open(file)

frames = info.n_frames
im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = window.after(50, lambda: animation(count))


gif_label = Label(window, image="",bg=backgroundcolour)

window.title('Jordan')



photo1 = PhotoImage(file="lib/mic.png")
l = Label(window, text=username)
l.config(font=("Calibri", 14))

button89 = Button(window, image=photo1, command=play)

btn2 = Button(text='EXIT', width=20, command=exitjordan, bg='#5C85FB')
btn2.config(font=("Calibri", 12))

settingsphoto = PhotoImage(file="lib/mainsettings.png")
settingsbutton = Button(window, image=settingsphoto, command=opensettings)
gifcanvas= Canvas(window,width=460,height=461)
photo = PhotoImage(file="lib/accountimage.png")
acount = Label(image=photo)

gamefile = PhotoImage(file="lib/gamefile.png")
gamebtn = Button(window, image=gamefile, command=games)
window.configure(bg=backgroundcolour)
mainwindow()

mainloop()
