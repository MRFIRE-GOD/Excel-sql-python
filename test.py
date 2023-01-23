import pandas as pd
import sqlite3

# Connect to or create the database
conn = sqlite3.connect('customer_list.db')

# Read data from the first Excel file
customer_info_df = pd.read_excel('Postnummerregister.csv')

# Insert the data into the customer_info table
customer_info_df.to_sql('customer_info', conn, if_exists='replace', index=False)

# Read data from the second Excel file
postcode_table_df = pd.read_excel('randoms.csv')

# Insert the data into the postcode_table table
postcode_table_df.to_sql('postcode_table', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
