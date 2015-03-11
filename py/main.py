import cv2
import glob
import os
import sys
import functions as fs
import postgres as po

#names = fs.createFileNameList("/home/andreas/Projekte/test-data/")



#def main(name):
    #name = name + '/'
    #fs.createTempData('data/' + name)
    ##fs.createTempData('data/historical/')

    #recent = fs.createFileNameList('data/' + name + 'station_metadata/')
    ##historical = fs.createFileNameList('data/historical/temporary_metadata/')
    ##print test
    ##print ''
    #allDataList = []
    #for i in recent:
        #if 'Stationsmetadaten' in i['name']:
            ##print i['name']
            #data = fs.getStations('data/' + name + 'station_metadata/', i['name'])
            ##print len(data)
        #else:
            #data = None

        #allDataList.append(data)

    #for a in range(len(allDataList)):
        #for b in range(len(allDataList[a])):
            #print allDataList[a][b]['Stations_id'] ,allDataList[a][b]['Stationsname'] ,allDataList[a][b]['Stationshoehe'] ,allDataList[a][b]['Geogr.Breite'] ,allDataList[a][b]['Geogr.Laenge'] ,allDataList[a][b]['von_datum'] ,allDataList[a][b]['bis_datum'] ,allDataList[a][b]['Stationsname']
            #pass
            ##if 'recent' in name:
                ##po.into_recent(allDataList[a][b]['Stations_id'] ,allDataList[a][b]['Stationshoehe'] ,allDataList[a][b]['Geogr.Breite'] ,allDataList[a][b]['Geogr.Laenge'] ,allDataList[a][b]['von_datum'] ,allDataList[a][b]['bis_datum'] ,allDataList[a][b]['Stationsname'])
            ##if 'historical' in name:
                ##po.into_historical(allDataList[a][b]['Stations_id'] ,allDataList[a][b]['Stationshoehe'] ,allDataList[a][b]['Geogr.Breite'] ,allDataList[a][b]['Geogr.Laenge'] ,allDataList[a][b]['von_datum'] ,allDataList[a][b]['bis_datum'] ,allDataList[a][b]['Stationsname'])


##names = ['recent', 'historical']
##main(names[0])
##main(names[1])

#firstLineList = fs.getFirstLine('data/historical/temperatur_data/', 'produkt_klima_Tageswerte_19370101_19860630_00001.txt')

#print firstLineList


fileType = 'txt'
#txtFilesInZIP = fs.csvZIP('data/recent/tageswerte_KL_13711_akt.zip', fileType) 
currentZIP = fs.csvZIP('data/recent/tageswerte_KL_03513_akt.zip', fileType) 

readZIP = currentZIP.readZIP()

#print readZIP.keys()
for txtFiles in readZIP:
    if 'meta' in txtFiles:
        #print readZIP[txtFiles]['firstLine']

        #print readZIP[txtFiles].keys()
        print readZIP[txtFiles]['data']
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        