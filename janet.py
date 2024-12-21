import os
from tkinter import *
import sys
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit
import pyautogui
import wikipedia
from settings import *
from playsound import playsound
from PIL import Image
import random
from gtts import gTTS

from PyLyrics import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from googletrans import Translator
import subprocess
translator = Translator()
root=Tk()



opener = "open" if sys.platform == "darwin" else "xdg-open"





root.geometry("1500x750")
root.title('Janet')
if theme == "dark":
    bg2 = "#08121b"
elif theme == "light":
    bg2 = "white"
root.configure(bg=bg2)

root.resizable(0, 0)

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(word):
    if language=="hi-IN":
        wblah=str(translator.translate(word, dest="hi").text)
    if language=="en-IN":
        wblah=word
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)
    randfile = "text/" + f"{r1}" + "randomtext" + f"{r2}" + ".mp3"
    tts = gTTS(text=wblah, lang="hi", slow=False,)
    tts.save(randfile)
    playsound(randfile)
    os.remove(randfile)


if usergender == "Male" or usergender == "male":
    mamsir = "sir"
if usergender == "Female" or usergender == "female":
    mamsir = "mam"


def wishme():
    var.set("How may I help you")
    
    root.update()
    speak("no error in the code found")



def takeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            var.set("Listening...")
            root.update()
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 400
            audio = r.listen(source)
        try:
            var.set("Recognizing...")
            root.update()
            print("Recognizing")
            if language=="hi-IN":

                my_query = r.recognize_google(audio, language="hi-In")
                my_query = str(translator.translate(my_query, dest="en").text)
            if language=="en-IN":

                my_query = r.recognize_google(audio, language="en-In")

            if "!"in my_query:
                my_query.replace("!","")
            if "."in my_query:
                my_query.replace(".","")
            break
        except Exception as e:
            pass
    var1.set(my_query)
    root.update()

    return my_query



def opensettings():
    subprocess.call([opener, "interse.py"])


def openweb(myurl):

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

def bro(my_furl):
    if browser=="qb":
        openweb(my_furl)
    elif browser=="local":
        webbrowser.open(my_furl)
def play():
    btn2['state'] = 'disabled'
    button89['state'] = 'disabled'

    wishme()

    while True:
        button89.configure(bg='orange')


        query=takeCommand().lower()

        try:
            if 'exit' in query:
                var.set("Bye sir")
                button89.configure(bg='#5C85FB')
                btn2['state'] = 'normal'
                button89['state'] = 'normal'
                root.update()
                speak("Bye sir")
                break
            elif "introduce yourself" in query:
                speak("hello there my name is Janet and i am a virtual voice assistant. i can do multiple tasks like set alarms ,schedule messages ,search, etc")
                var.set("hello there my name is Janet and i am a virtual voice assistant. i can do multiple tasks like set alarms ,schedule messages ,search, etc")
                root.update()
            elif 'open youtube' in query:
                var.set('opening Youtube')
                root.update()
                speak('Okay')
                bro("https://www.youtube.com/")

            elif 'open whatsapp' in query:

                webbrowser.open('https://web.whatsapp.com/')
                var.set('opening whatsapp')
                root.update()
                speak(f'ok {mamsir}')
            elif "get lyrics of" in query:
                query=query.replace("get lyrics of","")
                speak(f"sir song {query} by which artist?")
                var.set(f"{mamsir} song {query} by which artist?")
                root.update()
                artist = takeCommand()
                h=PyLyrics.getLyrics(artist,query)
                speak(h)
                var.set(h)
                root.update()

            elif 'open course era' in query or 'open coursera' in query:
                var.set('opening course era')
                root.update()
                speak('opening course era')
                bro("https://www.coursera.org/")

            elif 'open google' in query:
                var.set('opening google')
                root.update()
                speak('opening google')
                bro("https://www.google.co.in/")

            elif 'hello' in query or "hello Janet" in query:
                var.set('hello sir,how may i help you?')
                root.update()
                speak("hello sir,how may i help you?")

            elif 'open stackoverflow' in query:
                var.set('opening stackoverflow')
                root.update()
                speak('opening stackoverflow')
                bro('https://stackoverflow.com')

            elif 'send a whatsapp message' in query:
                speak('to whom you want to send whatsapp message sir?')
                number = takeCommand()
                number = "+91" + number

                speak("what you want to send sir?")
                msg = takeCommand()
                speak("at what hour sir")
                inthour = int(takeCommand())
                speak("and at what minutes sir?")
                inmin = int(takeCommand())
                pywhatkit.sendwhatmsg(number, msg, inthour, inmin, wait_time=31)


            elif 'What\'s the time' in query or "what is the time" in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                var.set("Sir the time is %s" % strtime)
                root.update()
                speak("Sir the time is %s" % strtime)

            elif 'what is today\'s date' in query:
                strdate = datetime.datetime.today().strftime("%d %m %y")
                var.set("Sir today's date is %s" % strdate)
                root.update()
                speak("Sir today's date is %s" % strdate)

            elif 'open instagram' in query:
                var.set("opening instagram")
                root.update()
                speak('opening instagram')
                bro('https://www.instagram.com/')

            elif 'what are you doing' in query:
                var.set("just waiting for your command sir")
                root.update()
                speak("just waiting for your command sir")


            elif 'thank you' in query:
                var.set("Welcome Sir")
                root.update()
                speak("Welcome Sir")
            elif 'open facebook' in query:
                var.set("opening facebook")
                root.update()
                speak('opening facebook')
                bro('https://www.facebook.com/')

            elif 'what can you do for me' in query:
                var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
                root.update()
                speak(
                    'I can do multiple tasks for you sir like open websites , set alarms,search wikipedia,ETC. tell me whatever you want to perform sir')





            elif 'what\'s your name' in query or 'what is your name' in query:
                var.set("Myself Janet Sir")
                root.update()
                speak('myself Janet sir')



            elif 'say hello' in query:
                var.set('Hello Everyone! My self Janet')
                root.update()
                speak('Hello Everyone! My self Janet')




            elif 'open browser' in query:
                var.set("opening browser")
                root.update()
                speak("Opening browser")
                bro("https://www.google.co.in/")


            elif 'open googlemeet' in query or 'open google meet' in query or 'open meet' in query:

                var.set("opening google meet")
                root.update()
                speak("ok sir opening google meet")
                bro('https://meet.google.com/')



            elif ("set alarm" in query):
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
                            if root.event.key == "ENTER":
                                boretimepass = "stop"
                                arushmotu = False


            elif "open chart maker" in query:
                var.set("opening chartmaker")
                root.update()
                speak("opening chartmaker")
                os.startfile("ChartMaker.py")
                button89.configure(bg='#5C85FB')
                btn2['state'] = 'normal'
                button89['state'] = 'normal'
                root.update()
                break

            elif 'bye' in query or "sleep" in query:

                speak("bye sir have a good day")
                root.destroy()
                sys.exit()
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak(f"User asked to Locate {query}")
                lbor=(f"https://www.google.co.in/maps/place/{location}")
                bro(lbor)


            elif 'who are you' in query:

                var.set(
                    f"{mamsir} i am Janet,a voice assistant . {mamsir} i can perform various task like searching anything with wikipedia,open famous websites,set alarm, ETC")
                root.update()

                speak(
                    f"{mamsir}i am Janet ,a voice assistant developed by TEAM_Janet. {mamsir} i can perform various task like searching anything with wikipedia,open famous websites,set alarm, ETC")
            else :
                try:
                    r=wikipedia.summary(query,sentences=2)

                    var.set(r)
                    root.update()
                    speak(r)
                except:
                    pywhatkit.search(query)

        except Exception as e:
            print(e)
def place_my():
    mycan.grid(row=3, column=1, sticky="w", columnspan=5)
    gif_label.grid(row=3, column=6)
    label2.pack(side="right")
    hiscan.grid(row=3, column=7, sticky="e", columnspan=5)
    label1.pack(side="left")
    l.grid(row=1, column=3, sticky="w", padx=5, pady=5,columnspan=2)
    button89.grid(row=4, column=6)
    btn2.grid(row=5, column=6)
    settingsbutton.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    acount.grid(row=1, column=2, sticky="w", padx=5, pady=5)
    gap_label.grid(row=2, column=1)


hiscan = Canvas(root)
mycan = Canvas(root)
if theme == "dark":
    bg3 = "white"
elif theme == "light":
    bg3 = "black"
label2 = Label(hiscan, textvariable=var1, bg=bg2, width=35, height=15, font=("helvetica", 20), fg=bg3, wraplength=380,justify="right")

var1.set('User Said:')

label1 = Label(mycan, textvariable=var, bg=bg2, fg=bg3, width=32, height=15, font=("helvetica", 20), wraplength=380,justify="left")

var.set('Welcome')

file = "lib/janet.gif"
info = Image.open(file)

frames = info.n_frames
im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
if theme == "dark":
    bg1 = "#08121b"
elif theme == "light":
    bg1 = "white"
count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50, lambda: animation(count))


gif_label = Label(root, image="", bg=bg1)

animation(count)

gap_label = Label(root, height=2, bg=bg2,width=2)

photo1 = PhotoImage(file="lib/mic.png")

l = Label(root, text=username, fg=bg3, bg=bg2, border=0, highlightthickness=0, font=("helvetica", 17))

button89 = Button(root, image=photo1, command=play, border=0, highlightthickness=0, bg="#08121b")

btn2 = Button(text='EXIT', width=20, command=sys.exit, bg='#132639', fg="white", border=0, highlightthickness=0)
btn2.config(font=("helvetica", 12))

settingsphoto = PhotoImage(file="lib/mainsettings.png")
settingsbutton = Button(root, image=settingsphoto, command=opensettings, bg=bg2, border=0, highlightthickness=0)

photo = PhotoImage(file="lib/accountimage.png")
acount = Label(image=photo, bg="#08121b", highlightthickness=0, border=0)
place_my()

mainloop()
