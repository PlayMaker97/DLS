# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:30:12 2020

@author: Souhail Moutaai
"""

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

# Catégorie ;
categorie_nombres = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE',6 : 'SIX' ,7 :' SEVEN',8:'EIGHT',9:'NINE'}
categorie_alphabet={0: 'A',1: 'B',2:'C',3: 'D' ,4:'E',5:'F',6:'G',7:'I',8:'J',9:'K'}

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
    
    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    result1 = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
   

    prediction= {
'ZERO': result[0][0] , 
                 
                  'ONE': result[0][1], 
                  'TWO': result[0][2],
                  'THREE': result[0][3],
                  'FOUR': result[0][4],
                  'FIVE': result[0][5],
                  'SIX' : result[0][6],
                  'SEVEN' : result[0][7],
                  'EIGHT':result[0][8],
                  'NINE':result[0][9]
                
              
               
                
                  
                  }
    prediction1= {
            
            
            'A': result1[0][0],
                  'B': result1[0][1],
                  'C': result1[0][2],
                  'D' : result1[0][3],
                  'E': result1[0][4],
                  'F'  : result1[0][5],
                  'G' : result1[0][6],
                  'H' :result1[0][7],
                  #on peut ajouter d'autres alphabet
            
            
            }
   
   
   
  

    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    prediction1 = sorted(prediction1.items(), key=operator.itemgetter(1), reverse=True)
   
    if cat == "1" :
       cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
       cv2.imshow("Frame", frame)
       fen1 = tk.Tk()
       fen1.geometry('1000x1300')
       fen1.title("Application: Langue des signes")

   
       img =ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/s6.jpg"))  
       l=tk.Label(image=img)

       l.pack()




       label=tk.Label(fen1,text="                     Hand Detection:                       ",fg="black",bg="white",font="Verdana 32 bold italic")



 
       label2=tk.Label(fen1,text="       Veuillez faire un mouvement et puis cliquer sur le button Detecter ci-dessus:               ",fg="white",bg="black",font="Verdana 15 bold")




       frame=tk.Frame(fen1,background="white")
       frame.config(width=400, height=100)
       img1=ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/han3.jpg")) 
       l1=tk.Label(frame,text="      ",image=img1,bg="white") 
       img2=ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/circle-cropped.png")) 


       bouton=tk.Button(frame,text="clickme",image=img2,height=105,width=750,fg="white",bg="white",command=fen1.destroy,font="Verdana 18 bold",borderwidth=0)
       img3=ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/han1.jpg")) 
       l2=tk.Label(frame,image=img3,bg="white") 






       label3=tk.Label(fen1,text="                                                    Votre Signe Correspond au Signe:                                     ",fg="white",bg="black",font="Verdana 15 bold")
       frame1=tk.Frame(fen1,background="gray")
       frame1.config(width=400, height=100)
       label4=tk.Label(frame1,text="                                                              "+prediction[0][0]+"                                                 ",height=10,fg="red",bg="gray",font="Verdana 25 bold")
       img5 = ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/lol-removebg-preview-removebg-preview (1).png")) 

       l5=tk.Label(frame1,image=img5,bg="gray",fg="gray")
 

       fen1.configure(background="white")
       label.pack()
       #label1.pack()
       #lb.pack() 
       label2.pack()
       frame.pack()
       l2.pack(side="left")
       #l3.pack(side="right") 
       bouton.pack(side="left")
       l1.pack(side="left")

       #l4.pack(side="right")


       frame1.configure(background="gray")
       label3.pack()
       frame1.pack()
       l5.pack(side="left")
       label4.pack(side="right")
       #fen1.resizable(height=False,width=False)
       fen1.mainloop()







       cv2.imshow("Frame", frame)
    if cat == "2" :
       cv2.putText(frame, prediction1[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
       cv2.imshow("Frame", frame)
       fen1 = tk.Tk()
       fen1.geometry('1000x1300')
       fen1.title("Application: Langue des signes")

   
       img =ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/s6.jpg"))  
       l=tk.Label(image=img)

       l.pack()




       label=tk.Label(fen1,text="                     Hand Detection:                       ",fg="black",bg="white",font="Verdana 32 bold italic")



 
       label2=tk.Label(fen1,text="       Veuillez faire un mouvement et puis cliquer sur le button Detecter ci-dessus:               ",fg="white",bg="black",font="Verdana 15 bold")




       frame=tk.Frame(fen1,background="white")
       frame.config(width=400, height=100)
       img1=ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/han3.jpg")) 
       l1=tk.Label(frame,text="      ",image=img1,bg="white") 
       img2=ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/circle-cropped.png")) 


       bouton=tk.Button(frame,text="clickme",image=img2,height=105,width=750,fg="white",bg="white",command=fen1.destroy,font="Verdana 18 bold",borderwidth=0)
       img3=ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/han1.jpg")) 
       l2=tk.Label(frame,image=img3,bg="white") 






       label3=tk.Label(fen1,text="                                                    Votre Signe Correspond au Signe:                                     ",fg="white",bg="black",font="Verdana 15 bold")
       frame1=tk.Frame(fen1,background="gray")
       frame1.config(width=400, height=100)
       label4=tk.Label(frame1,text="                                                                "+prediction1[0][0]+"                                                 ",height=10,fg="red",bg="gray",font="Verdana 25 bold")
       img5 = ImageTk.PhotoImage(Image.open("C:/Users/Souhail Moutaai/Downloads/lol-removebg-preview-removebg-preview (1).png")) 

       l5=tk.Label(frame1,image=img5,bg="gray",fg="gray")
 

       fen1.configure(background="white")
       label.pack()
       #label1.pack()
       #lb.pack() 
       label2.pack()
       frame.pack()
       l2.pack(side="left")
       #l3.pack(side="right") 
       bouton.pack(side="left")
       l1.pack(side="left")

       #l4.pack(side="right")


       frame1.configure(background="gray")
       label3.pack()
       frame1.pack()
       l5.pack(side="left")
       label4.pack(side="right")
       #fen1.resizable(height=False,width=False)
       fen1.mainloop()








       #cv2.imshow("Frame", frame)"""
     
   
       
     
   
    # Displaying the predictions
    #cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.putText(frame, prediction1[0][0], (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.imshow("Frame", frame)
   
    
    
  



    
       
   
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
       break  
cap.release()
cv2.destroyAllWindows()



      
 
