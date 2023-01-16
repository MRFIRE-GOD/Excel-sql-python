#import 
import sqlite3 as sq
import pandas as pd
#func
def sql_oppgave1():
    #database lage
    con = sq.connect('data-info.db')
    c = con.cursor()
    #lage table med og top-navn 
    c.execute('CREATE TABLE IF NOT EXISTS name (Foravn TEXT, Etteravn TEXT, Epost TEXT, Telefon TEXT, Postnummer TEXT)')
    #åpne raw string
    f = open("randoms (1).csv", "r") 
    for line in f:
        c.execute('INSERT INTO name VALUES (?,?,?,?,?)', (line.split(',')))
    con.commit()
    
    c.execute('SELECT * FROM name')
    con.close()

sql_oppgave1()