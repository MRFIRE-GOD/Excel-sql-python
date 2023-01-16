#import 
import sqlite3 as sq
import pandas as pd
#func
def sql_oppgave2():
    #database lage
    con = sq.connect('info.db')
    c = con.cursor()
    #lage table med og top-navn 
    c.execute('CREATE TABLE IF NOT EXISTS name (Postnummer TEXT, Poststed TEXT, Kommunenummer TEXT, Kommunenavn TEXT, Kategori TEXT)')
    #åpne raw string
    f = open("Postnummerregister1.csv", "r") 
    for line in f:
        c.execute('INSERT INTO name VALUES (?,?,?,?,?)', (line.split(',')))
    con.commit()
    
    c.execute('SELECT * FROM name')
    con.close()

sql_oppgave2()