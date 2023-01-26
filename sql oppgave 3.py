import sqlite3

# Opprett forbindelse til databasen
conn = sqlite3.connect("kundeliste.db")
cursor = conn.cursor()

# Opprett tabellene
cursor.execute("CREATE TABLE kundeliste (kundenr INTEGER PRIMARY KEY, navn TEXT, adresse TEXT)")
cursor.execute("CREATE TABLE kundeinfo (kundenr INTEGER PRIMARY KEY, telefonnr TEXT, epost TEXT)")


# Les dataene fra filen
with open("data.txt", "r") as file:
    data = file.readlines()
    for line in data:
        line = line.strip().split(",")
        kundenr = line[0]
        navn = line[1]
        adresse = line[2]
        telefonnr = line[3]
        epost = line[4]
        postnr = line[5]
        poststed = line[6]
        
        # Legg til dataene i tabellene
        cursor.execute("INSERT INTO kundeliste VALUES (?,?,?)", (kundenr, navn, adresse))
        cursor.execute("INSERT INTO kundeinfo VALUES (?,?,?)", (kundenr, telefonnr, epost))
        cursor.execute("INSERT INTO postnummer_tabell VALUES (?,?)", (postnr, poststed))

# Spør brukeren om kundenummer
kundenr = input("Skriv inn kundenummer: ")

# Hent dataene om kunden fra tabellene
cursor.execute("SELECT * FROM kundeliste WHERE kundenr=?", (kundenr,))
kunde_data = cursor.fetchone()
cursor.execute("SELECT * FROM kundeinfo WHERE kundenr=?", (kundenr,))
kundeinfo_data = cursor.fetchone()
cursor.execute("SELECT poststed FROM postnummer_tabell WHERE postnr=?", (kunde_data[2],))
poststed_data = cursor.fetchone()

# Vis dataene om kunden
print("Kundenummer: ", kundenr)
print("Navn: ", kunde_data[1])
print("Adresse: ", kunde_data[2])
print("Telefonnr: ", kundeinfo_data[1])
print("E-post: ", kundeinfo_data[2])
print("Postnummer: ", kunde_data[2])

conn.close()