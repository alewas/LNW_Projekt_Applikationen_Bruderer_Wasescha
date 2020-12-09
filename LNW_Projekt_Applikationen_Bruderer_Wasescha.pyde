from random import *
#Zufallsgenerator importieren

import math
#Mathematikfunktionen importieren, wird für Modulo gebraucht


primfaktoren = [2,3,5,7,11,13]
#Liste mit möglichen Primfaktoren definieren 

userEingabe = True
k = False
t = True
x = 0
cxPos = 459
cyPos = 981
#Definieren der Variablen

def setup():
    size(1600, 1000)
    
    xPos = 100
    yPos = 100

    global bg
    bg = loadImage("mountain.jpg")


    i = randint(0, 5)
    a = primfaktoren[ i ]
    b = randint(14, 100)
    t = fragen(a,b,xPos,yPos)
#Allgemeines Setup starten

def draw():
    global t
    global x
    global cxPos
    global cyPos
    global userEingabe 
    xPos = 100
    yPos = 100

    
    textSize(64)
    fill(0,139,0)
    strokeWeight(12)
#Setzen aller Parameter und Variablen für den Start des Spiels
#Stroke Weight Umrandung des Kreises
#fill Farbe Text + Kreis

    if x < 7 and userEingabe == True:
    #Spieldurchgänge werden initiiert

    
        if t == k:
            x = x+1
            cxPos = cxPos + 144
            cyPos = cyPos - 114 

        else:
            x = 1
            cxPos = 603
            cyPos = 867
            #Bei einer falschen Antwort wird das Spiel neu gestartet


        
        
        i = randint(0, 5)
        a = primfaktoren[ i ]
        b = randint(14, 100)
        t = fragen(a,b,xPos,yPos)

        userEingabe = False 
    
    elif x == 7:
        background(bg)
        text("Gewonnen! Gib s ein, um neu zu starten.", xPos, yPos)
        if key == "s":
            x = 0
            cxPos = 459
            cyPos = 981
            userEingabe = True
            #Bei Erfolgreichem Spielabschluss (6 richtigen Antworten in Folge), kann das Spiel durch den User neu gestartet werden

    circle(cxPos, cyPos, 60)
    # circle(x-Koordinate, y-Koordinate, Durchmesser) wird dem Spielstand entsprechend gezeichnet

       

def keyPressed():
    global userEingabe
    global k
    userEingabe = True
    if key == "j":
        k = True
    if key == "n":
        k = False
    # Funktion für die Eingabe des Users
    
def fragen(a,b,xPos,yPos):
    background(bg)   
    text("Ist " + str(a) + " Primfaktor von " + str(b) + "? J/N", xPos, yPos)
    
    if (b % a) == 0:
        t = True
    else:
        t = False
    return(t)
    #Stellen der Frage und Lösung durch das Programm
