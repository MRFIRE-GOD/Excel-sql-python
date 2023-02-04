import csv
import xlrd 
import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('kundeliste.db')
cursor = conn.cursor()

# Create the customer info table
cursor.execute('''
CREATE TABLE IF NOT EXISTS kundeinfo (
  kundenummer INT PRIMARY KEY,
  navn TEXT NOT NULL,
  adresse TEXT NOT NULL,
  telefon INT NOT NULL
)
''')

# Read customer info from the xlsx file
book = xlrd.open_workbook("kundeinfo.xlsx")
sheet = book.sheet_by_index(0)
for row_idx in range(1, sheet.nrows):
    row = sheet.row(row_idx)
    kundenummer = int(row[0].value)
    navn = row[1].value
    adresse = row[2].value
    telefon = int(row[3].value)
    cursor.execute("""
        INSERT INTO kundeinfo (kundenummer, navn, adresse, telefon)
        VALUES (?,?,?,?)
        """, (kundenummer, navn, adresse, telefon))

# Create the postal code table
cursor.execute('''
CREATE TABLE IF NOT EXISTS postnummer_tabell (
  postnummer INT PRIMARY KEY,
  poststed TEXT NOT NULL
)
''')

# Read postal codes from the csv file
with open("postnummer_tabell.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip the header
    for row in reader:
        postnummer = int(row[0])
        poststed = row[1]
        cursor.execute("""
            INSERT INTO postnummer_tabell (postnummer, poststed)
            VALUES (?,?)
            """, (postnummer, poststed))

# Create the foreign key constraint
cursor.execute('''
ALTER TABLE kundeinfo 
ADD FOREIGN KEY (postnummer) 
REFERENCES postnummer_tabell(postnummer)
''')

conn.commit()

# Query customer information based on customer number
kundenummer = int(input("Enter customer number: "))
cursor.execute("""
    SELECT kundeinfo.kundenummer, navn, adresse, telefon, poststed
    FROM kundeinfo
    JOIN postnummer_tabell
    ON kundeinfo.postnummer = postnummer_tabell.postnummer
    WHERE kundeinfo.kundenummer=?
    """, (kundenummer,))
result = cursor.fetchone()
if result:
    print("Customer Number:", result[0])
    print("Name:", result[1])
    print("Address:", result[2])
    print("Phone:", result[3])
    print("Postal Code:", result[4])
else:
    print("Customer not found")
