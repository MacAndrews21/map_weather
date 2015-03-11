# -*- coding: utf-8 -*-
#s = 'Großenkneten'
#s = s.replace(u'00DF', '[ss]')

#print s



namedict = ({"first_name":"Joshua", "last_name":"Drake"},
            {"first_name":"Steven", "last_name":"Foo"},
            {"first_name":"David", "last_name":"Bar"})

namelist = [{"first_name":"Joshua", "last_name":"Drake"},
            {"first_name":"Steven", "last_name":"Foo"},
            {"first_name":"David", "last_name":"Bar"}]



#cur.executemany("""INSERT INTO bar(first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)
test = {"first_name":"David", "last_name":"Bar"}
namedict += (test,)

namelist += [test]
print namedict[0]['first_name']
print
print namelist