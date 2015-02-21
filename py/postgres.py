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


def into_db(stations_id,stationshoehe,geogr_breite,geogr_laenge,von_datum,bis_datum,stationsname):
    string = "host='localhost' dbname='map_weather_test' user='postgres' password='postgres' "
    
    stationsname = stationsname.replace( 'ß', '[ss]')
    stationsname = stationsname.replace( 'ä', '[ae]')
    stationsname = stationsname.replace( 'ö', '[oe]')
    stationsname = stationsname.replace( 'ü', '[ue]')
    stationsname = stationsname.replace( 'Ä', '[AE]')
    stationsname = stationsname.replace( 'Ö', '[OE]')
    stationsname = stationsname.replace( 'Ü', '[UE]')
    
    print stationsname
    try:
        con = psy.connect(string)
        cursor = con.cursor()    
        cursor.execute("""INSERT INTO recent(stations_id,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum ) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(stations_id,stationshoehe,geogr_breite,geogr_laenge,stationsname,von_datum,bis_datum,))
        con.commit()
        print 'SUCCESS'
    except:
        print "fail!"
    finally:
        if con:
            cursor.close()
            con.close()
            print "FIN"