import os
from datetime import datetime


# =========================================================
# CHAIN OF CUSTODY FOLDER
# =========================================================

LOG_FOLDER = "logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


# =========================================================
# CHAIN OF CUSTODY FILE
# =========================================================

CUSTODY_FILE = os.path.join(
    LOG_FOLDER,
    "chain_of_custody.txt"
)


# =========================================================
# ADD CUSTODY RECORD
# =========================================================

def add_custody_record():

    print("\n========================================")
    print("          CHAIN OF CUSTODY")
    print("========================================")

    evidence_id = input(
        "Enter Evidence ID: "
    )

    username = input(
        "Enter Username: "
    )

    action = input(
        "Enter Action "
        "(Collected/Transferred/Examined/Stored): "
    )

    location = input(
        "Enter Evidence Location: "
    )

    notes = input(
        "Enter Notes: "
    )

    current_time = datetime.now()

    custody_record = (
        f"Date/Time: {current_time}\n"
        f"Evidence ID: {evidence_id}\n"
        f"User: {username}\n"
        f"Action: {action}\n"
        f"Location: {location}\n"
        f"Notes: {notes}\n"
        f"{'-' * 60}\n"
    )

    with open(
        CUSTODY_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(custody_record)

    print(
        "\nChain of Custody Record Added! ✅"
    )


# =========================================================
# VIEW CUSTODY RECORDS
# =========================================================

def view_custody_records():

    print("\n========================================")
    print("       CHAIN OF CUSTODY RECORDS")
    print("========================================")

    if not os.path.exists(CUSTODY_FILE):

        print("\nNo custody records found.")

        return

    with open(
        CUSTODY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        records = file.read()

    if records.strip():

        print(records)

    else:

        print("\nCustody file is empty.")


# =========================================================
# TEST MENU
# =========================================================

if __name__ == "__main__":

    while True:

        print("\n========================================")
        print("       DIGITAL EVIDENCE CUSTODY")
        print("========================================")

        print("1. Add Custody Record")
        print("2. View Custody Records")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            add_custody_record()

        elif choice == "2":

            view_custody_records()

        elif choice == "3":

            print(
                "\nExiting Chain of Custody..."
            )

            break

        else:

            print("\nInvalid choice! ❌")