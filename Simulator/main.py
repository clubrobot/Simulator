#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from math import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from Elements import *
from Server_utils.Components_virtual import *
from Server_utils.tcptalks import *
from Server_tools import *
from geogebra import *
import random

BLUE = '#3498DB'
RED  = 'red'
WHITE = '#FFF'


def key(event):
    global rob
    global c
    global window
    global simu


    if(event.char =='z'):
        rob.setVelocity(1500,0)
        #c.forward()
    elif(event.char=='s'):
        rob.setVelocity(-500,0)
    elif(event.char=='q'):
        rob.setVelocity(0,1)
    elif(event.char=='d'):
        rob.setVelocity(0,-1)
    elif(event.char ==' '):
        rob.setVelocity(0,0)
    elif(event.char =='i'):
        Thread(target=rob.arduinos[1].grab_left).start()
    elif(event.char == 'o'):
        Thread(target=rob.arduinos[1].grab_center).start()
    elif(event.char == 'p'):
        Thread(target=rob.arduinos[1].grab_right).start()
    elif(event.char == 'l'):
        Thread(target=rob.arduinos[1].drop_tower).start()
    elif(event.char == 'f'):
        rob.fire_ball()






#Paramètre de la fenêtre
window = Tk()
window.title("Simulateur d'IA - Club Robot - INSA Rennes")
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file = os.path.join(os.path.dirname(__file__), 'logo.png')))
window.configure(width=1080,height=1720)
window.resizable(width=False,height=False)
#window.bind("<KeyPress>", key)




#window.geometry("800x533")
style = Style()
style.theme_use("clam")

Canvas = Canvas_area(window,width=800 ,height=533)
Canvas.show()


simu = Simulator(window,Canvas)
servers = ServerManager(simu, None)
simu.core.setMap(( (0,0),(0,3000),(2000,3000), (2000, 2067), (1850,2067), (1850,2089),(2000, 2089), (2000, 1467),(1700, 1467),(1700, 1489),(2000,1489),(2000, 867),(1850, 867), (1850,889), (2000, 889),(2000, 0)))
simu.launch()




#photo = PhotoImage(file="background.png")
Canvas.add_background("background.png")
#Bando option
menuBar = Menu(window)
window['menu'] = menuBar

FichierMenu = Menu(menuBar)
menuBar.add_cascade(label='Fichier')#, menu=FichierMenu)
FichierMenu.add_command(label='Nouveau')
FichierMenu.add_command(label='Ouvrir...')

ServerMenu = Menu(menuBar)
menuBar.add_cascade(label='Serveur')#, menu=ServerMenu)


OutilMenu = Menu(menuBar)
menuBar.add_cascade(label='Outils', menu=OutilMenu)
OutilMenu.add_command(label='Résolution',command=Canvas.update_resolution)
OutilMenu.add_command(label='Préférence connexion')
OutilMenu.add_command(label='Préférence IA')
OutilMenu.add_command(label='Manette')

def coucou():
    global simu
    time.sleep(100)
    score  = simu.getPoints()
    if(score[0]>score[1]):
        message = "Orange Gagne avec {} contre {}".format(*score)
    if(score[0]<score[1]):
        message = "Vert Gagne avec {} contre {}".format(score[1],score[0])
    if(score[0]==score[1]):
        message = "match nul avec {} partout".format(score[0])
    showinfo("RESULTAT", message)




def points():
    Thread(target=coucou).start()


ServerMenu.add_command(label='Lancer')#,command = Server.start)
ServerMenu.add_command(label='Arrêter')#,command = Server.stop)
ServerMenu.add_command(label='Paramètre')#,command = Server.setup)


launch_button = Button(window, text="Start",takefocus=False,command=points)
launch_button.pack(side=LEFT ,padx = 10, pady = 1)

reset = Button(window, text="reset",takefocus=False,command=servers.kick_all)
reset.pack(side=RIGHT ,padx = 10, pady = 1)

speed_scale = tkinter.Scale(window, orient='horizontal', from_=0, to=2,resolution=0.01, tickinterval=1, length=100,label='Speed')
speed_scale.pack(side=BOTTOM, padx = 2, pady = 2)
speed_scale.set(1)

#charge le geogebra
map_source = GeoGebra("map_ressources.ggb")

cup_list = list()
pos_list = list()
for x,y in map_source.getall("Cup_{R"):
    c = Cup(simu,color="red",x=x,y=y)
    cup_list.append(c)
    pos_list += [c.initial_coordinates]

for x,y in map_source.getall("Cup_{G"):
    c = Cup(simu,color="green",x=x,y=y)
    cup_list.append(c)
    pos_list += [c.initial_coordinates]

print(cup_list)
print(pos_list)
def cup_reset():
    global Cube_list
    for cup in cup_list:
        cup.reset()


def reset_all():
    cup_reset()

"""

rob = Robot("dem",simu)
rob.setPosition(1000,1000,0)
"""
servers.bind_reset_function(reset_all)


servers.start()
window.mainloop()
servers.clean()
servers.join()

#remove background-redim
os.remove("background_redim.gif")
