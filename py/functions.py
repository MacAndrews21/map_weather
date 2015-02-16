#import cv2
import glob
import os
import sys
import gdal
import csv
from gdalconst import *
import postgres as po

 
''' function: delete all ' ' from the file and write the file in an temporary file
    the original file will not be overwritten
    Called in: getStations()
'''
def cleanFile(filePath, fileName):
   
    ''' open file as csv '''
    csv = open(filePath + fileName, 'r')
    csvRead = csv.read()
    
    ''' replace alls ' ' with '' to clean up the file '''
    txt = csvRead.replace(' ', '')
    
    ''' close file '''
    csv.close()
    
    ''' write the file in an clean temporary file 
        this file will be overwritten by the next file
        => maybe it should be deleted after finish
    '''
    writeFile = open('py/temp.txt','w')
    writeFile.write(txt)
    writeFile.close() 

''' function: read the first line of the file to get the row names
    calls the temporary file
    Callled in: getStations()
'''    
def getFirstLine():
    
    with open('py/temp.txt', 'rb') as f:
        firstLine = f.readline()
        
        firstLineList = []
        firstLine = firstLine.replace(' ', '')
        
        for index in firstLine.split(';'):
            if len(index) > 1:
                #print index, len(index)
                firstLineList.append(index)
    
    return firstLineList
    
    
def getStations(filePath, fileName):
    
    cleanFile(filePath, fileName)
    
    firstLineList = getFirstLine()

    
    with open('py/temp.txt', "rb") as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ';')
        
        rowList = []
        
        for row in reader:
            #print row
            temp = {}
            for i in firstLineList:
                #print i
                temp[i] = row[i]
            
            rowList.append(temp)
           
        print rowList
 
filePath = 'data/tageswerte_00001_19370101_19860630_hist/'
fileName = 'Stationsmetadaten_klima_stationen_00001_19370101_19860630.txt'
#getStations("py/", "temp.txt")
#getStations(filePath, fileName)


def createFileNameList(folderPath):
    
    ''' create List of file names in folder '''
    fileNameList = []
   
    for fileData in glob.glob(os.path.join(folderPath, '*.txt')):
        ''' create temporary dictionary '''
        namesDictionary = {}
        
        ''' seperate filename '''
        startIndex = fileData.rfind('/') + 1
        fileName = fileData[startIndex:]
   
        
        ''' put fileName into temporary dictionary '''
        if 'Stationsmetadaten' in fileName:
            namesDictionary["name"] = fileName
            
            ''' add filename to list '''
            fileNameList.append(namesDictionary)
        
        
    return fileNameList

fileNameList = createFileNameList(filePath)
print fileNameList