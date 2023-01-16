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

def sql_oppgave2():
    # Connect to or create the SQLite database
    con = sq.connect('info.db')
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv("Postnummerregister1.csv")
    
    # Create table if it doesn't already exist
    df.to_sql('post', con, if_exists='append',index=False, dtype={'Postnummer': 'VARCHAR(20)',
                                                                'Poststed': 'VARCHAR(255)',
                                                                'Kommunenummer': 'VARCHAR(20)',
                                                                'Kommunenavn': 'VARCHAR(255)',
                                                                'Kategori': 'VARCHAR(255)'}
                                                                )
    # Retrieve and print the data from the table
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM post")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    # Close the connection
    con.close()

sql_oppgave2()