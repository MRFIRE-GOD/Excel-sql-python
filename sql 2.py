import pandas as pd
import sqlite3 as sq

def sql_oppgave2():
    # Connect to or create the SQLite database
    con = sq.connect('info.db')
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv("Postnummerregister1.csv")
    
    # Create table if it doesn't already exist
    df.to_sql('name', con, if_exists='append',index=False, dtype={'Postnummer': 'VARCHAR(20)',
                                                                'Poststed': 'VARCHAR(255)',
                                                                'Kommunenummer': 'VARCHAR(20)',
                                                                'Kommunenavn': 'VARCHAR(255)',
                                                                'Kategori': 'VARCHAR(255)'}
                                                                )
    # Retrieve and print the data from the table
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM name")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    # Close the connection
    con.close()

sql_oppgave2()
