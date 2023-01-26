import sqlite3
import csv

# database
conn = sqlite3.connect("kundeliste.db")
cursor = conn.cursor()

# lage  tables
cursor.execute("CREATE TABLE kundeliste (kundenr INTEGER PRIMARY KEY, navn TEXT, adresse TEXT)")
cursor.execute("CREATE TABLE kundeinfo (kundenr INTEGER,telefonnr TEXT, epost TEXT, FOREIGN KEY (kundenr) REFERENCES kundeliste(kundenr))")


# lese data fra Postnummerregister.csv filen
with open('Postnummerregister.csv', 'r') as kundeliste_file:
    kundeliste_reader = csv.reader(kundeliste_file)
    # Skip header
    next(kundeliste_reader)
    for row in kundeliste_reader:
        # legge tildata til kundeliste table
        cursor.execute("INSERT INTO kundeliste VALUES (?,?,?)", (row[0], row[1], row[2]))

# lese data fra randoms.csv file
with open('randoms.csv', 'r') as kundeinfo_file:
    kundeinfo_reader = csv.reader(kundeinfo_file)
    # Skip header row
    next(kundeinfo_reader)
    for row in kundeinfo_reader:
        # legge til data til kundeinfo table
            cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?)", (row[0], row[1], row[2]))


# lagre 
conn.commit()

# spøre kunder om customer number
customer_number = input("Hva er ditt kunde NR: ")

# kunde info fra  database
cursor.execute("SELECT * FROM kundeliste JOIN kundeinfo ON kundeliste.kundenr = kundeinfo.kundenr JOIN kundeinfo ON kundeliste.postnr = kundeinfo.postnr WHERE kundeliste.kundenr=?", (customer_number,))


customer_info = cursor.fetchone()
print("Customer Information:")
print("Name: ", customer_info[1])
print("Address: ", customer_info[2])
print("Phone number: ", customer_info[3])
print("Email: ", customer_info[4])
print("Postal code: ", customer_info[5])
print("Postal town: ", customer_info[6])

# Close the connection
conn.close()

