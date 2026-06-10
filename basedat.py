import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Ganjarpantek123", database="perpustakaan")
cursor = db.cursor()

# Create
cursor.execute("INSERT INTO anggota (nama, no_hp, alamat) VALUES (%s, %s, %s)", ('Siti', '0857112233', 'Sidoarjo'))
db.commit()

# Read
cursor.execute("SELECT * FROM anggota")
for row in cursor.fetchall(): print(row)

# Update
cursor.execute("UPDATE anggota SET nama = %s WHERE id_anggota = %s", ('Siti Aminah', 2))
db.commit()

# Delete
cursor.execute("DELETE FROM anggota WHERE id_anggota = %s", (2,))
db.commit()