import time
import pymysql
import socket

db_host = "db"
db_port = 3306
db_user = "root"
db_password = "YourNewStrongPassword"

temporal_host = "temporal"
temporal_port = 7233

# Wait for MySQL
while True:
    try:
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            port=db_port,
        )
        conn.close()
        print("✅ Database is ready.")
        break
    except Exception as e:
        print(f"⏳ Waiting for database to be ready: {e}")
        time.sleep(2)

# Wait for Temporal
while True:
    try:
        s = socket.create_connection((temporal_host, temporal_port), timeout=5)
        s.close()
        print("✅ Temporal is ready.")
        break
    except Exception as e:
        print(f"⏳ Waiting for Temporal to be ready: {e}")
        time.sleep(2)
