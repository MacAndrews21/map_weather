# -*- coding: utf-8 -*-
#import cv2
import glob
import os
import sys
import gdal
import csv
from gdalconst import *
import postgres as po
import zipfile

 
''' function: delete all ' ' from the file and write the file in an temporary file
    the original file will not be overwritten
    Called in: getStations()
'''
def cleanFile(csv, i):
   
    ''' open file as csv '''
    #csv = open(filePath + fileName, 'r')
    csvRead = csv.read()
    
    ''' replace alls ' ' with '' to clean up the file '''
    txt = csvRead.replace(' ', '')
    
    ''' close file '''
    csv.close()
    
    ''' write the file in an clean temporary file 
        this file will be overwritten by the next file
        => maybe it should be deleted after finish
    '''
    writeFile = open('py/temp_' + str(i) + '.txt','w')
    writeFile.write(txt)
    writeFile.close() 

''' function: read the first line of the file to get the row names
    calls the temporary file
    Called in: getStations()
'''    
def getFirstLine(filePath, fileName):
    
    with open(filePath + fileName, 'rb') as f:
        firstLine = f.readline()
        
        firstLineList = []
        firstLine = firstLine.replace(' ', '')
        
        for index in firstLine.split(';'):
            if len(index) > 1:
                #print index, len(index)
                firstLineList.append(index)
    
    return firstLineList


def readInZIP(folderPath):
    
    zfile = zipfile.ZipFile(folderPath)
    for finfo in zfile.namelist():
        #print finfo[0]
        #print finfo
        if 'Stationsmetadaten' in finfo:
            data = zfile.open(finfo)
            #temp = data.readlines()

            csvRead = data.read()
    
            ''' replace alls ' ' with '' to clean up the file '''
            txt = csvRead.replace(' ', '')
            
            txt_unicode = txt.decode("iso-8859-1")
            
            txt_utf8 = txt_unicode.encode("utf-8")
            
            writeFile = open('data/meta/' + finfo,'w')
            
            writeFile.write(txt_utf8)
            #writeFile.write('hallooooo')
            writeFile.close() 


    
''' function: read row by row data and put into an dictionary 
    Called in: ? 
'''
def getStations(filePath, fileName):
    
    #cleanFile(filePath, fileName)
    
    firstLineList = getFirstLine(filePath, fileName)

    
    with open(filePath + fileName, "rb") as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ';')
        
        rowList = []
        
        for row in reader:
            #print row
            temp = {}
            for i in firstLineList:
                #print i
                temp[i] = row[i]
            
            rowList.append(temp)
           
        #print rowList
        return rowList

''' function: creates a list of all text files in an folder
    except of the ones that do not start with 'Stationsmetadaten'
    Called in: ?
'''
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
        #if 'Stationsmetadaten' in fileName:
        namesDictionary["name"] = fileName
        
        ''' add filename to list '''
        fileNameList.append(namesDictionary)
        
        
    return fileNameList


''' function: creates a list of all folders in an folder
    Called in:?
'''
def createFolderNameList(folderPath):
    
    ''' create emtpy list for folder names '''
    folderNames = []
    
    ''' read all folder names in the folderPath and add it to list folderNames '''
    for name in os.listdir(folderPath):
        folderNames.append(name)
        
    return folderNames

folder = createFolderNameList('data')
#print folder

for z in range(len(folder)):
    if 'zip' in folder[z]:
        #print folder[z]
        readInZIP('data/' + folder[z])

