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
