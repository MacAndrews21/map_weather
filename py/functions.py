#import cv2
import glob
import os
import sys
import gdal
import csv
from gdalconst import *
import postgres as po

##metaData = os.popen('gdalinfo -stats -nomd -norat -noct -nofl ' + filePath + fileName)
#def getResolution (filePath, fileName):
    #dataset = gdal.Open(filePath + fileName, GA_ReadOnly)
    #width = dataset.RasterXSize
    #height = dataset.RasterYSize
    ##print 'Projection:', dataset.GetProjection()
    
    #geotrans = dataset.GetGeoTransform()
    #if not geotrans is None:
        #pixelSize = geotrans[1]
    
    #return width, height, pixelSize

def getStations(filePath, fileName):
    
    #csv = open(filePath + fileName, 'r')
    #csvRead = csv.read()
    #txt = csvRead.replace(' ', '')
    #print txt
    #csv.close()
    
    #temp = open('py/temp.txt','w')
    #temp.write(txt)
    #temp.close()

    with open('py/temp.txt', "rb") as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ';')
        #print 'READER:', reader
        rowList = []
        a = 0
        for row in reader:
            temp = {}
            temp['Stations_id'] = row['Stations_id']
            temp['Stationshoehe'] = row['Stationshoehe']
            temp['Geogr.Breite']  = row['Geogr.Breite'] 
            temp['Geogr.Laenge']  = row['Geogr.Laenge'] 
            temp['von_datum'] = row['von_datum']
            temp['bis_datum'] = row['bis_datum']
            temp['Stationsname']  = row['Stationsname'] 
            
            rowList.append(temp)
            #rowList.append(row)
        print rowList
 
  
getStations("/home/andie/Dropbox/Anita_Andreas/2015 Wetterkarte/tageswerte_00001_19370101_19860630_hist/", "Stationsmetadaten_klima_stationen_00001_19370101_19860630.txt")

Stations_ID; 
Mess_Datum; 
Qualitaets_Niveau; 
LUFTTEMPERATUR;
DAMPFDRUCK;
BEDECKUNGSGRAD;
LUFTDRUCK_STATIONSHOEHE;
REL_FEUCHTE; 
WINDGESCHWINDIGKEIT; 
LUFTTEMPERATUR_MAXIMUM;
LUFTTEMPERATUR_MINIMUM;
LUFTTEMP_AM_ERDB_MINIMUM; 
WINDSPITZE_MAXIMUM; 
NIEDERSCHLAGSHOEHE;
NIEDERSCHLAGSHOEHE_IND;
SONNENSCHEINDAUER; 
SCHNEEHOEHE;
eor





#def createFileNameList(folderPath):
    
    #''' create List of file names in folder '''
    #fileNameList = []
    
    
    
    #for fileData in glob.glob(os.path.join(folderPath, '*.txt')):
        #''' create temporary dictionary '''
        #namesDictionary = {}
        
        #''' seperate filename '''
        #startIndex = fileData.rfind('/') + 1
        #fileName = fileData[startIndex:]
        ##print fileName
        
        #width, height, pixelSize = getResolution(folderPath, fileName)

        
        #''' get kb id '''        
        #kb = fileName[:4]
        
        #''' get kb year '''        
        #end = fileName.rfind('.')
        #year = fileName[5:end]
        
        #''' put fileName, id and year into temporary dictionary '''
        #namesDictionary["name"] = fileName
        #namesDictionary["id"] = kb
        #namesDictionary["year"] = year
        #namesDictionary["width"] = width
        #namesDictionary["height"] = height
        #namesDictionary["pixelSize"] = pixelSize

        #''' add filename to list '''
        #fileNameList.append(namesDictionary)
        
        
    #return fileNameList
