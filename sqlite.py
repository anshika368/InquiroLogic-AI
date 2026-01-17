import sqlite3

#connect to sqlite database
connection=sqlite3.connect('student.db')

# create a cursor object to insert data, create table, etc
cursor=connection.cursor()

#create a table
table_info="""
create table STUDENT(NAME VARCHAR(20),CLASS VARCHAR(20),SECTION VARCHAR(25), MARKS INT)"""
cursor.execute(table_info)

##insert data into table
cursor.execute("INSERT INTO STUDENT VALUES('John Doe','10th Grade','A',85)")
cursor.execute("INSERT INTO STUDENT VALUES('Jane Smith','10th Grade','B',90)")
cursor.execute("INSERT INTO STUDENT VALUES('Emily Davis','9th Grade','A',88)")
cursor.execute("INSERT INTO STUDENT VALUES('Michael Brown','9th Grade','C',92)")
cursor.execute("INSERT INTO STUDENT VALUES('Jessica Wilson','10th Grade','A',95)")

#display all the data from the table
print("Data in STUDENT table:")
data=cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

#commit the changes
connection.commit()
#close the connection
connection.close()