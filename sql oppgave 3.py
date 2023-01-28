import sqlite3
import csv

def create_tables():
    # database
    conn = sqlite3.connect("kundeliste.db")
    cursor = conn.cursor()

    # lage  kundeinfo table
    cursor.execute('''CREATE TABLE kundeinfo (
                        kundenr INTEGER PRIMARY KEY,
                        fname TEXT,
                        ename TEXT,
                        epost TEXT,
                        tlf TEXT,
                        postnummer INTEGER,
                        FOREIGN KEY (postnummer) REFERENCES postnummer_tabell(postnummer)
                    )''')

    # lage postnummer_tabell table
    cursor.execute('''CREATE TABLE postnummer_tabell (
                        postnummer INTEGER PRIMARY KEY,
                        poststed TEXT,
                        kommunenummer  TEXT,
                        kommunenavn TEXT,
                        kategori TEXT
                    )''')

    
    conn.commit()
    conn.close()

def populate_tables():
    # kontakte til database
    conn = sqlite3.connect("kundeliste.db")
    cursor = conn.cursor()

    # lese data fra Postnummerregister.csv 
    with open('Postnummerregister.csv', 'r') as postnummer_file:
        postnummer_reader = csv.reader(postnummer_file)
        
        next(postnummer_reader)
        for row in postnummer_reader:
            # legg til data til postnummer_tabell 
            cursor.execute("INSERT INTO postnummer_tabell VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))

    # lese data fra randoms.csv 
    with open('randoms.csv', 'r') as kundeinfo_file:
        kundeinfo_reader = csv.reader(kundeinfo_file)
        # row
        next(kundeinfo_reader)
        for row in kundeinfo_reader:
            # legge til data til kundeinfo 
            cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))

    # 
    conn.commit()
    conn.close()

def get_customer_info():
    # kontakte til  database
    conn = sqlite3.connect("kundeliste.db")
    cursor = conn.cursor()

    # spøre om kunde nr
    customer_number = input("Hva er ditt kunde NR: ")

    # få kunde nr info fra database
    cursor.execute('''SELECT kundeinfo.fname, kundeinfo.ename, kundeinfo.epost, kundeinfo.tlf, postnummer_tabell.poststed, postnummer_tabell.kommunenavn
                      FROM kundeinfo
                      JOIN postnummer_tabell ON kundeinfo.postnummer = postnummer_tabell.postnummer
                      WHERE kundeinfo.kundenr = ?''', (customer_number,))

    # printe resultate
    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.commit()
    conn.close()
create_tables()
populate_tables()
get_customer_info()