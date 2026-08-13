import os
import shutil
from datetime import datetime


# =========================================================
# BACKUP FOLDER
# =========================================================

BACKUP_FOLDER = "backups"

if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)


# =========================================================
# CREATE BACKUP
# =========================================================

def create_backup():

    print("\n========================================")
    print("          CREATE PROJECT BACKUP")
    print("========================================")

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_name = "Backup_" + timestamp

    backup_path = os.path.join(
        BACKUP_FOLDER,
        backup_name
    )

    os.makedirs(
        backup_path,
        exist_ok=True
    )

    # -----------------------------------------------------
    # FILES TO BACKUP
    # -----------------------------------------------------

    files_to_backup = [
        "auth.py",
        "security.py",
        "evidence.py",
        "audit.py",
        "custody.py",
        "reports.py",
        "main.py",
        "database.py",
        "backup.py"
    ]

    copied_files = 0

    for file_name in files_to_backup:

        if os.path.isfile(file_name):

            shutil.copy2(
                file_name,
                backup_path
            )

            copied_files += 1

            print(
                "Backed up:",
                file_name
            )

    # -----------------------------------------------------
    # BACKUP EVIDENCE STORAGE
    # -----------------------------------------------------

    evidence_folder = "evidence_storage"

    if os.path.isdir(evidence_folder):

        storage_backup = os.path.join(
            backup_path,
            "evidence_storage"
        )

        shutil.copytree(
            evidence_folder,
            storage_backup,
            dirs_exist_ok=True
        )

        print(
            "Backed up: evidence_storage"
        )

    else:

        print(
            "evidence_storage folder not found."
        )

    # -----------------------------------------------------
    # BACKUP LOGS
    # -----------------------------------------------------

    logs_folder = "logs"

    if os.path.isdir(logs_folder):

        logs_backup = os.path.join(
            backup_path,
            "logs"
        )

        shutil.copytree(
            logs_folder,
            logs_backup,
            dirs_exist_ok=True
        )

        print(
            "Backed up: logs"
        )

    else:

        print(
            "logs folder not found."
        )

    # -----------------------------------------------------
    # BACKUP REPORTS
    # -----------------------------------------------------

    reports_folder = "reports"

    if os.path.isdir(reports_folder):

        reports_backup = os.path.join(
            backup_path,
            "reports"
        )

        shutil.copytree(
            reports_folder,
            reports_backup,
            dirs_exist_ok=True
        )

        print(
            "Backed up: reports"
        )

    else:

        print(
            "reports folder not found."
        )

    # -----------------------------------------------------
    # BACKUP SECRET KEY
    # -----------------------------------------------------

    if os.path.isfile("secret.key"):

        shutil.copy2(
            "secret.key",
            backup_path
        )

        print(
            "Backed up: secret.key"
        )

    # -----------------------------------------------------
    # BACKUP COMPLETE
    # -----------------------------------------------------

    print("\n========================================")
    print("       BACKUP CREATED SUCCESSFULLY")
    print("========================================")

    print(
        "Files backed up:",
        copied_files
    )

    print(
        "Backup location:",
        backup_path
    )

    return backup_path


# =========================================================
# VIEW BACKUPS
# =========================================================

def view_backups():

    print("\n========================================")
    print("            AVAILABLE BACKUPS")
    print("========================================")

    if not os.path.exists(BACKUP_FOLDER):

        print("\nNo backup folder found.")
        return

    backups = os.listdir(
        BACKUP_FOLDER
    )

    backup_folders = []

    for backup in backups:

        backup_path = os.path.join(
            BACKUP_FOLDER,
            backup
        )

        if os.path.isdir(backup_path):

            backup_folders.append(
                backup
            )

    if not backup_folders:

        print("\nNo backups found.")
        return

    for number, backup in enumerate(
        backup_folders,
        start=1
    ):

        print(
            str(number)
            + ". "
            + backup
        )


# =========================================================
# TEST MENU
# =========================================================

if __name__ == "__main__":

    while True:

        print("\n========================================")
        print("          BACKUP & RESTORE SYSTEM")
        print("========================================")

        print("1. Create Backup")
        print("2. View Backups")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            create_backup()

        elif choice == "2":

            view_backups()

        elif choice == "3":

            print(
                "\nExiting Backup System..."
            )

            break

        else:

            print(
                "\nInvalid choice! ❌"
            )