# Digital Evidence Management System (DEMS)

A Python-based Digital Evidence Management System designed to securely manage digital evidence while maintaining evidence integrity, controlled access, auditability, and chain of custody.

## 📌 Project Overview

Digital evidence such as CCTV videos, images, documents, audio files, and other digital records must be protected from unauthorized access and tampering.

The Digital Evidence Management System provides a centralized system for managing digital evidence and maintaining a record of important evidence-related activities — built with forensic and law-enforcement workflows in mind.

## 🔐 Key Security Features

- Secure user authentication
- Role-based access control
- SHA-256 evidence hashing
- Evidence integrity verification
- Evidence encryption and decryption
- Chain of custody tracking
- Audit logging
- Backup functionality
- Evidence reports
- Controlled permissions

## 🧩 Main Modules

| Module        | Description                                |
| ------------- | ------------------------------------------ |
| `main.py`     | Main application entry point               |
| `gui.py`      | Graphical user interface                   |
| `auth.py`     | Authentication and user roles              |
| `database.py` | Database connectivity and operations       |
| `evidence.py` | Evidence management                        |
| `security.py` | Hashing, encryption and security functions |
| `custody.py`  | Chain of custody management                |
| `audit.py`    | Audit activity logging                     |
| `reports.py`  | Report generation                          |
| `backup.py`   | Evidence/database backup                   |

## 🔄 System Workflow

```
User Login
    ↓
Role & Permission Verification
    ↓
Evidence Upload
    ↓
SHA-256 Hash Generation
    ↓
Evidence Encryption
    ↓
Secure Storage
    ↓
Database Record
    ↓
Evidence Search / Access
    ↓
Integrity Verification
    ↓
Chain of Custody & Audit Logging
    ↓
Reports / Backup
```

## 🛡️ SHA-256 Integrity Verification

When evidence is uploaded, the system generates a SHA-256 hash for the file.

The hash can later be recalculated and compared with the original stored hash.

```text
Original File
     ↓
SHA-256 Hash
     ↓
Stored Hash
     ↓
Later Verification
     ↓
Match       → Evidence Verified
No Match    → Possible Tampering
```

## ⚙️ Installation & Setup

**Requirements:** Python 3.9+ recommended.

1. **Clone the repository**
   ```bash
   git clone https://github.com/arhum-dev/Digital-Evidence-Management-System.git
   cd Digital-Evidence-Management-System
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   Update the connection settings in `database.py` with your database credentials before first run.

5. **Run the application**
   ```bash
   python main.py
   ```



## 🚧 Roadmap / Future Improvements

- Trusted timestamping for chain-of-custody entries
- Improved encryption key management
- Automated test suite

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙋 Author

Built by [Arhum](https://github.com/arhum-dev) — Cyber Security student at NUTECH.
