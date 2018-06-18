import pandas as pd
import math
import numpy as np
from matplotlib import pyplot as plt
from operator import itemgetter, attrgetter
import PyPDF2
import re
import unicodedata
import subprocess
import os, sys

#set new options in pandas so that it won't break up the table to ensure that user sees all available monsters

pd.set_option('display.max_rows', 500)


#read in monster csv file and make all columns into arrays

data = pd.read_csv('D&D_5e_Monster_Manual.csv',header=0)
data = data.fillna('none')
Name = np.array(data['Name'])
AC = np.array(data['AC'])
Type = np.array(data['Type'])
Align = np.array(data['ALIGNMENT'])
HP = np.array(data['HP'])
Size = np.array(data['Size'])
CR = np.array(data['CR'])
Arctic = np.array(data['Arctic'])
Coast = np.array(data['Coast'])
Desert = np.array(data['Desert'])
Forest = np.array(data['Forest'])
Grassland = np.array(data['Grassland'])
Hill = np.array(data['Hill'])
Mountain = np.array(data['Mountain'])
Swamp = np.array(data['Swamp'])
Underdark = np.array(data['Underdark'])
Underwater = np.array(data['Underwater'])
Urban = np.array(data['Urban'])


#ask the user for their players level and terrain in order to establish the highest challenge rating and terrain type for a given foe

level = input("please center your players' current level ")
terrain = input("please enter the current terrain. You may choose from: Arctic, Coast, Desert, Forest, Grassland, Hill, Mountain, Swamp, Underdark, Underwater, or Urban: ")
indices = []

#get the indices of any monsters that match both the challenge rating and the terrain type, then create a matrix of each of those monsters and print to the command line for viewing

for i in range(0, len(CR)):
    if terrain[i] == 'YES' and CR[i] <= level:
        indices.append(i)

matrix = [(Name[i],AC[i],HP[i],CR[i],Type[i],Size[i]) for i in indices]
matrix = sorted(matrix, key=itemgetter(3), reverse=True)
matrix = pd.DataFrame(matrix)
matrix.columns = ['Name','AC','HP','CR','Type','Size']
print matrix

#ask the user for a monster they want more information about

filename = 'Monster_Manual.pdf'
monster = raw_input("for more information about a monster, enter its name here (case sensitive). If not, just write 'no thanks': ")
monster = str(monster)
if monster=='no thanks':
    sys.exit()

#make sure word order agrees with the monster manual regarding ages. (text file and pdf do not agree)

if 'Young' in monster:
    monster = monster.split(',')
    monster = reversed(monster)
    monster = ' '.join(monster)
if 'Adult' in monster:
    monster = monster.split(',')
    monster = reversed(monster)
    monster = ' '.join(monster)
#fix issue with parsing some c's, text reader sees them as e's
if monster == 'Orc':
    monster = 'Ore'
if monster == 'Orc Eye of Gruumsh':
    monster = 'Ore Eye ofGruumsh'
if monster == 'Orc War Chief':
    monster == 'Ore War Chief'
if monster == 'Ice Mephit':
    monster ='lee Mephit'
if monster == 'Ice Devil':
    monster - 'lee Devil'
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

app = pdfReader.getPage(351)#retrieve the index in order to find the monster more quickly
app2 = pdfReader.getPage(352)#the second page of the index
text = app.extractText()+app2.extractText()#extract the text from the full index
text = unicodedata.normalize('NFKD', text).encode('ascii','ignore') #get rid of unicode characters

#find the page that the monster's stats show up on by finding the first number that appears after the name of the monster in the index

x = text.find(monster)
newtext = text[x:x+200]
index = [int(s) for s in newtext.split() if s.isdigit()]
page = index[0]
if monster == 'Veteran':
    page = 350

writer = PyPDF2.PdfFileWriter()
newpage = pdfReader.getPage(page)
writer.addPage(newpage)

#write this out to a file and display it for the user

NewPDFfilename = monster+'.pdf'
with open(NewPDFfilename, "wb") as outputStream: #create new PDF
    writer.write(outputStream) #write pages to new PDF

dirpath = os.getcwd()
opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, NewPDFfilename])

#remove the file so that the user's folder isn't crowded
os.remove(NewPDFfilename)







