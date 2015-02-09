import cv2
import glob
import os
import sys
import functions as fs
import postgres as po

names = fs.createFileNameList("/home/andreas/Projekte/test-data/")

#print len(names)
#print names[0]

#res = fs.getResolution("/home/andreas/Projekte/test-data/", "1011_1956.tif")

for name in names:
    #print name['id']
    "{'name': '1011_1956.tif', 'height': 4742, 'width': 3161, 'year': '1956', 'pixelSize': 0.5061063788453273, 'id': '1011'}"
    po.into(name['id'], name['year'], name['width'],name['height'], name['pixelSize'])
