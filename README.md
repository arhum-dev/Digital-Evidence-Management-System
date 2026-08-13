# Digital Evidence Management System (DEMS)

A Python-based Digital Evidence Management System designed to securely manage digital evidence while maintaining evidence integrity, controlled access, auditability, and chain of custody.

## 📌 Project Overview

Digital evidence such as CCTV videos, images, documents, audio files, and other digital records must be protected from unauthorized access and tampering.

The Digital Evidence Management System provides a centralized system for managing digital evidence and maintaining a record of important evidence-related activities.

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

| Module | Description |
|---|---|
| `main.py` | Main application entry point |
| `gui.py` | Graphical user interface |
| `auth.py` | Authentication and user roles |
| `database.py` | Database connectivity and operations |
| `evidence.py` | Evidence management |
| `security.py` | Hashing, encryption and security functions |
| `custody.py` | Chain of custody management |
| `audit.py` | Audit activity logging |
| `reports.py` | Report generation |
| `backup.py` | Evidence/database backup |

## 🔄 System Workflow

```text
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