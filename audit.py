import os
from datetime import datetime


# =========================================================
# LOGS FOLDER
# =========================================================

LOG_FOLDER = "logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


# =========================================================
# AUDIT LOG FILE
# =========================================================

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "audit_log.txt"
)


# =========================================================
# CREATE AUDIT LOG
# =========================================================

def create_audit_log(username, action, evidence_id=None):

    current_time = datetime.now()

    log_entry = (
        f"Date/Time: {current_time}\n"
        f"User: {username}\n"
        f"Action: {action}\n"
        f"Evidence ID: {evidence_id}\n"
        f"{'-' * 50}\n"
    )

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(log_entry)

    print("Audit Log Created Successfully! ✅")


# =========================================================
# VIEW AUDIT LOG
# =========================================================

def view_audit_log():

    print("\n========================================")
    print("              AUDIT LOG")
    print("========================================")

    if not os.path.exists(LOG_FILE):

        print("\nNo audit logs found.")

        return

    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        logs = file.read()

    if logs.strip():

        print(logs)

    else:

        print("\nAudit log is empty.")


# =========================================================
# CLEAR AUDIT LOG
# =========================================================

def clear_audit_log():

    if os.path.exists(LOG_FILE):

        open(
            LOG_FILE,
            "w",
            encoding="utf-8"
        ).close()

        print("\nAudit logs cleared successfully! ✅")

    else:

        print("\nNo audit log file exists.")


# =========================================================
# TEST MENU
# =========================================================

if __name__ == "__main__":

    while True:

        print("\n========================================")
        print("          AUDIT LOG SYSTEM")
        print("========================================")

        print("1. Create Audit Log")
        print("2. View Audit Logs")
        print("3. Clear Audit Logs")
        print("4. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            username = input(
                "Enter Username: "
            )

            action = input(
                "Enter Action: "
            )

            evidence_id = input(
                "Enter Evidence ID: "
            )

            create_audit_log(
                username,
                action,
                evidence_id
            )

        elif choice == "2":

            view_audit_log()

        elif choice == "3":

            clear_audit_log()

        elif choice == "4":

            print(
                "\nExiting Audit Log System..."
            )

            break

        else:

            print("\nInvalid choice! ❌")