#Python 3.5.2
#Note Keeper v1 by Kolt Racer

import os

#Creates a new file or open existing one
file = open('NOTES.txt','a')   


#Reads contents of NOTES.txt
file=open ('NOTES.txt')
print(file.read())


#Stores input to be written
note=input()


#Opens the file again and stores the text in NOTES.txt
file = open('NOTES.txt','a')
file.write("\n" + note + "\n")
file.close()
os.system('exit')
