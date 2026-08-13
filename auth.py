import pyodbc
import hashlib
import getpass


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
# CREATE USERS TABLE
# =========================================================

cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM sysobjects
    WHERE name='Users' AND xtype='U'
)
CREATE TABLE Users
(
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    PasswordHash VARCHAR(64) NOT NULL,
    Role VARCHAR(50) NOT NULL
)
""")

connection.commit()


# =========================================================
# PASSWORD HASH FUNCTION
# =========================================================

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# =========================================================
# CREATE USER
# =========================================================

def create_user():

    print("\n========================================")
    print("           CREATE NEW USER")
    print("========================================")

    username = input("Enter Username: ")

    password = getpass.getpass(
        "Enter Password: "
    )

    print("\nAvailable Roles:")
    print("1. Admin")
    print("2. Investigator")
    print("3. Forensic Officer")

    role_choice = input(
        "\nSelect Role: "
    )

    if role_choice == "1":
        role = "Admin"

    elif role_choice == "2":
        role = "Investigator"

    elif role_choice == "3":
        role = "Forensic Officer"

    else:
        print("\nInvalid Role! ❌")
        return

    password_hash = hash_password(password)

    try:

        cursor.execute("""
            INSERT INTO Users
            (Username, PasswordHash, Role)
            VALUES (?, ?, ?)
        """,
        username,
        password_hash,
        role)

        connection.commit()

        print("\nUser Created Successfully! ✅")
        print("Username:", username)
        print("Role:", role)

    except pyodbc.IntegrityError:

        print("\nUsername already exists! ❌")


# =========================================================
# LOGIN FUNCTION
# =========================================================

def login():

    print("\n========================================")
    print("       DIGITAL EVIDENCE LOGIN")
    print("========================================")

    username = input("Username: ")

    password = getpass.getpass(
        "Password: "
    )

    password_hash = hash_password(password)

    cursor.execute("""
        SELECT UserID, Username, Role
        FROM Users
        WHERE Username = ?
        AND PasswordHash = ?
    """,
    username,
    password_hash)

    user = cursor.fetchone()

    if user:

        print("\nLogin Successful! ✅")
        print("Welcome:", user.Username)
        print("Role:", user.Role)

        return user

    else:

        print("\nInvalid Username or Password! ❌")

        return None


# =========================================================
# ROLE PERMISSIONS
# =========================================================

ROLE_PERMISSIONS = {

    "Admin": [
        "add_evidence",
        "search_evidence",
        "view_evidence",
        "verify_integrity",
        "view_audit_logs",
        "chain_of_custody",
        "generate_reports",
        "create_backup",
        "view_backups",
        "encrypt_evidence",
        "decrypt_evidence",
        "manage_users"
    ],

    "Investigator": [
        "add_evidence",
        "search_evidence",
        "view_evidence",
        "chain_of_custody",
        "generate_reports"
    ],

    "Forensic Officer": [
        "search_evidence",
        "view_evidence",
        "verify_integrity",
        "chain_of_custody",
        "generate_reports",
        "encrypt_evidence",
        "decrypt_evidence"
    ]
}


# =========================================================
# CHECK PERMISSION
# =========================================================

def has_permission(user, permission):

    if user is None:
        return False

    role = user.Role

    permissions = ROLE_PERMISSIONS.get(
        role,
        []
    )

    return permission in permissions


# =========================================================
# SHOW USER PERMISSIONS
# =========================================================

def show_permissions(user):

    if user is None:

        print("\nNo user logged in! ❌")
        return

    role = user.Role

    permissions = ROLE_PERMISSIONS.get(
        role,
        []
    )

    print("\n========================================")
    print("          USER PERMISSIONS")
    print("========================================")

    print("Username:", user.Username)
    print("Role:", role)

    print("\nAllowed Actions:")

    for permission in permissions:

        print("✓", permission)


# =========================================================
# TEST MENU
# =========================================================

if __name__ == "__main__":

    current_user = None

    while True:

        print("\n========================================")
        print("       AUTHENTICATION SYSTEM")
        print("========================================")

        print("1. Create User")
        print("2. Login")
        print("3. Show My Permissions")
        print("4. Logout")
        print("5. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            create_user()

        elif choice == "2":

            current_user = login()

        elif choice == "3":

            show_permissions(current_user)

        elif choice == "4":

            current_user = None

            print("\nLogged out successfully! ✅")

        elif choice == "5":

            print(
                "\nExiting Authentication System..."
            )

            connection.close()

            print(
                "Database Connection Closed. ✅"
            )

            break

        else:

            print("\nInvalid choice! ❌")