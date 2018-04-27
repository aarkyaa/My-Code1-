
import sqlite3
connection = sqlite3.connect("Essar.db")

cursor = connection.cursor()

#delete 
#cursor.execute("""DROP TABLE Fleet;""")

sql_command = """
CREATE TABLE Fleet ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)

#Insert Value 

sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "ABC", "PQR", "Mumbai", "1961-10-25");"""
cursor.execute(sql_command)


sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "xyz", "DEF", "Pune", "1955-08-17");"""
cursor.execute(sql_command)

#Code Save:
connection.commit()

connection.close()
