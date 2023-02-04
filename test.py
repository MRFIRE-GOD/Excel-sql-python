import sqlite3
import csv

def create_tables():
    # Connect to the database
    conn = sqlite3.connect("test-kundeliste.db")
    cursor = conn.cursor()

    # Create the postnummer_tabell table
    cursor.execute('''CREATE TABLE postnummer_tabell (
                        postnummer INTEGER PRIMARY KEY,
                        poststed TEXT,
                        kommunenummer  TEXT,
                        kommunenavn TEXT,
                        kategori TEXT
                    )''')

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

    # Save the changes
    conn.commit()
    conn.close()

def populate_tables():
    # Connect to the database
    conn = sqlite3.connect("test-kundeliste.db")
    cursor = conn.cursor()

    # Read data from Postnummerregister.csv file
    with open('Postnummerregister.csv', 'r') as postnummer_file:
        postnummer_reader = csv.reader(postnummer_file)
        # Skip header
        next(postnummer_reader)
        for row in postnummer_reader:
            if len(row) == 5:
                postnummer = row[0]
                # Check if postnummer already exists in the table
                cursor.execute("SELECT * FROM postnummer_tabell WHERE postnummer=?", (postnummer,))
                if not cursor.fetchone():
                    # Add data to postnummer_tabell table
                    cursor.execute("INSERT INTO postnummer_tabell VALUES (?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4]))

    # Read data from randoms.csv file
    with open('randoms.csv', 'r') as kundeinfo_file:
        kundeinfo_reader = csv.reader(kundeinfo_file)
        # Skip header row
        next(kundeinfo_reader)
        for row in kundeinfo_reader:
            # Check if the number of columns in the row matches the number of columns in the table
            if len(row) == 6:
                cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))
            else:
                # Skip the row if the number of columns doesn't match
                continue

    # Save the changes
    conn.commit()
    conn.close()


def get_customer_info():
    # Connect to the database
    conn = sqlite3.connect("test-kundeliste.db")
    cursor = conn.cursor()

    # Get customer information
