import sqlite3
import csv



# database
conn = sqlite3.connect("tes-kundeliste.db")
cursor = conn.cursor()

    # lage  tables

cursor.execute("CREATE TABLE kundepost (Postnummer INTEGER PRIMARY KEY, Poststed TEXT, Kommunenummer  TEXT, Kommunenavn TEXT, Kategori TEXT)")
cursor.execute("CREATE TABLE kundeinfo (fname TEXT, ename TEXT, epost TEXT, tlf TEXT, postnummer TEXT)")

    cursor.execute("CREATE TABLE kundepost (Postnummer INTEGER PRIMARY KEY, Poststed TEXT, Kommunenummer  TEXT, Kommunenavn TEXT, Kategori TEXT)")
    cursor.execute("CREATE TABLE kundeinfo (fname TEXT, ename TEXT, epost TEXT, tlf TEXT, postnummer TEXT)"


    # lese data fra Postnummerregister.csv filen
with open('Postnummerregister.csv', 'r') as kundepost_file:
    kundepost_reader = csv.reader(kundepost_file)
        # Skip header
    next(kundepost_reader)
    for row in kundepost_reader:
            # legge tildata til kundeliste table
        cursor.execute("INSERT INTO kundepost VALUES (?,?,?,?,?)", (row[0], row[1], row[2], row[3],row[4]))

    # lese data fra randoms.csv file
with open('randoms.csv', 'r') as kundeinfo_file:
    kundeinfo_reader = csv.reader(kundeinfo_file)
        # Skip header row
    next(kundeinfo_reader)
    for row in kundeinfo_reader:
            # legge til data til kundeinfo table
            cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4]))


    # lagre 
conn.commit()

    # spøre kunder om customer number
customer_number = input("Hva er ditt kunde NR: ")

     # kunde info fra  database
cursor.execute("SELECT * FROM kundepost JOIN kundeinfo ON kundepost.postnummer = kundeinfo.postnummer WHERE kundepost.postnummer=?", (customer_number,))
customer_info = cursor.fetchone()
if customer_info:
    print("Customer Information:")
    print("Name: ", customer_info[1])
    print("Address: ", customer_info[2])
    print("Phone number: ", customer_info[3])
    print("Email: ", customer_info[4])
    print("Postal code: ", customer_info[5])
    print("Postal town: ", customer_info[6])
else:
    print("No customer found with this number")


    # Close the connection
conn.close()
