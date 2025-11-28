import psycopg2

DATA = ["Alignment", "Linux", "Python", "SQL from Python"]

conn = psycopg2.connect(
    dbname="kmorrin_db",
    user="kmorrin",
    password="changeme",
    host="localhost"
)

cur = conn.cursor()

for name in DATA:
    cur.execute(
        "INSERT INTO test_table (name) VALUES (%s);",
        (name,)
    )

conn.commit()
cur.close()
conn.close()

print("Inserted rows:", len(DATA))
