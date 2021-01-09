# -*- coding: utf-8 -*-






"""
Created on Sun Mar 22 19:08:28 2020

@author: Souhail Moutaai"""
import cv2

import os

# Création du dossier pour l"ajout du dataset 

if  os.path.exists("C:/Users/Souhail Moutaai/Desktop/Chatei"):
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/0")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/1")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/2")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/3")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/4")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/5")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/6")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/7")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/8")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/9")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/A")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/B")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/C")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/D")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/E")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/F")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/G")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/H")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/I")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/J")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/K")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/L")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/M")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/N")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/O")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/P")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Q")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/R")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/S")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/T")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/U")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/V")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/W")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/X")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Y")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Z")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Creer_Dossier")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Coppier_Fichier")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Jeu")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Musique")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Ouvrire un Site Web")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Video")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/Ecrire Dans un Fichier")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/PDF ou Word")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/tr/fichier_signes")
                                                                                    
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/0")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/1")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/2")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/3")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/4")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/5")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/6")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/7")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/8")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/9")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/A")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/B")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/C")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/D")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/E")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/F")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/G")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/H")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/I")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/J")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/K")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/L")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/M")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/N")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/O")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/P")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Q")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/R")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/S")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/T")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/U")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/V")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/W")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/X")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Y")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Z")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Creer_Dossier")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Coppier_Fichier")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Jeu")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Musique")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Ouvrire un Site Web")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Video")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/Ecrire Dans un Fichier")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/PDF ou Word")
    os.makedirs("C:/Users/Souhail Moutaai/Desktop/Chatei/test/fichier_signes")
   
    

# Train or test 
mode = 'tr'
directory = 'C:/Users/Souhail Moutaai/Desktop/Chatei/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'six': len(os.listdir(directory+"/6")),
             'seven': len(os.listdir(directory+"/7")),
             'eight': len(os.listdir(directory+"/8")),
             'nine': len(os.listdir(directory+"/9")),
          
             'A': len(os.listdir(directory+"/A")),
             'B': len(os.listdir(directory+"/B")),
             'C': len(os.listdir(directory+"/C")),
             'D': len(os.listdir(directory+"/D")),
             'E': len(os.listdir(directory+"/E")),
             'F': len(os.listdir(directory+"/F")),
             'G': len(os.listdir(directory+"/G")),
             'H': len(os.listdir(directory+"/H")),
             'I': len(os.listdir(directory+"/I")),
             'J': len(os.listdir(directory+"/J")),
             'K': len(os.listdir(directory+"/K")),
             'L': len(os.listdir(directory+"/L")),
             'M': len(os.listdir(directory+"/M")),
             'N': len(os.listdir(directory+"/N")),
             'O': len(os.listdir(directory+"/O")),
             'P': len(os.listdir(directory+"/P")),
             'Q': len(os.listdir(directory+"/Q")),
             'R': len(os.listdir(directory+"/R")),
             'S': len(os.listdir(directory+"/S")),
             'T': len(os.listdir(directory+"/T")),
             'U': len(os.listdir(directory+"/U")),
             'V': len(os.listdir(directory+"/V")),
             'W': len(os.listdir(directory+"/W")),
             'X': len(os.listdir(directory+"/X")),
             'Y': len(os.listdir(directory+"/Y")),
             'Coppier_Fichier': len(os.listdir(directory+"/Coppier_Fichier")),
             'Creer_Dossier': len(os.listdir(directory+"/Creer_Dossier")),
             'Jeu': len(os.listdir(directory+"/Jeu")),
             'Musique': len(os.listdir(directory+"/Musique")),
             'Ouvrire un Site Web': len(os.listdir(directory+"/Ouvrire un Site Web")),
             'Video': len(os.listdir(directory+"/Video")),
             'PDF ou Word': len(os.listdir(directory+"/PDF ou Word")),
             'Ecrire Dans un Fichier ': len(os.listdir(directory+"/Ecrire Dans un Fichier")),
             'fichier_signes': len(os.listdir(directory+"/Z")),
          
             
             }
    
    # Ecriture du nombre d'images de chaque mouvement on peut ajouter les autres mouvements mais on auraient un grande surface d'ecriture sur la caméra
    cv2.putText(frame, "ON : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
   
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64)) 
 
    cv2.imshow("Frame", frame)
    
    
    # Capture des images
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', roi)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', roi)
 
    if    interrupt & 0xFF == ord('A'):
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('B'):
        cv2.imwrite(directory+'B/'+str(count['B'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('C'):
        cv2.imwrite(directory+'C/'+str(count['C'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('D'):
        cv2.imwrite(directory+'D/'+str(count['D'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('E'):
        cv2.imwrite(directory+'E/'+str(count['E'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('F'):
        cv2.imwrite(directory+'F/'+str(count['F'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('G'):
        cv2.imwrite(directory+'G/'+str(count['G'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('H'):
        cv2.imwrite(directory+'H/'+str(count['H'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('I'):
        cv2.imwrite(directory+'I/'+str(count['I'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('J'):
        cv2.imwrite(directory+'J/'+str(count['J'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('K'):
        cv2.imwrite(directory+'K/'+str(count['K'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('L'):
        cv2.imwrite(directory+'L/'+str(count['L'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('M'):
        cv2.imwrite(directory+'M/'+str(count['M'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('N'):
        cv2.imwrite(directory+'N/'+str(count['N'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('O'):
        cv2.imwrite(directory+'O/'+str(count['O'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('P'):
        cv2.imwrite(directory+'P/'+str(count['P'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('Q'):
        cv2.imwrite(directory+'Q/'+str(count['Q'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('R'):
        cv2.imwrite(directory+'R/'+str(count['R'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('S'):
        cv2.imwrite(directory+'S/'+str(count['S'])+'.jpg', roi)
        
    if    interrupt & 0xFF == ord('T'):
        cv2.imwrite(directory+'T/'+str(count['T'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('U'):
        cv2.imwrite(directory+'U/'+str(count['U'])+'.jpg', roi)
       
    if    interrupt & 0xFF == ord('V'):
        cv2.imwrite(directory+'V/'+str(count['V'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('W'):
        cv2.imwrite(directory+'W/'+str(count['W'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('X'):
        cv2.imwrite(directory+'X/'+str(count['X'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('Y'):
        cv2.imwrite(directory+'Y/'+str(count['Y'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('Z'):
        cv2.imwrite(directory+'Z/'+str(count['Z'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('*'):
        cv2.imwrite(directory+'Coppier_Fichier/'+str(count['Coppier_Fichier'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('+'):
        cv2.imwrite(directory+'Creer_Dossier/'+str(count['Creer_Dossier'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('-'):
        cv2.imwrite(directory+'Jeu/'+str(count['Jeu'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('/'):
        cv2.imwrite(directory+'Ouvrire un Site Web/'+str(count['/'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('$'):
        cv2.imwrite(directory+'Video/'+str(count['Video'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('#'):
        cv2.imwrite(directory+'Musique/'+str(count['Musique'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('^'):
        cv2.imwrite(directory+'Ecrire Dans un Fichier/'+str(count['Ecrire Dans un Fichier'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('_'):
        cv2.imwrite(directory+'fichier_signes/'+str(count['fichier_signes'])+'.jpg', roi)
    if    interrupt & 0xFF == ord('('):
        cv2.imwrite(directory+'PDF ou Word/'+str(count['PDF ou Word'])+'.jpg', roi) 
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)   
        """
