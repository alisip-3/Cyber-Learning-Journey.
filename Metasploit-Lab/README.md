# Windows Post-Exploitation & Meterpreter Lab

## 📌 Project Overview
This lab demonstrates a complete cyber-attack lifecycle on a Windows environment, from payload generation to full system compromise and post-exploitation monitoring.

---

## 🚀 Step-by-Step Execution

### 1. Payload Generation & Delivery Setup
![Step 1](screenshot/01-payload-gen-and-server.png)
> **Technical Detail:** Generated a malicious `zoom.exe` using `msfvenom` and launched a Python-based HTTP server to deliver the payload.

---

### 2. File Delivery to Target
![Step 2](screenshot/02-target-download-success.png)
> **Delivery:** The file was successfully downloaded by the target machine, as shown in the local directory.

---

### 3. Establishing the Initial Shell
![Step 3](screenshot/03-handler-initial-shell.png)
> **Execution:** Caught the incoming reverse connection using Metasploit's `multi/handler`. Initial access confirmed via `whoami`.

---

### 4. Upgrading to Meterpreter
![Step 4](screenshot/04-shell-to-meterpreter-upgrade.png)
> **Privilege Escalation:** Successfully upgraded the basic command shell to a Meterpreter session for advanced control.

---

### 5. Post-Exploitation: Visual Evidence
![Step 5](screenshot/05-post-exploitation-evidence.png)
> **Control:** Demonstrated the ability to exfiltrate data, take screenshots, and capture webcam images from the compromised host.

---

## 🛡️ Mitigation & Defense
* **Endpoint Protection:** Always keep Real-time protection and Antivirus signatures updated.
* **Network Hygiene:** Avoid downloading or executing untrusted files within a local network.
* **Least Privilege:** Run daily tasks using a standard user account rather than an administrator.
