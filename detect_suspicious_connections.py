#!/usr/bin/env python3

import psutil
import socket
import logging
from datetime import datetime

# Configuration
LOG_FILE = "/var/log/suspicious_connections.log"

# Allowed IPs (e.g. Internal IP, DNS, proxy, ...)
WHITELIST = [
    "127.0.0.1",
    "8.8.8.8",
    "1.1.1.1",
    "::1"
]

# Logging Setup
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Outgoing connections
def get_suspicious_connexions():
    suspicious = []
    for conn in psutil.net_connections(kind="inet"):
        if conn.status != psutil.CONN_ESTABLISHED:
            continue
        if not conn.raddr: #No remote address
            continue

        ip, port = conn.raddr
        if ip not in WHITELIST:
            suspicious.append({
                "pid": conn.pid,
                "remote_ip": ip,
                "remote_port": port,
                "local_port": conn.laddr.port
            })
    return suspicious

# Process Info
def get_process_name(pid):
    try:
        return psutil.Process(pid).name()
    except Exception:
        return "Unknown"

# Main
def main():
    suspicious_conns = get_suspicious_connexions()

    if suspicious_conns:
        logging.info("=== Suspicious,outgoing connections detected ===")
        for conn in suspicious_conns:
            proc_name = get_process_name(conn["pid"])
            message = (f"Process: {proc_name} (PID: {conn['pid']})"
                       f"=> {conn['remote_ip']}:{conn['remote_port']}"
                       f"(local port {conn['local_port']})")
            print(message)
            logging.warning(message)
    else:
        logging.info("No suspicious outgoing connections detected.")

if __name__ == "__main__":
    main()