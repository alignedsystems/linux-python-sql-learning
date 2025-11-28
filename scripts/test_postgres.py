import psycopg2

conn = psycopg2.connect(
    dbname="kmorrin_db",
    user="kmorrin",
    password="changeme",
    host="localhost"
)

cur = conn.cursor()
cur.execute("SELECT * FROM test_table;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
