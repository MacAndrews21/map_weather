# -*- coding: utf-8 -*-
import psycopg2 as psy
import sys
import pprint

#def con():
    #string = "host='localhost' dbname='teetest' user='postgres' password='postgres' "

    #return string

#def select():
    #string = "host='localhost' dbname='teetest' user='postgres' password='postgres' "

    #con = psy.connect(string)
    #cursor = con.cursor()  
    #cursor.execute("SELECT * FROM tee")

    #records = cursor.fetchall()

    #return records

#rec = into()
#pprint.pprint(rec)

def into(kb, year, width, height, pixelSize):
    string = "host='localhost' dbname='teetest' user='postgres' password='postgres' "

    try:
        con = psy.connect(string)
        cursor = con.cursor()    
        cursor.execute("INSERT INTO tee (kb, year, width, height, pxsize) VALUES (%s, %s, %s, %s, %s)",(kb,year, width, height, pixelSize,))
        con.commit()
    except:
        print "fail!"
    finally:
        if con:
            cursor.close()
            con.close()
            print "FIN"
    
    

    #records = cursor.fetchall()

    #return records


#,geogr_breite,geogr_laenge,von_datum,bis_datum,stationsname,


def into_recent(stations_id,stationshoehe,geogr_breite,geogr_laenge,von_datum,bis_datum,stationsname):
    string = "host='localhost' dbname='map_weather_test' user='postgres' password='postgres' "
    
    #stationsname = stationsname.replace( 'ß', '[ss]')
    #stationsname = stationsname.replace( 'ä', '[ae]')
    #stationsname = stationsname.replace( 'ö', '[oe]')
    #stationsname = stationsname.replace( 'ü', '[ue]')
    #stationsname = stationsname.replace( 'Ä', '[AE]')
    #stationsname = stationsname.replace( 'Ö', '[OE]')
    #stationsname = stationsname.replace( 'Ü', '[UE]')
    
    if bis_datum == '':
        bis_datum = None
    if geogr_breite == '':
        geogr_breite = None
    if geogr_laenge == '':
        geogr_laenge = None
    if stationshoehe == '':
        stationshoehe = None
    
    print stationsname
    try:
        con = psy.connect(string)
        cursor = con.cursor()
        
        cursor.execute("""INSERT INTO recent(stations_id,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum,geom_4326 ) VALUES (%s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_Point(%s,%s),4326))""",(stations_id,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum,geogr_laenge,geogr_breite,))
        #cursor.execute("""INSERT INTO recent(stations_i,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum ) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(999,5,99.999,99.999,'hallo_welt',20151223,20153256,))

        con.commit()
        print 'SUCCESS'
    except psy.Error as e:
        print "connecting fail!"
            
        print "INSERT INTO failed!"        
        log = open('database.log', 'a')    
        log.write(stations_id + ' :: ' + stationsname + '\n')    
        log.write(e.pgerror + '\n\n')    
        log.close()    
  
    finally:
        if con:
            cursor.close()
            con.close()
            print "FIN"

def into_historical(stations_id,stationshoehe,geogr_breite,geogr_laenge,von_datum,bis_datum,stationsname):
    string = "host='localhost' dbname='map_weather_test' user='postgres' password='postgres' "
    
    #stationsname = stationsname.replace( 'ß', '[ss]')
    #stationsname = stationsname.replace( 'ä', '[ae]')
    #stationsname = stationsname.replace( 'ö', '[oe]')
    #stationsname = stationsname.replace( 'ü', '[ue]')
    #stationsname = stationsname.replace( 'Ä', '[AE]')
    #stationsname = stationsname.replace( 'Ö', '[OE]')
    #stationsname = stationsname.replace( 'Ü', '[UE]')
    
    if bis_datum == '':
        bis_datum = 0
    if geogr_breite == '':
        geogr_breite = 0
    if geogr_laenge == '':
        geogr_laenge = 0
    if stationshoehe == '':
        stationshoehe = 0
    
    print stationsname
    try:
        con = psy.connect(string)
        cursor = con.cursor()
        
        cursor.execute("""INSERT INTO historical(stations_id,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum,geom_4326 ) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_Point(%s,%s),4326))""",(stations_id,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum,geogr_laenge,geogr_breite,))
        #cursor.execute("""INSERT INTO recent(stations_i,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum ) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(999,5,99.999,99.999,'hallo_welt',20151223,20153256,))

        con.commit()
        print 'SUCCESS'
    except psy.Error as e:
        print "connecting fail!"
            
        print "INSERT INTO failed!"        
        log = open('database.log', 'a')    
        log.write(stations_id + ' :: ' + stationsname + '\n')    
        log.write(e.pgerror + '\n\n')    
        log.close()    
  
    finally:
        if con:
            cursor.close()
            con.close()
            print "FIN"            
            
