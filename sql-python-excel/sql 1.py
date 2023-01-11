#import modul
import sqlite3 as sq
import pandas as pd
def sql_oppgave1():
    con = sq.connect('data-info.db')
    c = con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS name (For Navn TEXT, Etter Navn TEXT, Epost TEXT, Telefon TEXT, Postnummer TEXT)')
    f = open("randoms (1).csv", "r")
    for line in f:
        c.execute('INSERT INTO name VALUES (?,?,?,?,?)', (line.split(',')))
    con.commit()
    c.execute('SELECT * FROM name')
    con.close()

sql_oppgave1()