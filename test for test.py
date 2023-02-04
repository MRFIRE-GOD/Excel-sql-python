import sqlite3
import csv

def kundeinfo():
    # Connect to the database
    conn = sqlite3.connect("kundeliste.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("CREATE TABLE kundeinfo (Kundenummer INTEGER PRIMARY KEY, Fornavn TEXT, Etternavn TEXT, Epost TEXT, Tlf TEXT, Postnummer INTEGER, FOREIGN KEY (Postnummer) REFERENCES postnummer_tabell(Postnummer))")
    cursor.execute("CREATE TABLE postnummer_tabell (Postnummer INTEGER PRIMARY KEY, Poststed TEXT, Kommunenummer INTEGER, Kommunenavn TEXt, Kategori TEXT)")

    # Read data from the "kundeinfo.csv" file
    with open('randoms.csv', 'r') as kundeinfo_file:
        kundeinfo_reader = csv.reader(kundeinfo_file)
        next(kundeinfo_reader)
        for row in kundeinfo_reader:
            if len(row) >= 6:
                cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))


    # Read data from the "postnummer_tabell.csv" file
    with open('Postnummerregister.csv', 'r') as postnummer_file:
        postnummer_reader = csv.reader(postnummer_file)
        # Skip header row
        next(postnummer_reader)
        for row in postnummer_reader:
            # Insert data into the "postnummer_tabell" table
            cursor.execute("INSERT INTO postnummer_tabell VALUES (?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4]))

    # Save changes to the database
    conn.commit()

    # Ask the user for a customer number
    customer_number = input("Hva er ditt kundenummer: ")

    # Get customer information from the database
    cursor.execute("SELECT * FROM kundeinfo JOIN postnummer_tabell ON kundeinfo.Postnummer = postnummer_tabell.Postnummer WHERE Kundenummer=?", (customer_number,))
    customer_info = cursor.fetchone()
    print("Kundeinformasjon: ")
    print("Fnavn: ", customer_info[1]) 
    print("EtterNavn",customer_info[2])
    print("Epost: ", customer_info[3])
    print("Telefonnummer: ", customer_info[4])
    print("Postnummer: ", customer_info[5])
    print("Poststed: ", customer_info[6])

    # Close the connection
    conn.close()

kundeinfo()
