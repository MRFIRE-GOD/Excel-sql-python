import sqlite3
# Get customer number from user
customer_number = input("Enter customer number: ")

# Connect to the database
conn = sqlite3.connect('customer_list.db')
c = conn.cursor()


# Retrieve all information about the customer
c.execute("SELECT * FROM customer_info WHERE customer_number = ?", (customer_number,))
customer_info = c.fetchall()

c.execute("SELECT * FROM postcode_table WHERE customer_number = ?", (customer_number,))
postcode_info = c.fetchall()

# Print the customer information
print("Customer Number: ", customer_info[0])
print("Name: ", customer_info[1])
print("Address: ", customer_info[2])
print("Postcode: ", customer_info[3])
print("City: ", postcode_info[0])
print("State: ", postcode_info[1])

# Close the connection
conn.close()
