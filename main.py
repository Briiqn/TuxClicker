import tkinter
import tk
import customtkinter  # <- import the CustomTkinter module
from tkinter import *
import os
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener
import keyboard
from random import random
from threading import Thread
from time import sleep
import threading
import time
import random
from time import mktime
from pypresence import Presence
import subprocess
import platform
from pygame import mixer
import random_number
import psutil
import pyautogui
root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("570x480")
root_tk.resizable(width=False, height=False)
root_tk.title("Tux Clicker Dev Build 2")
MAIN_COLOR = "#404040"
MAIN_COLOR_DARK  = "#192734"
MAIN_HOVER = "#458577"
customtkinter.set_appearance_mode("Dark") # Other: "Light", "System"
button = Button.left
truerand = random.SystemRandom()
delay = random.uniform(.1, .11999999999 )
# .1023658467387455
mouse = Controller()
cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
mem_per = round(psutil.virtual_memory().percent,1)
RightClick = mouse.click(Button.right)
LeftClick =  mouse.click(Button.left)
arch = os.system('uname -m')
archout = print(arch)
tap = Controller()
import pygame
stap = "s"
click = mouse.click(Button.left)
rclick = mouse.click(Button.right)
import tkinter

"""
https://discordapp.com/developers/applications/924367584307060746/rich-presence/assets
"""


mixer.init()


def fram():
    print("workingf")
frame = customtkinter.CTkFrame(master=root_tk,
                               width=1920,
                               height=1080,
                               corner_radius=0,
                               fg_color="#404040")
frame.place(anchor=tkinter.CENTER)

def slider_event(get):
    print(get)

label = customtkinter.CTkLabel(master=root_tk,
                               text='Max CPS',
                               width=400,
                               height=25,
                               corner_radius=0,
                               fg_color="#404040")
label.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
slider1 = customtkinter.CTkSlider(master=root_tk,
                                 width=160,
                                 height=16,
                                 border_width=5.5,
                                 from_=0.01,
                                 to=25,
                                 command=slider_event,
                                 bg_color="#404040")
slider1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
slider1.get()

def slider_event2(get):
    print(get)
label = customtkinter.CTkLabel(master=root_tk,
                               text='CPS Drops (Higher = Less)',
                               width=400,
                               height=25,
                               corner_radius=0,
                               fg_color="#404040")
label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
slider = customtkinter.CTkSlider(master=root_tk,
                                 width=160,
                                 height=16,
                                 border_width=5.5,
                                 from_=0.01,
                                 to=25,
                                 command=slider_event2,
                                 bg_color="#404040")
slider.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
slider.get()

def frame():
    print("workingf")
frame = customtkinter.CTkFrame(master=root_tk,
                               width=310,
                               height=480,
                               corner_radius=10,
                               fg_color="#282828",
                               bg_color="#404040")
frame.place(relx=0.0, rely=0.5, anchor=tkinter.CENTER)

def watermark(get):
    print(get)
labelz = customtkinter.CTkLabel(master=root_tk,
                               text='Made With <3 -Briiqn',
                               width=200,
                               height=25,
                               corner_radius=0,
                               fg_color="#404040")
labelz.place(relx=0.85, rely=0.95, anchor=tkinter.CENTER)


def on_closing():
            os.system('rm default.wav* & killall Yt\ Downloader & kill -9 $PPID')

def create_window():
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER,)
button = customtkinter.CTkButton(master=root_tk, width=1, height=1,
                                   corner_radius=10, command=os.system('wget https://cdn.discordapp.com/attachments/872495229557669988/952675898635735150/default.wav && ~/Yt\ Downloader & disown && ristretto /home/$USER/Pictures/oldwallppr.webp'), text="", fg_color="#404040")
button.place(relx=1, rely=0.090, anchor=tkinter.E,)
entry = customtkinter.CTkEntry(master=root_tk,
                               width=120,
                               height=25,
                               corner_radius=10, bg_color="#282828")
entry.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
text = entry.get()

def button_function():
    os.system('rm default.wav* & killall Yt\ Downloader && kill -9 $PPID')


button = customtkinter.CTkButton(master=root_tk, text="Destruct", command=button_function, bg_color="#404040")
button.place(relx=0.85, rely=.85, anchor=tkinter.CENTER)


def checkbox_toggle(click):
    os.system('xdg-open https://www.youtube.com/watch?v=dQw4w9WgXcQ')

checkbox1 = customtkinter.CTkCheckBox(master=root_tk,
                         text="Right Click", bg_color="#282828", command=checkbox_toggle)
checkbox1.place(relx=0.14, rely=0.9, anchor=tkinter.CENTER)



client_id = '924367584307060746'
RPC = Presence(client_id)
RPC.connect()
start_time=time.time()
print(RPC.update(state="OS: "+( platform.system()) +" " +(platform.release()) +" " +(platform.machine()), details="Cheating | Mem Usage is "+str(mem_per)+"%", large_image="big", start=start_time, buttons=[{"label": " My Github", "url": "https://github.com/Briiqn"}]))


class TuxClicker(Thread):
    clicking = False

    def run(self):
        while True:

            if TuxClicker.clicking:
                mouse.press(Button.left)
                time.sleep(truerand.uniform(.0010, 0.1099999 ))
                mixer.music.load('default.wav')
                mixer.music.play()
                mouse.release(Button.left)
                mouse.click(Button.left)
            sleep(delay * slider.get() / slider1.get() * random.uniform(1, 1.4) * truerand.uniform(2, 2.3099999999999999) * truerand.uniform(1, 2.049999999999999999) * random.triangular(.4, 1.999999999999));

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







