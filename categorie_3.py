# -*- coding: utf-8 -*-

"""Created on Fri Jul 10 03:56:35 2020

@author: Souhail Moutaai"""
import numpy as np
from keras.models import model_from_json
import operator
import cv2
import sys, os
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageSequence
import shutil
import webbrowser


#from tkinter import *
from random import randint
import pygame.mixer
import mimetypes
import  os 

# Loading the model
json_file = open("C:/Users/Souhail Moutaai/Desktop/PFA/model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("C:/Users/Souhail Moutaai/Desktop/PFA/model-bw.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)
categorie3={0: 'fichier_signes', 1: 'Coppier_Fichier',2: 'Creer_Dossier' ,3: 'Jeu',4:'Musique',5:'Ouvrire un Site Web',6:'Video',7:'PDF ou Word',8:'Ecrire Dans un Fichier'}
cat= str(input("Quel est la catégorie que vous voulez prédire? "))
while True:
    _, frame = cap.read()
   
    frame = cv2.flip(frame, 1)
    
  
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
   
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
   
    roi = frame[y1:y2, x1:x2]
    #roi=frame
    

    roi = cv2.resize(roi, (64, 64)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    
   
    result2 = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    prediction2= {
            'fichier_signes' : result2[0][0],
            'Coppier_Fichier': result2[0][1],
            'Creer_Dossier': result2[0][2],
            'Jeu': result2[0][3],
        'Musique': result2[0][4],
        'Ouvrire un Site Web' : result2[0][5],
        'Video' : result2[0][6],
        'Ecrire Dans un Fichier': result2[0][7],
        'PDF ou Word':result2[0][8],
        
                
                
            
            
            }
    
    prediction2 = sorted(prediction2.items(), key=operator.itemgetter(1), reverse=True)
    if prediction2[0][0] == 'Creer_Dossier' :
       dossier = str(input("Quel est le nom du dossier ? "))
       os.mkdir(dossier)
    if prediction2[0][0] == 'Coppier_Fichier' :
       fichier=str(input("DONNER LE NOm du fichier que vous voulez coppier"))
       dos=str(input("donner le dossier destination"))
       filePath = shutil.copy(fichier, dos)
       print(filePath)
       print("Copie du fichier avec succés")
    if prediction2 [0][0]== 'Ouvrire un Site Web' :
       site=str(input("donner le nom du site web"))
       sit=site+".com"
       webbrowser.open(sit)
     
    if prediction2[0][0]== 'Ecrire Dans un Fichier' :
       fichier = open("../data.txt", "a")
       texte=str(input("veuillez ecrire votre phrase"))
       fichier.write("\n"+texte)
       print("votre texte a été ecrit avec succés")
       fichier.close()  
    if prediction2[0][0]== 'Video' :
       vid=str(input("veuillez ecrire le nom de la video")) 
       os.startfile('C:/Users/Souhail Moutaai/Videos/'+vid+'.mp4')
    if prediction2[0][0]== 'PDF ou Word' :
       mimetypes.init()
       mimetypes.knownfiles

       print(os.listdir("C:/Users/Souhail Moutaai/Desktop/Dos"))
       fich=str(input("Veuillez saisir le nom du fichier"))
       char=mimetypes.MimeTypes().guess_type("C:/Users/Souhail Moutaai/"+fich)[0]
       print(char)


       os.startfile("C:/Users/Souhail Moutaai/Downloads/"+fich)

       
    if prediction2[0][0]== 'Musique' :
         
       pygame.mixer.init()
       pygame.mixer.music.load("C:/Users/Souhail Moutaai/Desktop/Ebay/EBAY KINGS -- كيف حققت 15 الف دولار/SUSPEND الدرس الاول تخطي/STORE/Travis Scott - goosebumps ft. Kendrick Lamar.mp3")   # chargement de la musique
       pygame.mixer.music.play()   # la musique est jouée
       stopp=str(input("voulez vous arreter la musique?"))
       if stopp== "oui" :
          pygame.mixer.music.stop()
          break
    
    if prediction2[0][0] == 'Jeu' :
    

       def aligne(grille):
    ###########################################################
    ####    victoire par ligne
          for x in range(3):
              if grille[x][0]==grille[x][1]==grille[x][2]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png" or grille[x][0]==grille[x][1]==grille[x][2]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png":
                can.create_line(0,j,600,j,width=6,fill="black")
                return "un joueur gagne"
        
            
    #############################################################
    ####   victoire par colonne
          for x in range(3):
              if grille[0][x]==grille[1][x]==grille[2][x]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png" or grille[0][x]==grille[1][x]==grille[2][x]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png":
                 can.create_line(i,0,i,600,width=6,fill="black")
                 return "un joueur gagne"
        
            
    #############################################################
    ####    victoire par diagonale
          if grille[0][0]== grille[1][1]== grille[2][2]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png" or grille[0][0]== grille[2][2]== grille[1][1]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png":
             can.create_line(0,0,600,600,width=6,fill="black")
             return "un joueur gagne"
  
      

          elif grille[0][2]== grille[1][1]== grille[2][0]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png" or grille[0][2]== grille[1][1]== grille[2][0]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png":
              can.create_line(600,0,0,600,width=6,fill="black")
              return "un joueur gagne"
        
      
    ##########################################################"
    #### egalite
          if grille[0][0]!=". " and grille[0][1]!=". " and grille[0][2]!=". " and grille[1][0]!=". " and grille[1][1]!=". " and grille[1][2]!=". " and grille[2][0]!=". " and grille[2][1]!=". " and grille[2][2]!=". ":
             return "égalite personne ne gagne cette manche"



       def jeuG():
         global image_joueurs
         global joueurs
         joueur=["C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png","C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png"]
         joueurs=["C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png","C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png"] 
    
    
         global can
         global fen
         for loop in range(randint(0,1)):  #choix aleatoire de qui commence
             joueur.reverse()
         fen=tk.Tk()
    
         can=tk.Canvas(fen , height=600 , width=600 )
         can.pack()
         image_joueurs=[tk.PhotoImage(file=joueur[0]), tk.PhotoImage(file=joueur[1])]
         tracerGrille=tk.Button(fen , text="Tracer la grille" , command=grille)
         tracerGrille.pack()
         quitter=tk.Button(fen, text="Quitter", command=fen.destroy)
         quitter.pack()
    
         fen.mainloop()
         return joueur
  
  
       def grille():
    
        can.delete("all")
        creagrille()
    #ligne
        can.create_line(0,5,600,5, width=10,fill="black")
        can.create_line(0,200,600,200, width=10,fill="black")
        can.create_line(0,400,600,400, width=10,fill="black")
        can.create_line(0,595,600,595, width=10,fill="black")
  
    #colonne
        can.create_line(5,0,5,600, width=10,fill="black")
        can.create_line(200,0,200,600, width=10,fill="black")
        can.create_line(400,0,400,600, width=10,fill="black")
        can.create_line(600,0,600,600, width=10,fill="black")


    
        can.bind("<Button-1>" ,jouer)
   
           
  
       def jouer(event):
           global i
           global j
           i=event.x
           j=event.y
           if  0<=i and i<=199:
               i=100
               k=0
           elif  200<=i and i<=399:
              i=300
              k=1
           elif  400<=i and i<=600:
              i=500
              k=2    
           if 0<=j and j<=199:
              j=90
              z=0
           elif  200<=j and j<=399:
                 j=290
                 z=1
           elif  400<=j and j<=600:
              j=490
              z=2
    
    
           if grille[z][k]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/rond.png" or grille[z][k]=="C:/Users/Souhail Moutaai/Desktop/PFA/morpion/croix.png":
              return jouer
           else:
            grille[z][k]=joueurs[0]
            can.create_image(i,j, image=image_joueurs[0])
           joueurs.reverse()
           image_joueurs.reverse()
           var=aligne(grille)
    
           if var =="un joueur gagne":
              can.create_rectangle(150,245,450,325,fill="black")
              can.create_text(295,285,text="Bravo tu as gagné",font=("Cursive",25),fill="red")
        
           elif var=="égalite personne ne gagne cette manche":
                can.create_rectangle(100,245,500,325,fill="black")
                can.create_text(305,285,text="Egalité personne ne gagne",font=("Cursive",25),fill="red")
         
       def creagrille():
           global grille
           grille=[[". "]*3 for s in range(3)]


    
       jeuG()
    if cat == "3" :
       
       cv2.putText(frame, prediction2[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1) 
       cv2.imshow("Frame", frame)
       interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
       break  
cap.release()
cv2.destroyAllWindows()

