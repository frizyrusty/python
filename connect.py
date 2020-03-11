# from pip._internal import main
# main(['install', 'mysql-connector-python-rf'])

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

if db.is_connected():
    print("Berhasil terhubung ke database")
else:
    print("Tidak berhasil")
    exit();

cursor = db.cursor()
# cursor.execute("CREATE DATABASE toko_mainan")

# sql = """CREATE TABLE customers (
#   customer_id INT AUTO_INCREMENT PRIMARY KEY,
#   name VARCHAR(255),
#   address Varchar(255)
# )
# """
# cursor.execute(sql)

sql = "INSERT INTO customers (name, address) values (%s, %s)"
val = ("Dian", "Bandung")
cursor.execute(sql, val)
db.commit()
print("{} data ditambahkan".format(cursor.rowcount))