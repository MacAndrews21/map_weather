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
    
    def __init__ (self, zipFolderPath, fileType):
        self.zipFolderPath = zipFolderPath
        #self.readZIP()
    #def test(self):
        #t = self.zipFolderPath + 'XYT'
        
        #return t
        
    ''' function: this function change all string in utf-8
    '''
    def makeUTF8(self, txt):
        txt = txt.decode("iso-8859-1")
        txt = txt.encode("utf-8")
        return txt
        
    def getFirstLine(self, firstLine):
        regex = re.compile('[a-z_\?\.]+', re.IGNORECASE)
        #firstLine = firstLine.lower()
        firstLineList = regex.findall(firstLine)
        
        return firstLineList
        
    def readZIP(self):
        zfile = zipfile.ZipFile(self.zipFolderPath)

        dataDictionary = {}
        
        for finfo in zfile.namelist():
            #temp = data.readlines()
            temp = {}
            if fileType in finfo:
                ''' get the first line of the file '''
                fileData = zfile.open(finfo, 'r')
                firstLine = fileData.readline()
                data = fileData.readlines()
                #reader = csv.DictReader(fileData, delimiter = ';')
                fileData.close()
                
                firstLine = self.makeUTF8(firstLine)
                
                ''' delete all ' ' between the comma seperated values;  fvl = first line values'''
                firstLineList = self.getFirstLine(firstLine)
                temp['firstLine'] = firstLineList


                with zfile.open(finfo, "r") as csvfile:
                    
                    reader = csv.DictReader(csvfile, delimiter = ';')
                    
                    rowList = []
                    for row in reader:
                        temptemp = {}
                        for i in row:
                            i = self.makeUTF8(i)
                            for z in firstLineList:
                                
                                if z in i:
                                    if row[i]:
                                        xy = row[i]
                                        
                                        #xy = re.sub('^[ {1,}\d+]', '', xy)
                                        xy = re.sub(' {2,}', '', xy)
                                        xy = self.makeUTF8(xy)
                                        #xy = row[i]
                                    else:
                                        xy = 'none'
                                    temptemp[z] = xy
                        rowList.append(temptemp)       

                temp['data'] = rowList

                ''' add the temporary dictionary to dataDictionary '''
                dataDictionary[finfo] = temp
                
                
        return dataDictionary
        #return test
        
        
        

        
fileType = 'txt'
m = csvZIP('data/recent/tageswerte_KL_13711_akt.zip', fileType) 
#m = csvZIP('data/recent/tageswerte_KL_03513_akt.zip', fileType) 

test = m.readZIP()
#print test
#print len(test)
#print test['Stationsmetadaten_klima_stationen_13711_20131005_20150216.txt']
for key in test:
    if 'meta' in key:
        print test[key]['firstLine']
        #l = len(test[key]['data'])
        #print len(test[key]['data'])
        #for index in range(len(test[key]['data'])):
            #print test[key]['data'][index][']
        print test[key]['data'][0]
        #print test[key]['data'][2]
        #print test[key]['data'][3]
    
        
        #for row in readerX:
            #print row

#print test['Stationsmetadaten_klima_stationen_13711_20131005_20150216.txt']['firstLine']

#test = m.getFirstLine()

#x = test[7]
#x = x.decode("iso-8859-1")
#x = x.encode("utf-8")
#print x

#print len(test)
        

#readInZIP('../data/recent/temp', 'data/recent/tageswerte_KL_13711_akt.zip')   

#createTempData('data/recent/')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
