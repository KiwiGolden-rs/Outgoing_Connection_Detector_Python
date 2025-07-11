# Outgoing_Connection_Detector_Python

This project provides a lightweight Python script that scans for suspicious outgoing network connections on a system. It was created as part of a personal learning journey focused on scripting for cybersecurity use cases.

---

## 🎯 Purpose

- Identify processes that establish outgoing connections to non-whitelisted IP addresses.
- Raise alerts for potential malware, data exfiltration, or unauthorized access.
- Learn Python scripting in a practical cybersecurity context.

---

## 📚 What I Learned

- How to inspect live network connections in Python using the `psutil` library.
- Associating network connections with process IDs (PIDs) and process names.
- Implementing a whitelist to reduce false positives.
- Building a script ready for scheduled execution (e.g., via cron or scheduled tasks).

---

## 🧩 Features

- ✅ Lists all **active outgoing TCP/UDP connections**
- ✅ Associates each connection with the **process name and PID**
- ✅ Filters connections using a **configurable whitelist**
- ✅ Logs suspicious activity in a log file
- ✅ Minimal, portable, and efficient — works cross-platform

---

## 🛠️ Requirements

- Python 3.6+
- [`psutil`](https://pypi.org/project/psutil/)

Install it via:

```bash
pip install psutil
```

---

## 📄 Usage

Run the script manually:

```bash
sudo python3 detect_suspicious_connections.py
```

By default, it logs results to:

`/var/log/suspicious_connections.log`

### 📁 Whitelist Configuration

You can customize the whitelist of known safe IP addresses inside the script:

```python
WHITELIST = [
    "127.0.0.1",
    "8.8.8.8",
    "1.1.1.1",
    "::1"
]
```

### 📂 Sample Log Output

```log
2025-07-10 19:42:01 - WARNING - Process: python3 (PID: 3241) => 185.129.61.45:443 (local port 38882)
2025-07-10 19:42:01 - WARNING - Process: powershell.exe (PID: 4012) => 45.88.33.5:80 (local port 51720)
```

---

## 🔐 Security Notes

  - Run as root/admin to access all process info.

  - Logs are stored in `/var/log` to prevent tampering (can be change for windows).

  - Avoid writing logs to user-writable directories.

---

📘 License
MIT License
