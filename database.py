import pyodbc
from datetime import datetime

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-SVFFVMG\\SQLEXPRESS;"
    "DATABASE=DigitalEvidenceDB;"
    "Trusted_Connection=yes;"
)

print("SQL Server Connected Successfully! ✅")

cursor = connection.cursor()

# Insert new evidence
cursor.execute("""
    INSERT INTO evidence
    (CaseID, FileName, UploadedBy, SHA256Hash, UploadDate)
    VALUES (?, ?, ?, ?, ?)
""",
"CASE004",
"CCTV_004.mp4",
"Investigator",
"samplehash004",
datetime.now()
)

connection.commit()

print("New evidence added successfully! ✅")

# Show all evidence
cursor.execute("SELECT * FROM evidence")

print("\nEvidence Records:")

for row in cursor.fetchall():
    print(row)

connection.close()