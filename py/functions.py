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
import re 


 
''' function: delete all ' ' from the file and write the file in an temporary file
    the original file will not be overwritten
    Called in: getStations()
'''
def cleanFile(finfo, csvRead, folderPath, tempFolder):


    ''' replace alls ' ' with '' to clean up the file '''
    txt = csvRead.replace(' ', '')

    txt_unicode = txt.decode("iso-8859-1")

    txt_utf8 = txt_unicode.encode("utf-8")

    writeFile = open(folderPath + tempFolder + finfo,'w')

    writeFile.write(txt_utf8)
    #writeFile.write('hallooooo')
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


def readInZIP(folderPath, zipFolderPath):
    
    zfile = zipfile.ZipFile(zipFolderPath)
    for finfo in zfile.namelist():
        data = zfile.open(finfo)
        #temp = data.readlines()

        csvRead = data.read()
        #print finfo[0]
        #print finfo
        if 'Stationsmetadaten' in finfo:
            cleanFile(finfo, csvRead, folderPath,'station_metadata/')
        if 'produkt_klima' in finfo:
            cleanFile(finfo, csvRead, folderPath,'temperatur_data/')


    
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

def createTempData(folderPath):
    folder = createFolderNameList(folderPath)
    #print folder

    for z in range(len(folder)):
        if 'zip' in folder[z]:
            #print folder[z]
            readInZIP(folderPath, folderPath + folder[z])
            
''' class: this class is supposed to carry over or replace the functions above
    Called in:?
    Discription: 
'''
class csvZIP(object):
    
    ''' init function 
    '''
    def __init__ (self, zipFolderPath, fileType):
        self.zipFolderPath = zipFolderPath
        self.fileType = fileType

    ''' function: change characters in utf-8 and 
        returns the characters
    '''
    def makeUTF8(self, txt):
        txt = txt.decode("iso-8859-1")
        txt = txt.encode("utf-8")
        return txt
 
    ''' function: get strings in the first line of the csv file and store it in a list and 
        returns the List
    '''
    def getFirstLine(self, firstLine):
        regex = re.compile('[a-z_\?\.]+', re.IGNORECASE)
        #firstLine = firstLine.lower()
        firstLineList = regex.findall(firstLine)
        
        return firstLineList

    ''' function: open zip file and reads all 'fileType' files
        returns from each file the first line as a list and the data as a list of dictionaries.
        first line:     ['row_1', 'row_2']
        data:           [ {'row_1': 'data_1, 'row_2': 'data_1}
                         ,{'row_1': 'data_2, 'row_2': 'data_2}
                         ,{'row_1': 'data_3, 'row_2': 'data_3}
                        ]
    '''        
    def readZIP(self):
        ''' open zip file '''
        zfile = zipfile.ZipFile(self.zipFolderPath)

        ''' dictionary which will be returned '''
        dataDictionary = {}
        
        ''' go through the files in the zip file '''
        for finfo in zfile.namelist():
            
            ''' temporary dictionary to store the first line list '''
            tempList = {}
            
            ''' if-clause to get only files who ends with 'fileType'''
            if self.fileType in finfo:
                
                ''' get the first line of current file '''
                fileData = zfile.open(finfo, 'r')
                firstLine = fileData.readline()              
                fileData.close()
                ''' turn first line in utf-8 '''
                firstLine = self.makeUTF8(firstLine)
                
                ''' create list of strings in the first line of current file;
                    delete all ' ' between the comma seperated values;
                    add firstLineList to temporary dictionary;
                '''
                firstLineList = self.getFirstLine(firstLine)
                tempList['firstLine'] = firstLineList

                ''' open current file as comma seperated file (csv)'''
                with zfile.open(finfo, "r") as csvfile:
                    
                    ''' read csv-file as dictionary '''
                    reader = csv.DictReader(csvfile, delimiter = ';')
                    
                    ''' list of rows or rather columns (see description of this function above )'''
                    dataList = []
                    for row in reader:
                        ''' temporary dictionary to store {'row': 'data'} '''
                        tempDictionary = {}
                        for data in row:
                            ''' turn 'data' in utf-8 '''
                            data = self.makeUTF8(data)
                            for z in firstLineList:                               
                                if z in data:
                                    if row[data]:
                                        xy = row[data]
                                        xy = str(xy).strip()
                                        xy = self.makeUTF8(xy)
                                    else:
                                        xy = 'none'
                                    tempDictionary[z] = xy
                        dataList.append(tempDictionary)       

                tempList['data'] = dataList

                ''' add the temporary dictionary to dataDictionary '''
                dataDictionary[finfo] = tempList
                
                
        return dataDictionary


class readCSV(object):
    
    ''' Klassenattribute'''
    #fileType = 'csv'
    
    ''' Initialisierungsmethode '''
    def __init__(self, csvFileName, fileEnding='csv'):
        self.csvFileName = csvFileName
        self.fileEnding = fileEnding
        
    def __str__(self):
        return "FileName: %s \nFileEnding: %s" % (self.csvFileName,self.fileEnding)
    
c = readCSV("csvFile.csv", fileEnding='txt')

print c        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
