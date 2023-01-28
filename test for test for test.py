import sqlite3
import csv

def create_tables():
    # Connect to the database
    conn = sqlite3.connect("test-kundeliste.db")
    cursor = conn.cursor()

    # Create the kundeinfo table
    cursor.execute('''CREATE TABLE kundeinfo (
                        kundenr INTEGER PRIMARY KEY,
                        fname TEXT,
                        ename TEXT,
                        epost TEXT,
                        tlf TEXT,
                        postnummer INTEGER,
                        FOREIGN KEY (postnummer) REFERENCES postnummer_tabell(postnummer)
                    )''')

    # Create the postnummer_tabell table
    cursor.execute('''CREATE TABLE postnummer_tabell (
                        postnummer INTEGER PRIMARY KEY,
                        poststed TEXT,
                        kommunenummer  TEXT,
                        kommunenavn TEXT,
                        kategori TEXT
                    )''')

    # Save the changes
    conn.commit()
    conn.close()

def populate_tables():
    # Connect to the database
    conn = sqlite3.connect("kundeliste.db")
    cursor = conn.cursor()

    # Read data from Postnummerregister.csv file
    with open('Postnummerregister.csv', 'r') as postnummer_file:
        postnummer_reader = csv.reader(postnummer_file)
        # Skip header
        next(postnummer_reader)
        for row in postnummer_reader:
            # Add data to postnummer_tabell table
            cursor.execute("INSERT INTO postnummer_tabell VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))

    # Read data from randoms.csv file
    with open('randoms.csv', 'r') as kundeinfo_file:
        kundeinfo_reader = csv.reader(kundeinfo_file)
        # Skip header row
        next(kundeinfo_reader)
        for row in kundeinfo_reader:
            # Add data to kundeinfo table
            cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))

    # Save the changes
    conn.commit()
    conn.close()

def get_customer_info():
    # Connect to the database
    conn = sqlite3.connect("kundeliste.db")
    cursor = conn.cursor()

    # Ask the user for customer number
    customer_number = input("Hva er ditt kunde NR: ")

    # Get customer info from the database
    cursor.execute('''SELECT kundeinfo.fname, kundeinfo.ename, kundeinfo.epost, kundeinfo.tlf, postnummer_tabell.poststed, postnummer_tabell.kommunenavn
                      FROM kundeinfo
                      JOIN postnummer_tabell ON kundeinfo.postnummer = postnummer_tabell.postnummer
                      WHERE kundeinfo.kundenr = ?''', (customer_number,))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    # Save the changes
    conn.commit()
    conn.close()
create_tables()
populate_tables()
get_customer_info()