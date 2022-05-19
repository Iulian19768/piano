import tkinter as tk
from tkinter import *
from turtle import bgcolor

import pygame


main_window=tk.Tk()

main_window.geometry('1050x500')

main_window.title('piano')

pygame.mixer.init()

def do():
   pygame.mixer.music.load("key01.mp3")
   pygame.mixer.music.play()

def re():
   pygame.mixer.music.load("key02.mp3")
   pygame.mixer.music.play()

def mi():
   pygame.mixer.music.load("key03.mp3")
   pygame.mixer.music.play()




test_button=tk.Button(main_window, height= 20 , width=6, command= do)

test_button.place(x=0,y=190)
t1=tk.Button(main_window,  height= 20 , width=6, command= re)
t1.place(x=52,y=190)
t2=tk.Button(main_window,  height= 20 , width=6, command= mi)
t2.place(x=104,y=190)
t3=tk.Button(main_window,  height= 20 , width=6)
t3.place(x=152,y=190)
t4=tk.Button(main_window,  height= 20 , width=6)
t4.place(x=204,y=190)
t5=tk.Button(main_window,  height= 20 , width=6)
t5.place(x=252,y=190)
t6=tk.Button(main_window,  height= 20 , width=6)
t6.place(x=304,y=190)
t7=tk.Button(main_window,  height= 20 , width=6)
t7.place(x=352,y=190)
t9=tk.Button(main_window,  height= 20 , width=6)
t9.place(x=404,y=190)
t8=tk.Button(main_window,  height= 20 , width=6)
t8.place(x=452,y=190)
t10=tk.Button(main_window, height= 20 , width=6)
t10.place(x=504,y=190)
t11=tk.Button(main_window,  height= 20 , width=6)
t11.place(x=552,y=190)
t12=tk.Button(main_window, height= 20 , width=6)
t12.place(x=604,y=190)
t13=tk.Button(main_window,  height= 20 , width=6)
t13.place(x=652,y=190)
t14=tk.Button(main_window, height= 20 , width=6)
t14.place(x=704,y=190)
t15=tk.Button(main_window,  height= 20 , width=6)
t15.place(x=752,y=190)
t16=tk.Button(main_window, height= 20 , width=6)
t16.place(x=804,y=190)
t17=tk.Button(main_window,  height= 20 , width=6)
t17.place(x=852,y=190)
t18=tk.Button(main_window, height= 20 , width=6)
t18.place(x=904,y=190)
t19=tk.Button(main_window,  height= 20 , width=6)
t19.place(x=952,y=190)
t20=tk.Button(main_window,  height= 20 , width=6)
t20.place(x=1004,y=190)
b1= tk.Button(main_window, bg='black', width=3,height=15)
b1.place(x=36, y=190)
b2= tk.Button(main_window, bg='black', width=3,height=15)
b2.place(x=88, y=190)

b4= tk.Button(main_window, bg='black', width=3,height=15)
b4.place(x=187, y=190)
b5= tk.Button(main_window, bg='black', width=3,height=15)
b5.place(x=237, y=190)
b6= tk.Button(main_window, bg='black', width=3,height=15)
b6.place(x=287, y=190)

b7= tk.Button(main_window, bg='black', width=3,height=15)
b7.place(x=387, y=190)
b9= tk.Button(main_window, bg='black', width=3,height=15)
b9.place(x=437, y=190)

b11= tk.Button(main_window, bg='black', width=3,height=15)
b11.place(x=537, y=190)
b12= tk.Button(main_window, bg='black', width=3,height=15)
b12.place(x=587, y=190)
b13= tk.Button(main_window, bg='black', width=3,height=15)
b13.place(x=637, y=190)

b15= tk.Button(main_window, bg='black', width=3,height=15)
b15.place(x=737, y=190)
b16= tk.Button(main_window, bg='black', width=3,height=15)
b16.place(x=787, y=190)
b17= tk.Button(main_window, bg='black', width=3,height=15)
b17.place(x=887, y=190)
b18= tk.Button(main_window, bg='black', width=3,height=15)
b18.place(x=937, y=190)
b19= tk.Button(main_window, bg='black', width=3,height=15)
b19.place(x=987, y=190)



main_window.mainloop()
