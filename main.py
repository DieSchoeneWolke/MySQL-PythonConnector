# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import os
import logging
import time
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

logging.basicConfig(filename='cpy.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

cnx = None

try:
    cnx = mysql.connector.connect(user=user, password=password,
                                   host=host,
                                   database=database)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        logging.error("Something is wrong with your user name or password: %s", err)
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        logging.error("Database does not exist: %s", err)
    elif err.errno == errorcode.ER_HOSTNAME:
        logging.error("Hostname does not exist: %s", err)
    else:
        logging.error("An error occurred: %s", err)

cursor = cnx.cursor()

# Queries go here

add_band = ("INSERT INTO bands"
            "(name)"
            "VALUES (%s)")

data_band = ['Geert']

# cursor.execute(add_band, data_band)

cursor.execute("SELECT * FROM bands")

bands = cursor.fetchall()
for bands in bands:
    print(bands)

# Make sure data is committed to the database
cnx.commit()

# Until the connection and cursor are closed
cursor.close()
cnx.close()
