import mysql.connector
import os
from urllib.parse import urlparse

mysql_url = os.getenv("MYSQL_URL")

url = urlparse(mysql_url)

conn = mysql.connector.connect(
    host=url.hostname,
    user=url.username,
    password=url.password,
    database=url.path[1:],
    port=url.port
)

print("MySQL connected")
conn.close()
