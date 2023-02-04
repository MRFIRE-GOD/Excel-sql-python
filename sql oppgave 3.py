import sqlite3
import csv

def main():
    create_tables()
    populate_tables()
    get_customer_info()

def create_tables():
    conn = sqlite3.connect("test-test-kundeliste.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE postnummer_tabell (
            postnummer INTEGER PRIMARY KEY,
            poststed TEXT,
            kommunenummer  TEXT,
            kommunenavn TEXT,
            kategori TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE kundeinfo (
            kundenr INTEGER PRIMARY KEY,
            fname TEXT,
            ename TEXT,
            epost TEXT,
            tlf TEXT,
            postnummer INTEGER,
            FOREIGN KEY (postnummer) REFERENCES postnummer_tabell(postnummer)
        )
    ''')

    conn.commit()
    conn.close()

def populate_tables():
    conn = sqlite3.connect("test-kundeliste.db")
    cursor = conn.cursor()

    with open('Postnummerregister.csv', 'r') as postnummer_file:
        reader = csv.reader(postnummer_file)
        next(reader)
        for row in reader:
            if len(row) == 5:
                postnummer = row[0]
                cursor.execute("SELECT * FROM postnummer_tabell WHERE postnummer=?", (postnummer,))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO postnummer_tabell VALUES (?,?,?,?,?)", row)

    with open('randoms.csv', 'r') as kundeinfo_file:
        reader = csv.reader(kundeinfo_file)
        next(reader)
        for row in reader:
            if len(row) == 6:
                cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?,?,?,?)", row)

    conn.commit()
    conn.close()

def get_customer_info():
    conn = sqlite3.connect("test-kundeliste.db")
    cursor = conn.cursor()

    customer_number = input("What is your customer number: ")

    cursor.execute('''
        SELECT fname, ename, epost, tlf, poststed, kommunenavn
        FROM kundeinfo
        JOIN postnummer_tabell ON kundeinfo.postnummer = postnummer_tabell.postnummer
        WHERE kundenr = ?
    ''', (customer_number,))

    customer_info = cursor.fetchone()

    if customer_info:
        print("Kunde informasjon:")
        print("Fornavn: ", customer_info[0])
        print("Etternavn: ", customer_info[1])
        print("E-post: ", customer_info[2])
        print("Telefon: ", customer_info[3])
        print("Poststed: ", customer_info[4])
        print("Kommunenavn: ", customer_info[5])
    else:
            print("Ingen kunde funnet med kundenummer ", customer_number)

    conn.close()

if __name__ == '__main__':
    main()
    create_tables()
    populate_tables()
    get_customer_info()

