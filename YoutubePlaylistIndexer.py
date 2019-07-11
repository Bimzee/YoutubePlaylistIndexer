import os

## path = 'D:\\Angular2' 
## filePat ="D:\\ag6.txt"

folderPath = 'D:\Venkat\DotnetCore' 
playLstFile ="D:\Venkat\p1.txt"




def initateRename( folderPath, playLstFile ):
   playlstNames =orderdName(playLstFile)
   i=1
   for fileName in playlstNames:
      fileName = fileName+".mp4"
      renameFileNew (folderPath, fileName, str(i) + fileName)
      i=i+1

##youtube-dl -i --get-filename --skip-download https://www.youtube.com/playlist?list=PLm9l7EEbJuhyDYNuItj3sG8h3xAZbjIxr > pl.txt



def renameFileNew (folderPath , fileName , newFileName ):
   path = 'D:\\Angular2'
   files = os.listdir(folderPath)
   if fileName in files:
      os.rename(os.path.join(folderPath , fileName ), os.path.join(folderPath , newFileName ))
   


def orderdName(playLstFile):
   txtFile =open(playLstFile)
   names=[]
   fullName=txtFile.readlines()
   for name in fullName:
      names.append(name.split('.')[0])
   return names
   
initateRename(folderPath,playLstFile)