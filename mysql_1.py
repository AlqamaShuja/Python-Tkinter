import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="pydb")

# if(connection.is_connected()):
#     print("Connection Established")
#     print(connection.connection_id)

cursor = connection.cursor()
# cursor.execute("CREATE DATABASE pyDB")
# query = "CREATE TABLE book(bookId integer(4), title varchar(40), price float(5, 2))"
# cursor.execute(query)
id = 12
title1 = "Python"
price = 2.5
query = f"INSERT INTO book (bookId, title, price) VALUES (%s, %s, %s)"
# query = "INSERT INTO book(bookId, title, price) VALUES ("+ str(id) +"," + str(title1) +"," + str(price) + ")"
# para = (13, "NodeJS", 345)
# cursor.execute(query, para)

para = [
    (15, "Next", 88.2),
    (16, "NodeJS", 65.5),
    (17, "ReactJS", 44.24),
    (23, "VueJS", 23.5),
    (34, "C++", 520),
    (45, "Go", 420),
    (18, "Ruby on Rail", 290),
]

# cursor.executemany(query, para)

# connection.commit()

# print(cursor.rowcount, " Inserted")

# Fetch all data
# selectQuery = "SELECT * FROM book";
# cursor.execute(selectQuery)
# result = cursor.fetchall()
#
# for x in result:
#     print(x)


# UPDATE
updateQuery = "UPDATE book SET price=price+10 WHERE price>100"
cursor.execute(updateQuery)
connection.commit()

print(cursor.rowcount, " rows affected")