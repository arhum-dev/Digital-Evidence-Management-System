# =========================================================
# DIGITAL EVIDENCE MANAGEMENT SYSTEM
# FINAL GUI
# =========================================================

import tkinter as tk
from tkinter import messagebox, filedialog
import os
from datetime import datetime

import auth
import evidence
import security
import audit
import custody
import reports
import backup


# =========================================================
# COLORS
# =========================================================

NAVY = "#0B1F3A"
DARK_BLUE = "#071525"
BLUE = "#1E5AA8"
LIGHT_BLUE = "#D6E4F0"
WHITE = "#FFFFFF"
GREEN = "#198754"
RED = "#B02A37"
GRAY = "#6C757D"


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Digital Evidence Management System")
root.geometry("1050x700")
root.resizable(False, False)
root.configure(bg=NAVY)


# =========================================================
# GLOBAL USER
# =========================================================

current_user = None
dashboard_frame = None


# =========================================================
# CLEAR WINDOW
# =========================================================

def clear_window():

    for widget in root.winfo_children():
        widget.destroy()


# =========================================================
# HEADER
# =========================================================

def create_header(title_text, subtitle_text=""):

    title = tk.Label(
        root,
        text=title_text,
        font=("Arial", 25, "bold"),
        bg=NAVY,
        fg=WHITE
    )

    title.pack(pady=(30, 5))

    if subtitle_text:

        subtitle = tk.Label(
            root,
            text=subtitle_text,
            font=("Arial", 12),
            bg=NAVY,
            fg=LIGHT_BLUE
        )

        subtitle.pack(pady=(0, 20))


# =========================================================
# TEXT OUTPUT WINDOW
# =========================================================

def show_text_window(title, text, width=85, height=25):

    window = tk.Toplevel(root)

    window.title(title)
    window.geometry("850x550")
    window.configure(bg=NAVY)

    label = tk.Label(
        window,
        text=title,
        font=("Arial", 18, "bold"),
        bg=NAVY,
        fg=WHITE
    )

    label.pack(pady=15)

    text_box = tk.Text(
        window,
        width=width,
        height=height,
        font=("Consolas", 10),
        bg=WHITE,
        fg="#111111",
        wrap="none"
    )

    text_box.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    text_box.insert(
        "1.0",
        text
    )

    text_box.config(
        state="disabled"
    )

    close_button = tk.Button(
        window,
        text="CLOSE",
        command=window.destroy,
        width=15,
        font=("Arial", 10, "bold"),
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    )

    close_button.pack(pady=15)


# =========================================================
# PERMISSION CHECK
# =========================================================

def allowed(permission):

    global current_user

    if current_user is None:

        messagebox.showwarning(
            "Login Required",
            "Please login first."
        )

        return False

    if not auth.has_permission(
        current_user,
        permission
    ):

        messagebox.showerror(
            "Access Denied",
            "Your role does not have permission "
            "for this action."
        )

        return False

    return True


# =========================================================
# LOGIN
# =========================================================

def login():

    global current_user

    username = username_entry.get().strip()
    password = password_entry.get()

    if username == "" or password == "":

        messagebox.showwarning(
            "Login",
            "Please enter username and password."
        )

        return

    try:

        password_hash = auth.hash_password(
            password
        )

        auth.cursor.execute(
            """
            SELECT UserID, Username, Role
            FROM Users
            WHERE Username = ?
            AND PasswordHash = ?
            """,
            username,
            password_hash
        )

        user = auth.cursor.fetchone()

        if user:

            current_user = user

            audit.create_audit_log(
                current_user.Username,
                "User Logged In"
            )

            messagebox.showinfo(
                "Login Successful",
                f"Welcome {user.Username}!\n\n"
                f"Role: {user.Role}"
            )

            show_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password."
            )

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# =========================================================
# DASHBOARD
# =========================================================

def show_dashboard():

    global dashboard_frame

    clear_window()

    dashboard_frame = tk.Frame(
        root,
        bg=NAVY
    )

    dashboard_frame.pack(
        fill="both",
        expand=True
    )

    tk.Label(
        dashboard_frame,
        text="DIGITAL EVIDENCE MANAGEMENT SYSTEM",
        font=("Arial", 25, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(
        pady=(25, 5)
    )

    tk.Label(
        dashboard_frame,
        text=(
            f"Welcome, {current_user.Username}   |   "
            f"Role: {current_user.Role}"
        ),
        font=("Arial", 12),
        bg=NAVY,
        fg=LIGHT_BLUE
    ).pack(
        pady=(0, 10)
    )

    tk.Label(
        dashboard_frame,
        text="MAIN DASHBOARD",
        font=("Arial", 18, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(
        pady=10
    )

    button_frame = tk.Frame(
        dashboard_frame,
        bg=NAVY
    )

    button_frame.pack(
        pady=5
    )

    buttons = [

        ("Add Evidence", add_evidence_gui),

        ("Search Evidence", search_evidence_gui),

        ("Show All Evidence", show_all_evidence_gui),

        ("Calculate SHA-256", calculate_hash_gui),

        ("Verify Integrity", verify_integrity_gui),

        ("Encrypt Evidence", encrypt_evidence_gui),

        ("Decrypt Evidence", decrypt_evidence_gui),

        ("Chain of Custody", custody_gui),

        ("Audit Logs", audit_gui),

        ("Generate Report", generate_report_gui),

        ("View Reports", view_reports_gui),

        ("Create Backup", create_backup_gui),

        ("View Backups", view_backups_gui),

        ("My Permissions", permissions_gui),

        ("Logout", logout_user)

    ]

    for index, (text, command) in enumerate(buttons):

        row = index // 3
        column = index % 3

        button = tk.Button(
            button_frame,
            text=text,
            command=command,
            width=24,
            height=2,
            font=("Arial", 10, "bold"),
            bg=BLUE,
            fg=WHITE,
            activebackground="#174A8A",
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2"
        )

        button.grid(
            row=row,
            column=column,
            padx=8,
            pady=7
        )

    tk.Label(
        dashboard_frame,
        text=(
            "Digital Forensics • Evidence Integrity • "
            "Chain of Custody"
        ),
        font=("Arial", 9),
        bg=NAVY,
        fg=LIGHT_BLUE
    ).pack(
        side="bottom",
        pady=15
    )


# =========================================================
# ADD EVIDENCE
# =========================================================

def add_evidence_gui():

    if not allowed("add_evidence"):
        return

    window = tk.Toplevel(root)

    window.title("Add Evidence")
    window.geometry("650x450")
    window.configure(bg=NAVY)

    tk.Label(
        window,
        text="ADD NEW EVIDENCE",
        font=("Arial", 20, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(pady=20)

    form = tk.Frame(
        window,
        bg=NAVY
    )

    form.pack(pady=10)

    tk.Label(
        form,
        text="Case ID:",
        font=("Arial", 11, "bold"),
        bg=NAVY,
        fg=WHITE
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    case_entry = tk.Entry(
        form,
        width=35,
        font=("Arial", 11)
    )

    case_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    tk.Label(
        form,
        text="Evidence File:",
        font=("Arial", 11, "bold"),
        bg=NAVY,
        fg=WHITE
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    file_entry = tk.Entry(
        form,
        width=35,
        font=("Arial", 11)
    )

    file_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    def browse_file():

        path = filedialog.askopenfilename(
            title="Select Evidence File"
        )

        if path:

            file_entry.delete(
                0,
                tk.END
            )

            file_entry.insert(
                0,
                path
            )

    tk.Button(
        form,
        text="Browse",
        command=browse_file,
        bg=GRAY,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).grid(
        row=1,
        column=2,
        padx=5
    )

    tk.Label(
        form,
        text="Uploaded By:",
        font=("Arial", 11, "bold"),
        bg=NAVY,
        fg=WHITE
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=10
    )

    uploaded_entry = tk.Entry(
        form,
        width=35,
        font=("Arial", 11)
    )

    uploaded_entry.insert(
        0,
        current_user.Username
    )

    uploaded_entry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    def save_evidence():

        case_id = case_entry.get().strip()
        file_path = file_entry.get().strip()
        uploaded_by = uploaded_entry.get().strip()

        if not case_id or not file_path:

            messagebox.showwarning(
                "Missing Information",
                "Please enter Case ID and select an evidence file."
            )

            return

        if not os.path.isfile(file_path):

            messagebox.showerror(
                "File Not Found",
                "Evidence file does not exist."
            )

            return

        try:

            file_name = os.path.basename(
                file_path
            )

            sha256_hash = security.calculate_file_hash(
                file_path
            )

            if not sha256_hash:

                messagebox.showerror(
                    "Hash Error",
                    "Unable to calculate SHA-256."
                )

                return

            evidence.cursor.execute(
                """
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
                datetime.now()
            )

            evidence.connection.commit()

            audit.create_audit_log(
                current_user.Username,
                "Added Evidence"
            )

            messagebox.showinfo(
                "Success",
                "Evidence Added Successfully! ✅\n\n"
                f"File: {file_name}\n\n"
                f"SHA-256:\n{sha256_hash}"
            )

            window.destroy()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    tk.Button(
        window,
        text="ADD EVIDENCE",
        command=save_evidence,
        width=20,
        font=("Arial", 11, "bold"),
        bg=GREEN,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack(
        pady=25
    )


# =========================================================
# SEARCH EVIDENCE
# =========================================================

def search_evidence_gui():

    if not allowed("search_evidence"):
        return

    window = tk.Toplevel(root)

    window.title("Search Evidence")
    window.geometry("650x450")
    window.configure(bg=NAVY)

    tk.Label(
        window,
        text="SEARCH EVIDENCE",
        font=("Arial", 20, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(pady=25)

    tk.Label(
        window,
        text="Evidence ID:",
        font=("Arial", 11, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack()

    entry = tk.Entry(
        window,
        width=30,
        font=("Arial", 12)
    )

    entry.pack(pady=10)

    def search():

        evidence_id = entry.get().strip()

        if not evidence_id:

            messagebox.showwarning(
                "Missing ID",
                "Please enter Evidence ID."
            )

            return

        try:

            evidence.cursor.execute(
                """
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
                evidence_id
            )

            record = evidence.cursor.fetchone()

            if record:

                result = (
                    f"Evidence ID: {record.EvidenceID}\n"
                    f"Case ID: {record.CaseID}\n"
                    f"File Name: {record.FileName}\n"
                    f"Uploaded By: {record.UploadedBy}\n"
                    f"SHA-256: {record.SHA256Hash}\n"
                    f"Upload Date: {record.UploadDate}"
                )

                show_text_window(
                    "Evidence Found",
                    result,
                    width=75,
                    height=15
                )

                audit.create_audit_log(
                    current_user.Username,
                    "Searched Evidence",
                    evidence_id
                )

            else:

                messagebox.showerror(
                    "Not Found",
                    "Evidence record not found."
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    tk.Button(
        window,
        text="SEARCH",
        command=search,
        width=18,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack(pady=20)


# =========================================================
# SHOW ALL EVIDENCE
# =========================================================

def show_all_evidence_gui():

    if not allowed("view_evidence"):
        return

    try:

        evidence.cursor.execute(
            """
            SELECT
                EvidenceID,
                CaseID,
                FileName,
                UploadedBy,
                SHA256Hash,
                UploadDate
            FROM Evidence
            ORDER BY EvidenceID
            """
        )

        records = evidence.cursor.fetchall()

        if not records:

            messagebox.showinfo(
                "Evidence",
                "No evidence records found."
            )

            return

        output = ""

        for record in records:

            output += (
                "----------------------------------------\n"
                f"Evidence ID: {record.EvidenceID}\n"
                f"Case ID: {record.CaseID}\n"
                f"File Name: {record.FileName}\n"
                f"Uploaded By: {record.UploadedBy}\n"
                f"SHA-256: {record.SHA256Hash}\n"
                f"Upload Date: {record.UploadDate}\n"
            )

        show_text_window(
            "All Evidence",
            output,
            width=85,
            height=25
        )

        audit.create_audit_log(
            current_user.Username,
            "Viewed All Evidence"
        )

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# =========================================================
# CALCULATE SHA-256
# =========================================================

def calculate_hash_gui():

    if not allowed("verify_integrity"):
        return

    file_path = filedialog.askopenfilename(
        title="Select Evidence File"
    )

    if not file_path:
        return

    try:

        file_hash = security.calculate_file_hash(
            file_path
        )

        if file_hash:

            messagebox.showinfo(
                "SHA-256 Hash",
                f"File:\n"
                f"{os.path.basename(file_path)}\n\n"
                f"SHA-256:\n"
                f"{file_hash}\n\n"
                f"Length: {len(file_hash)} characters"
            )

            audit.create_audit_log(
                current_user.Username,
                "Calculated SHA-256 Hash"
            )

    except Exception as error:

        messagebox.showerror(
            "Hash Error",
            str(error)
        )


# =========================================================
# VERIFY EVIDENCE INTEGRITY
# =========================================================

def verify_integrity_gui():

    if not allowed("verify_integrity"):
        return

    window = tk.Toplevel(root)

    window.title("Verify Evidence Integrity")
    window.geometry("700x500")
    window.configure(bg=NAVY)

    tk.Label(
        window,
        text="VERIFY EVIDENCE INTEGRITY",
        font=("Arial", 20, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(pady=20)

    tk.Label(
        window,
        text="Evidence File:",
        font=("Arial", 11, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack()

    file_entry = tk.Entry(
        window,
        width=70,
        font=("Arial", 10)
    )

    file_entry.pack(pady=8)

    def browse():

        path = filedialog.askopenfilename(
            title="Select Evidence File"
        )

        if path:

            file_entry.delete(
                0,
                tk.END
            )

            file_entry.insert(
                0,
                path
            )

    tk.Button(
        window,
        text="Browse",
        command=browse,
        width=12,
        bg=GRAY,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack()

    tk.Label(
        window,
        text="Original SHA-256 Hash:",
        font=("Arial", 11, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(pady=(25, 5))

    hash_entry = tk.Entry(
        window,
        width=70,
        font=("Arial", 10)
    )

    hash_entry.pack(pady=8)

    def verify():

        file_path = file_entry.get().strip()

        original_hash = (
            hash_entry.get()
            .strip()
            .lower()
        )

        if not file_path:

            messagebox.showwarning(
                "Missing File",
                "Please select an evidence file."
            )

            return

        if not original_hash:

            messagebox.showwarning(
                "Missing Hash",
                "Please enter the original SHA-256 hash."
            )

            return

        if len(original_hash) != 64:

            messagebox.showerror(
                "Invalid SHA-256",
                f"SHA-256 must contain exactly 64 characters.\n\n"
                f"You entered: {len(original_hash)} characters."
            )

            return

        if not os.path.isfile(file_path):

            messagebox.showerror(
                "File Not Found",
                "Evidence file was not found."
            )

            return

        try:

            current_hash = security.calculate_file_hash(
                file_path
            )

            if not current_hash:

                messagebox.showerror(
                    "Hash Error",
                    "Unable to calculate SHA-256."
                )

                return

            current_hash = (
                current_hash
                .strip()
                .lower()
            )

            if len(current_hash) != 64:

                messagebox.showerror(
                    "Hash Error",
                    "Security module returned an invalid SHA-256 hash."
                )

                return

            if current_hash == original_hash:

                messagebox.showinfo(
                    "INTEGRITY VERIFIED",
                    "EVIDENCE INTEGRITY VERIFIED! ✅\n\n"
                    "The file has NOT been modified.\n\n"
                    f"Current SHA-256:\n{current_hash}\n\n"
                    f"Original SHA-256:\n{original_hash}"
                )

                audit.create_audit_log(
                    current_user.Username,
                    "Verified Evidence Integrity"
                )

            else:

                messagebox.showwarning(
                    "EVIDENCE MODIFIED",
                    "WARNING: Evidence File Has Been Modified! ❌\n\n"
                    f"Current SHA-256:\n{current_hash}\n\n"
                    f"Original SHA-256:\n{original_hash}"
                )

                audit.create_audit_log(
                    current_user.Username,
                    "Evidence Integrity Warning"
                )

        except Exception as error:

            messagebox.showerror(
                "Verification Error",
                str(error)
            )

    tk.Button(
        window,
        text="VERIFY INTEGRITY",
        command=verify,
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack(pady=25)


# =========================================================
# ENCRYPT EVIDENCE
# =========================================================

def encrypt_evidence_gui():

    if not allowed("encrypt_evidence"):
        return

    file_path = filedialog.askopenfilename(
        title="Select Evidence File"
    )

    if not file_path:
        return

    try:

        encrypted_path = security.encrypt_file(
            file_path
        )

        if encrypted_path:

            audit.create_audit_log(
                current_user.Username,
                "Encrypted Evidence"
            )

            messagebox.showinfo(
                "Encryption Successful",
                "Evidence encrypted successfully! 🔒\n\n"
                f"Encrypted file:\n{encrypted_path}"
            )

    except Exception as error:

        messagebox.showerror(
            "Encryption Error",
            str(error)
        )


# =========================================================
# DECRYPT EVIDENCE
# =========================================================

def decrypt_evidence_gui():

    if not allowed("decrypt_evidence"):
        return

    file_path = filedialog.askopenfilename(
        title="Select Encrypted Evidence",
        filetypes=[
            ("Encrypted Files", "*.encrypted"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:

        decrypted_path = security.decrypt_file(
            file_path
        )

        if decrypted_path:

            audit.create_audit_log(
                current_user.Username,
                "Decrypted Evidence"
            )

            messagebox.showinfo(
                "Decryption Successful",
                "Evidence decrypted successfully! 🔓\n\n"
                f"Decrypted file:\n{decrypted_path}"
            )

    except Exception as error:

        messagebox.showerror(
            "Decryption Error",
            str(error)
        )


# =========================================================
# CHAIN OF CUSTODY
# =========================================================

def custody_gui():

    if not allowed("chain_of_custody"):
        return

    window = tk.Toplevel(root)

    window.title("Chain of Custody")
    window.geometry("700x600")
    window.configure(bg=NAVY)

    tk.Label(
        window,
        text="CHAIN OF CUSTODY",
        font=("Arial", 20, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(pady=20)

    form = tk.Frame(
        window,
        bg=NAVY
    )

    form.pack()

    fields = [
        "Evidence ID",
        "Username",
        "Action",
        "Location",
        "Notes"
    ]

    entries = {}

    for row, field in enumerate(fields):

        tk.Label(
            form,
            text=field + ":",
            font=("Arial", 10, "bold"),
            bg=NAVY,
            fg=WHITE
        ).grid(
            row=row,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        entry = tk.Entry(
            form,
            width=40,
            font=("Arial", 10)
        )

        if field == "Username":

            entry.insert(
                0,
                current_user.Username
            )

        entry.grid(
            row=row,
            column=1,
            padx=10,
            pady=8
        )

        entries[field] = entry

    def add_record():

        try:

            evidence_id = entries["Evidence ID"].get().strip()
            username = entries["Username"].get().strip()
            action = entries["Action"].get().strip()
            location = entries["Location"].get().strip()
            notes = entries["Notes"].get().strip()

            if not evidence_id or not action:

                messagebox.showwarning(
                    "Missing Information",
                    "Evidence ID and Action are required."
                )

                return

            current_time = datetime.now()

            record = (
                f"Date/Time: {current_time}\n"
                f"Evidence ID: {evidence_id}\n"
                f"User: {username}\n"
                f"Action: {action}\n"
                f"Location: {location}\n"
                f"Notes: {notes}\n"
                f"{'-' * 60}\n"
            )

            with open(
                custody.CUSTODY_FILE,
                "a",
                encoding="utf-8"
            ) as file:

                file.write(record)

            audit.create_audit_log(
                current_user.Username,
                "Added Chain of Custody Record",
                evidence_id
            )

            messagebox.showinfo(
                "Success",
                "Chain of Custody Record Added! ✅"
            )

            window.destroy()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    tk.Button(
        window,
        text="ADD CUSTODY RECORD",
        command=add_record,
        width=22,
        font=("Arial", 10, "bold"),
        bg=GREEN,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack(pady=20)

    def view_records():

        if not os.path.exists(
            custody.CUSTODY_FILE
        ):

            show_text_window(
                "Chain of Custody",
                "No custody records found."
            )

            return

        with open(
            custody.CUSTODY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            records = file.read()

        show_text_window(
            "Chain of Custody Records",
            records
        )

    tk.Button(
        window,
        text="VIEW CUSTODY RECORDS",
        command=view_records,
        width=22,
        font=("Arial", 10, "bold"),
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)


# =========================================================
# AUDIT LOGS
# =========================================================

def audit_gui():

    if not allowed("view_audit_logs"):
        return

    if not os.path.exists(
        audit.LOG_FILE
    ):

        show_text_window(
            "Audit Logs",
            "No audit logs found."
        )

        return

    try:

        with open(
            audit.LOG_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            logs = file.read()

        if not logs.strip():

            logs = "Audit log is empty."

        show_text_window(
            "Audit Logs",
            logs
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =========================================================
# GENERATE REPORT
# =========================================================

def generate_report_gui():

    if not allowed("generate_reports"):
        return

    try:

        reports.generate_report()

        audit.create_audit_log(
            current_user.Username,
            "Generated Evidence Report"
        )

        messagebox.showinfo(
            "Report",
            "Evidence report generated successfully! ✅"
        )

    except Exception as error:

        messagebox.showerror(
            "Report Error",
            str(error)
        )


# =========================================================
# VIEW REPORTS
# =========================================================

def view_reports_gui():

    if not allowed("generate_reports"):
        return

    try:

        if not os.path.exists(
            reports.REPORT_FOLDER
        ):

            show_text_window(
                "Reports",
                "Reports folder does not exist."
            )

            return

        files = [
            f
            for f in os.listdir(
                reports.REPORT_FOLDER
            )
            if f.endswith(".txt")
        ]

        if not files:

            show_text_window(
                "Reports",
                "No reports found."
            )

            return

        output = "\n".join(
            f"{i}. {file}"
            for i, file in enumerate(
                files,
                start=1
            )
        )

        show_text_window(
            "Available Reports",
            output,
            width=60,
            height=15
        )

        audit.create_audit_log(
            current_user.Username,
            "Viewed Reports"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =========================================================
# CREATE BACKUP
# =========================================================

def create_backup_gui():

    if not allowed("create_backup"):
        return

    try:

        backup_path = backup.create_backup()

        if backup_path:

            audit.create_audit_log(
                current_user.Username,
                "Created System Backup"
            )

            messagebox.showinfo(
                "Backup Successful",
                "Backup created successfully! 💾\n\n"
                f"Location:\n{backup_path}"
            )

    except Exception as error:

        messagebox.showerror(
            "Backup Error",
            str(error)
        )


# =========================================================
# VIEW BACKUPS
# =========================================================

def view_backups_gui():

    if not allowed("view_backups"):
        return

    try:

        if not os.path.exists(
            backup.BACKUP_FOLDER
        ):

            show_text_window(
                "Backups",
                "No backup folder found."
            )

            return

        folders = []

        for item in os.listdir(
            backup.BACKUP_FOLDER
        ):

            path = os.path.join(
                backup.BACKUP_FOLDER,
                item
            )

            if os.path.isdir(path):

                folders.append(item)

        if not folders:

            show_text_window(
                "Backups",
                "No backups found."
            )

            return

        output = "\n".join(
            f"{i}. {folder}"
            for i, folder in enumerate(
                folders,
                start=1
            )
        )

        show_text_window(
            "Available Backups",
            output,
            width=60,
            height=15
        )

        audit.create_audit_log(
            current_user.Username,
            "Viewed Backups"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =========================================================
# MY PERMISSIONS
# =========================================================

def permissions_gui():

    if current_user is None:
        return

    permissions = auth.ROLE_PERMISSIONS.get(
        current_user.Role,
        []
    )

    permission_text = "\n".join(
        f"✓ {permission}"
        for permission in permissions
    )

    messagebox.showinfo(
        "My Permissions",
        f"Username: {current_user.Username}\n"
        f"Role: {current_user.Role}\n\n"
        f"Allowed Actions:\n\n"
        f"{permission_text}"
    )


# =========================================================
# LOGOUT
# =========================================================

def logout_user():

    global current_user

    if current_user:

        audit.create_audit_log(
            current_user.Username,
            "User Logged Out"
        )

    current_user = None

    show_login()


# =========================================================
# LOGIN SCREEN
# =========================================================

def show_login():

    clear_window()

    create_header(
        "DIGITAL EVIDENCE MANAGEMENT SYSTEM",
        "Secure Digital Evidence & Forensic Management"
    )

    login_frame = tk.Frame(
        root,
        bg=NAVY
    )

    login_frame.pack(
        pady=25
    )

    tk.Label(
        login_frame,
        text="Username",
        font=("Arial", 12, "bold"),
        bg=NAVY,
        fg=WHITE
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=12
    )

    global username_entry
    global password_entry

    username_entry = tk.Entry(
        login_frame,
        width=30,
        font=("Arial", 12)
    )

    username_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=12
    )

    tk.Label(
        login_frame,
        text="Password",
        font=("Arial", 12, "bold"),
        bg=NAVY,
        fg=WHITE
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=12
    )

    password_entry = tk.Entry(
        login_frame,
        width=30,
        show="*",
        font=("Arial", 12)
    )

    password_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=12
    )

    login_button = tk.Button(
        root,
        text="LOGIN",
        command=login,
        width=22,
        height=2,
        font=("Arial", 12, "bold"),
        bg=BLUE,
        fg=WHITE,
        activebackground="#174A8A",
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2"
    )

    login_button.pack(
        pady=20
    )

    tk.Label(
        root,
        text=(
            "Digital Forensics • Evidence Integrity • "
            "Chain of Custody"
        ),
        font=("Arial", 9),
        bg=NAVY,
        fg=LIGHT_BLUE
    ).pack(
        side="bottom",
        pady=20
    )

    username_entry.focus()


# =========================================================
# WINDOW CLOSE
# =========================================================

def close_application():

    try:

        if current_user:

            audit.create_audit_log(
                current_user.Username,
                "System Closed"
            )

    except Exception:
        pass

    try:
        auth.connection.close()
    except Exception:
        pass

    try:
        evidence.connection.close()
    except Exception:
        pass

    try:
        reports.connection.close()
    except Exception:
        pass

    root.destroy()


# =========================================================
# START APPLICATION
# =========================================================

root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)

show_login()

root.mainloop()