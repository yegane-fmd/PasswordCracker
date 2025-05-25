# 🔐 Password Cracker by SHA256

A simple Python project that attempts to brute-force 4-digit numeric passwords from SHA256 hashes.

## 📁 Files
- `cracker.py` – Main script
- `hashes_only.csv` – Sample CSV file (Name, Hash)

## ▶️ How to Run
```bash
python cracker.py

Make sure you have Python 3 installed.

📌 How it Works
	1.	Reads a CSV file with names and SHA256 hashes.
	2.	Tries all 4-digit numbers (0000 to 9999).
	3.	Compares hashes and finds matching passwords.

⚠️ Note

This is an educational project. Do not use for malicious purposes.