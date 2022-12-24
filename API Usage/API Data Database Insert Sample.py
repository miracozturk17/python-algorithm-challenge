#********MsSQL********#
import requests
import pyodbc

response = requests.get("http://api_adresi")
data = response.json()

server = 'sunucu_adresi'
database = 'veritabanı_adı'
username = 'kullanıcı_adı'
password = 'parola'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

for item in data:
    cursor.execute("INSERT INTO tablo_adı (sütun1, sütun2, sütun3) VALUES (?,?,?)", item["sütun1"], item["sütun2"], item["sütun3"])
    cnxn.commit()

cnxn.close()



#********MySQL********#
import requests
import mysql.connector

response = requests.get("http://api_adresi")
data = response.json()

cnx = mysql.connector.connect(user='kullanıcı_adı', password='parola', host='sunucu_adresi', database='veritabanı_adı')
cursor = cnx.cursor()

for item in data:
    cursor.execute("INSERT INTO tablo_adı (sütun1, sütun2, sütun3) VALUES (%s,%s,%s)", (item["sütun1"], item["sütun2"], item["sütun3"]))
    cnx.commit()

cnx.close()



#********Oracle********#
import requests
import cx_Oracle

response = requests.get("http://api_adresi")
data = response.json()

dsn_tns = cx_Oracle.makedsn('sunucu_adresi', 'port_numarası', service_name='veritabanı_adı')
conn = cx_Oracle.connect(user='kullanıcı_adı', password='parola', dsn=dsn_tns)
cursor = conn.cursor()

for item in data:
    cursor.execute("INSERT INTO tablo_adı (sütun1, sütun2, sütun3) VALUES (:1, :2, :3)", (item["sütun1"], item["sütun2"], item["sütun3"]))
    conn.commit()

cursor.close()
conn.close()



#********MongoDB********#
import requests
from pymongo import MongoClient

response = requests.get("http://api_adresi")
data = response.json()

client = MongoClient("mongodb://kullanıcı_adı:parola@sunucu_adresi/veritabanı_adı")
db = client['veritabanı_adı']

for item in data:
    result = db.tablo_adı.insert_one(item)

client.close()



#********Cassandra********#
import requests
from cassandra.cluster import Cluster

response = requests.get("http://api_adresi")
data = response.json()

cluster = Cluster(['sunucu_adresi'])
session = cluster.connect()
session.set_keyspace('veritabanı_adı')

for item in data:
    session.execute("INSERT INTO tablo_adı (sütun1, sütun2, sütun3) VALUES (%s, %s, %s)", (item["sütun1"], item["sütun2"], item["sütun3"]))

cluster.shutdown()



#********PostgreSQL********#
import requests
import psycopg2

response = requests.get("http://api_adresi")
data = response.json()

cnxn = psycopg2.connect(host="sunucu_adresi", database="veritabanı_adı", user="kullanıcı_adı", password="parola")
cursor = cnxn.cursor()

for item in data:
    cursor.execute("INSERT INTO tablo_adı (sütun1, sütun2, sütun3) VALUES (%s, %s, %s)", (item["sütun1"], item["sütun2"], item["sütun3"]))
    cnxn.commit()

cursor.close()
cnxn.close()



#********DBeaver********#
import requests
import pyodbc

response = requests.get("http://api_adresi")
data = response.json()

cnxn = pyodbc.connect('DRIVER={veritabanı_sürücüsü};'
                      'SERVER=sunucu_adresi;'
                      'DATABASE=veritabanı_adı;'
                      'UID=kullanıcı_adı;'
                      'PWD=parola')
cursor = cnxn.cursor()

for item in data:
    cursor.execute("INSERT INTO tablo_adı (sütun1, sütun2, sütun3) VALUES (?, ?, ?)", (item["sütun1"], item["sütun2"], item["sütun3"]))
    cnxn.commit()

cursor.close()
cnxn.close()