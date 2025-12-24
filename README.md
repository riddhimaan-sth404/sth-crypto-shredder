<h1 align='center'>Cryto Shredder - sth.exe</h1>

## Overview
This tool, when executed as `sth.exe`, is designed for educational, research, and authorized security testing purposes. It demonstrates how encryption can be applied to files across a Windows system by recursively scanning the C:\ drive, encrypting files using the Fernet symmetric encryption, and targeting specific system directories such as the Windows Boot and Recovery folders. It also provides real-time status updates via a console window and attempts to reboot the system after the process completes.

**Important:** This tool is intended solely for lawful and authorized use. It is **not** intended for malicious activities or unauthorized access. Always ensure you have explicit permission before running this tool on any system. Misuse of this software for harmful purposes is illegal and unethical.

---

## Features
- **Systematic scanning:** Recursively searches the C:\ drive for files, excluding critical system directories such as `Windows` and `System Volume Information` to demonstrate the scope of file encryption.
- **Encryption process:** Encrypts all identified files with a generated Fernet key, illustrating the principles of data security and encryption.
- **Targeted system directories:** Encrypts files within the Windows Boot and Recovery directories to demonstrate their importance in system recovery and security.
- **Progress monitoring:** Opens a console window that displays real-time status messages, aiding understanding of the process flow.
- **Error handling:** Logs exceptions encountered during file operations into `C:/log.enclog` for analysis and transparency.
- **Post-operation actions:** Displays a summary message with the total number of encrypted files and initiates a system reboot—highlighting the impact of encryption.

**Note:** Use this tool responsibly and only within environments where you have explicit authorization.

---

## Usage Instructions
1. Obtain or compile the executable as `sth.exe`.
2. Run `sth.exe` with administrator privileges to access protected system files—only on systems you own or have explicit permission to test.
3. The tool will:
   - Generate a cryptographic key.
   - Encrypt files across the drive.
   - Encrypt specific system directories.
   - Provide live progress updates.
   - Reboot the system upon completion.

**Legal Reminder:** Always ensure you have written authorization before performing any security testing or data encryption demonstrations on computer systems.

---

## Ethical and Legal Notice
This software is intended solely for lawful purposes such as security research, educational demonstrations, and authorized testing. Unauthorized use of this tool to access, modify, or damage systems without permission is illegal and subject to prosecution.

Use this tool responsibly to understand encryption's power and limitations. It is your responsibility to ensure compliance with all applicable laws and regulations.

---

## Disclaimer
The author disclaims any liability for misuse, unauthorized use, or damages resulting from the operation of this software. Use it only in environments where you have explicit permission and for lawful purposes.

**Use responsibly and ethically to promote cybersecurity awareness and education.**

---
