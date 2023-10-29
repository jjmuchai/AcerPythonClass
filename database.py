import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE1(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully")
conn.close()