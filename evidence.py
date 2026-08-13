import pyodbc
from security import calculate_file_hash
from datetime import datetime


# =========================================================
# SQL SERVER CONNECTION
# =========================================================

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-SVFFVMG\\SQLEXPRESS;"
    "DATABASE=DigitalEvidenceDB;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

print("SQL Server Connected Successfully! ✅")


# =========================================================
# ADD EVIDENCE
# =========================================================

def add_evidence():

    print("\n========================================")
    print("           ADD NEW EVIDENCE")
    print("========================================")

    case_id = input("Enter Case ID: ")
    file_path = input("Enter Evidence File Path: ")
    uploaded_by = input("Enter Uploaded By: ")

    # Check if file exists
    try:

        with open(file_path, "rb"):
            pass

    except FileNotFoundError:

        print("\nEvidence file not found! ❌")
        return

    # Get file name
    file_name = file_path.split("\\")[-1]

    # Calculate SHA-256 hash
    sha256_hash = calculate_file_hash(file_path)

    if sha256_hash is None:

        print("\nUnable to calculate file hash! ❌")
        return

    # Current date and time
    upload_date = datetime.now()

    # Save evidence into database
    try:

        cursor.execute("""
            INSERT INTO Evidence
            (
                CaseID,
                FileName,
                UploadedBy,
                SHA256Hash,
                UploadDate
            )
            VALUES (?, ?, ?, ?, ?)
        """,
        case_id,
        file_name,
        uploaded_by,
        sha256_hash,
        upload_date)

        connection.commit()

        print("\nEvidence Added Successfully! ✅")
        print("File Name:", file_name)
        print("SHA-256:", sha256_hash)

    except pyodbc.Error as error:

        print("\nDatabase Error! ❌")
        print(error)


# =========================================================
# SEARCH EVIDENCE
# =========================================================

def search_evidence():

    print("\n========================================")
    print("          SEARCH EVIDENCE")
    print("========================================")

    evidence_id = input("Enter Evidence ID: ")

    cursor.execute("""
        SELECT
            EvidenceID,
            CaseID,
            FileName,
            UploadedBy,
            SHA256Hash,
            UploadDate
        FROM Evidence
        WHERE EvidenceID = ?
    """,
    evidence_id)

    evidence = cursor.fetchone()

    if evidence:

        print("\nEvidence Found! ✅")
        print("----------------------------------------")
        print("Evidence ID:", evidence.EvidenceID)
        print("Case ID:", evidence.CaseID)
        print("File Name:", evidence.FileName)
        print("Uploaded By:", evidence.UploadedBy)
        print("SHA-256:", evidence.SHA256Hash)
        print("Upload Date:", evidence.UploadDate)
        print("----------------------------------------")

    else:

        print("\nEvidence not found! ❌")


# =========================================================
# SHOW ALL EVIDENCE
# =========================================================

def show_all_evidence():

    print("\n========================================")
    print("             ALL EVIDENCE")
    print("========================================")

    cursor.execute("""
        SELECT
            EvidenceID,
            CaseID,
            FileName,
            UploadedBy,
            SHA256Hash,
            UploadDate
        FROM Evidence
    """)

    records = cursor.fetchall()

    if not records:

        print("\nNo evidence records found.")
        return

    for record in records:

        print("\n----------------------------------------")
        print("Evidence ID:", record.EvidenceID)
        print("Case ID:", record.CaseID)
        print("File Name:", record.FileName)
        print("Uploaded By:", record.UploadedBy)
        print("SHA-256:", record.SHA256Hash)
        print("Upload Date:", record.UploadDate)


# =========================================================
# CLOSE DATABASE
# =========================================================

def close_connection():

    if connection:

        connection.close()

        print("\nDatabase Connection Closed. ✅")


# =========================================================
# TEST MENU
# =========================================================

if __name__ == "__main__":

    while True:

        print("\n========================================")
        print("       DIGITAL EVIDENCE MANAGEMENT")
        print("========================================")

        print("1. Add Evidence")
        print("2. Search Evidence")
        print("3. Show All Evidence")
        print("4. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            add_evidence()

        elif choice == "2":

            search_evidence()

        elif choice == "3":

            show_all_evidence()

        elif choice == "4":

            print(
                "\nExiting Evidence Management..."
            )

            close_connection()

            break

        else:

            print("\nInvalid choice! ❌")