import sqlite3
import os

# Create database connection 

con = sqlite3.connect('Test.db') # This will create the database

# Create Cursor to use to perform actions on the database

cur = con.cursor()

# Use the cursor to execute a sql command in this case to create a table to hold information

file_exists = os.path.exists('Test.db')  # Checks to see if database exists


if file_exists:
    print("Database Already Exists")

else:    
    cur.execute(""" CREATE TABLE Customers(     
                first_name text,
                last_name text,
                address_1 text,
                address_2 text)
    """)
    print("Database Added...")


# Use cursor to insert data into the table

#cur.execute("INSERT INTO Customers VALUES ('Russell','Smith','3 Blackett Cottage','Matfen')")

#print("Data Added to Database")






con.commit()    # Commits the changes to the database

# Close the database connection

con.close()