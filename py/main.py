import cv2
import glob
import os
import sys
import functions as fs
import postgres as po

#names = fs.createFileNameList("/home/andreas/Projekte/test-data/")

temp = fs.createFolderNameList('data')
#test = []
#for t in temp:
    #print t
    #print ''
    
test = fs.createFileNameList('data/meta/')
#print test
#print ''
allDataList = []
for i in test:
    if 'Stationsmetadaten' in i['name']:
        #print i['name']
        data = fs.getStations('data/meta/', i['name'])
        #print len(data)
    else:
        data = None
    
    if data != None:
        for s in range(len(data)):
            #print data[s]['Geogr.Breite']
            pass
        pass

    allDataList.append(data)
    #test.append(data)
#print test
for a in range(len(allDataList)):
    for b in range(len(allDataList[a])):
        print allDataList[a][b]['Stations_id'] ,allDataList[a][b]['Stationsname'] ,allDataList[a][b]['Stationshoehe'] ,allDataList[a][b]['Geogr.Breite'] ,allDataList[a][b]['Geogr.Laenge'] ,allDataList[a][b]['von_datum'] ,allDataList[a][b]['bis_datum'] ,allDataList[a][b]['Stationsname']
        #pass
        po.into_db(allDataList[a][b]['Stations_id'] ,allDataList[a][b]['Stationshoehe'] ,allDataList[a][b]['Geogr.Breite'] ,allDataList[a][b]['Geogr.Laenge'] ,allDataList[a][b]['von_datum'] ,allDataList[a][b]['bis_datum'] ,allDataList[a][b]['Stationsname'])

