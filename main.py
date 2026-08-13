# =========================================================
# DIGITAL EVIDENCE MANAGEMENT SYSTEM
# FINAL MAIN FILE
# =========================================================

import auth
import evidence
import security
import audit
import custody
import reports
import backup


# =========================================================
# CHECK PERMISSION
# =========================================================

def allowed(user, permission):

    if user is None:
        print("\nPlease login first! ❌")
        return False

    if not auth.has_permission(user, permission):

        print(
            "\nAccess Denied! ❌"
        )

        print(
            "Your role does not have permission "
            "for this action."
        )

        return False

    return True


# =========================================================
# MAIN SYSTEM
# =========================================================

def main():

    print("\n========================================")
    print("     DIGITAL EVIDENCE MANAGEMENT")
    print("========================================")
    print("       SECURE FORENSIC SYSTEM")
    print("========================================")

    current_user = None

    while True:

        # -------------------------------------------------
        # LOGIN MENU
        # -------------------------------------------------

        if current_user is None:

            print("\n========================================")
            print("              LOGIN MENU")
            print("========================================")

            print("1. Login")
            print("2. Create User")
            print("3. Exit")

            choice = input(
                "\nEnter your choice: "
            )

            if choice == "1":

                current_user = auth.login()

                if current_user:

                    print(
                        "\nWelcome to Digital Evidence System! 🔐"
                    )

            elif choice == "2":

                auth.create_user()

            elif choice == "3":

                print(
                    "\nExiting Digital Evidence System..."
                )

                break

            else:

                print(
                    "\nInvalid choice! ❌"
                )

            continue

        # -------------------------------------------------
        # USER INFORMATION
        # -------------------------------------------------

        print("\n========================================")
        print("       DIGITAL EVIDENCE SYSTEM")
        print("========================================")

        print(
            "Logged in user:",
            current_user.Username
        )

        print(
            "Role:",
            current_user.Role
        )

        print("========================================")

        # -------------------------------------------------
        # MAIN MENU
        # -------------------------------------------------

        print("\n1. Add Evidence")
        print("2. Search Evidence")
        print("3. Show All Evidence")
        print("4. Calculate SHA-256")
        print("5. Verify Evidence Integrity")
        print("6. Encrypt Evidence")
        print("7. Decrypt Evidence")
        print("8. Add Chain of Custody Record")
        print("9. View Chain of Custody")
        print("10. View Audit Logs")
        print("11. Generate Evidence Report")
        print("12. View Reports")
        print("13. Create Backup")
        print("14. View Backups")
        print("15. Show My Permissions")
        print("16. Logout")
        print("17. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        # =================================================
        # 1. ADD EVIDENCE
        # =================================================

        if choice == "1":

            if allowed(
                current_user,
                "add_evidence"
            ):

                evidence.add_evidence()

                audit.create_audit_log(
                    current_user.Username,
                    "Added Evidence"
                )

        # =================================================
        # 2. SEARCH EVIDENCE
        # =================================================

        elif choice == "2":

            if allowed(
                current_user,
                "search_evidence"
            ):

                evidence.search_evidence()

                audit.create_audit_log(
                    current_user.Username,
                    "Searched Evidence"
                )

        # =================================================
        # 3. SHOW ALL EVIDENCE
        # =================================================

        elif choice == "3":

            if allowed(
                current_user,
                "view_evidence"
            ):

                evidence.show_all_evidence()

                audit.create_audit_log(
                    current_user.Username,
                    "Viewed All Evidence"
                )

        # =================================================
        # 4. CALCULATE SHA-256
        # =================================================

        elif choice == "4":

            if allowed(
                current_user,
                "verify_integrity"
            ):

                file_path = input(
                    "Enter evidence file path: "
                )

                file_hash = (
                    security.calculate_file_hash(
                        file_path
                    )
                )

                if file_hash:

                    print("\nSHA-256 Hash:")
                    print(file_hash)

                    audit.create_audit_log(
                        current_user.Username,
                        "Calculated SHA-256 Hash"
                    )

        # =================================================
        # 5. VERIFY INTEGRITY
        # =================================================

        elif choice == "5":

            if allowed(
                current_user,
                "verify_integrity"
            ):

                file_path = input(
                    "Enter evidence file path: "
                )

                original_hash = input(
                    "Enter original SHA-256 hash: "
                )

                security.verify_file_integrity(
                    file_path,
                    original_hash
                )

                audit.create_audit_log(
                    current_user.Username,
                    "Verified Evidence Integrity"
                )

        # =================================================
        # 6. ENCRYPT EVIDENCE
        # =================================================

        elif choice == "6":

            if allowed(
                current_user,
                "encrypt_evidence"
            ):

                file_path = input(
                    "Enter evidence file path: "
                )

                security.encrypt_file(
                    file_path
                )

                audit.create_audit_log(
                    current_user.Username,
                    "Encrypted Evidence"
                )

        # =================================================
        # 7. DECRYPT EVIDENCE
        # =================================================

        elif choice == "7":

            if allowed(
                current_user,
                "decrypt_evidence"
            ):

                encrypted_path = input(
                    "Enter encrypted file path: "
                )

                security.decrypt_file(
                    encrypted_path
                )

                audit.create_audit_log(
                    current_user.Username,
                    "Decrypted Evidence"
                )

        # =================================================
        # 8. ADD CHAIN OF CUSTODY
        # =================================================

        elif choice == "8":

            if allowed(
                current_user,
                "chain_of_custody"
            ):

                custody.add_custody_record()

                audit.create_audit_log(
                    current_user.Username,
                    "Added Chain of Custody Record"
                )

        # =================================================
        # 9. VIEW CHAIN OF CUSTODY
        # =================================================

        elif choice == "9":

            if allowed(
                current_user,
                "chain_of_custody"
            ):

                custody.view_custody_records()

                audit.create_audit_log(
                    current_user.Username,
                    "Viewed Chain of Custody"
                )

        # =================================================
        # 10. VIEW AUDIT LOGS
        # =================================================

        elif choice == "10":

            if allowed(
                current_user,
                "view_audit_logs"
            ):

                audit.view_audit_log()

        # =================================================
        # 11. GENERATE REPORT
        # =================================================

        elif choice == "11":

            if allowed(
                current_user,
                "generate_reports"
            ):

                reports.generate_report()

                audit.create_audit_log(
                    current_user.Username,
                    "Generated Evidence Report"
                )

        # =================================================
        # 12. VIEW REPORTS
        # =================================================

        elif choice == "12":

            if allowed(
                current_user,
                "generate_reports"
            ):

                reports.view_reports()

                audit.create_audit_log(
                    current_user.Username,
                    "Viewed Reports"
                )

        # =================================================
        # 13. CREATE BACKUP
        # =================================================

        elif choice == "13":

            if allowed(
                current_user,
                "create_backup"
            ):

                backup.create_backup()

                audit.create_audit_log(
                    current_user.Username,
                    "Created System Backup"
                )

        # =================================================
        # 14. VIEW BACKUPS
        # =================================================

        elif choice == "14":

            if allowed(
                current_user,
                "view_backups"
            ):

                backup.view_backups()

                audit.create_audit_log(
                    current_user.Username,
                    "Viewed Backups"
                )

        # =================================================
        # 15. SHOW PERMISSIONS
        # =================================================

        elif choice == "15":

            auth.show_permissions(
                current_user
            )

        # =================================================
        # 16. LOGOUT
        # =================================================

        elif choice == "16":

            audit.create_audit_log(
                current_user.Username,
                "User Logged Out"
            )

            current_user = None

            print(
                "\nLogged out successfully! ✅"
            )

        # =================================================
        # 17. EXIT
        # =================================================

        elif choice == "17":

            audit.create_audit_log(
                current_user.Username,
                "System Closed"
            )

            print(
                "\n========================================"
            )

            print(
                "   DIGITAL EVIDENCE SYSTEM CLOSED"
            )

            print(
                "========================================"
            )

            break

        # =================================================
        # INVALID CHOICE
        # =================================================

        else:

            print(
                "\nInvalid choice! ❌"
            )


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print(
            "\n\nProgram interrupted by user."
        )

    except Exception as error:

        print(
            "\nSystem Error! ❌"
        )

        print(error)