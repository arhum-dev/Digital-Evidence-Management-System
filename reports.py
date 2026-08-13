import pyodbc
import os
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
# REPORTS FOLDER
# =========================================================

REPORT_FOLDER = "reports"

if not os.path.exists(REPORT_FOLDER):
    os.makedirs(REPORT_FOLDER)


# =========================================================
# GENERATE EVIDENCE REPORT
# =========================================================

def generate_report():

    print("\n========================================")
    print("        GENERATE EVIDENCE REPORT")
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
        ORDER BY EvidenceID
    """)

    records = cursor.fetchall()

    if not records:

        print("\nNo evidence records found! ❌")
        return

    current_time = datetime.now()

    report_name = (
        "Evidence_Report_"
        + current_time.strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )

    report_path = os.path.join(
        REPORT_FOLDER,
        report_name
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as report:

        report.write("=" * 70 + "\n")
        report.write(
            "        DIGITAL EVIDENCE MANAGEMENT SYSTEM\n"
        )
        report.write(
            "              EVIDENCE REPORT\n"
        )
        report.write("=" * 70 + "\n\n")

        report.write(
            "Report Generated: "
            + str(current_time)
            + "\n\n"
        )

        report.write(
            "Total Evidence Records: "
            + str(len(records))
            + "\n\n"
        )

        report.write("-" * 70 + "\n")

        for record in records:

            report.write("\n")
            report.write(
                "Evidence ID: "
                + str(record.EvidenceID)
                + "\n"
            )

            report.write(
                "Case ID: "
                + str(record.CaseID)
                + "\n"
            )

            report.write(
                "File Name: "
                + str(record.FileName)
                + "\n"
            )

            report.write(
                "Uploaded By: "
                + str(record.UploadedBy)
                + "\n"
            )

            report.write(
                "SHA-256 Hash: "
                + str(record.SHA256Hash)
                + "\n"
            )

            report.write(
                "Upload Date: "
                + str(record.UploadDate)
                + "\n"
            )

            report.write("-" * 70 + "\n")

    print(
        "\nEvidence Report Generated Successfully! ✅"
    )

    print("Report saved at:")
    print(report_path)


# =========================================================
# VIEW REPORTS
# =========================================================

def view_reports():

    print("\n========================================")
    print("             AVAILABLE REPORTS")
    print("========================================")

    if not os.path.exists(REPORT_FOLDER):

        print("\nReports folder does not exist.")
        return

    files = os.listdir(REPORT_FOLDER)

    report_files = [
        file
        for file in files
        if file.endswith(".txt")
    ]

    if not report_files:

        print("\nNo reports found.")
        return

    for number, file in enumerate(
        report_files,
        start=1
    ):

        print(
            str(number)
            + ". "
            + file
        )


# =========================================================
# CLOSE DATABASE CONNECTION
# =========================================================

def close_connection():

    if connection:

        connection.close()

        print(
            "\nDatabase Connection Closed. ✅"
        )


# =========================================================
# TEST MENU
# =========================================================

if __name__ == "__main__":

    while True:

        print("\n========================================")
        print("          EVIDENCE REPORT SYSTEM")
        print("========================================")

        print("1. Generate Evidence Report")
        print("2. View Available Reports")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            generate_report()

        elif choice == "2":

            view_reports()

        elif choice == "3":

            print(
                "\nExiting Report System..."
            )

            close_connection()

            break

        else:

            print("\nInvalid choice! ❌")