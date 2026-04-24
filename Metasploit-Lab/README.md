# Windows Post-Exploitation & Meterpreter Lab

## 📌 Project Overview
This lab demonstrates a complete cyber-attack lifecycle on a Windows environment.

---

## 🚀 Step-by-Step Execution

### 1. Payload Generation & Delivery Setup
![Step 1](screenshot/01-payload-gen-and-server.jpg)
> Generated a malicious `zoom.exe` and started a Python HTTP server.

---

### 2. File Delivery to Target
![Step 2](screenshot/02-target-download-success.jpg)
> The payload was successfully delivered to the target's machine.

---

### 3. Establishing the Initial Shell
![Step 3](screenshot/03-handler-initial-shell.jpg)
> Caught the incoming reverse connection using Metasploit.

---

### 4. Upgrading to Meterpreter
![Step 4](screenshot/04-shell-to-meterpreter-upgrade.jpg)
> Upgraded the basic shell to a full Meterpreter session.

---

### 5. Post-Exploitation: Visual Evidence
![Step 5](screenshot/05-post-exploitation-evidence.jpg)
> Demonstrated control by taking a screenshot and a webcam snapshot.

---

## 🛡️ Mitigation & Defense
* Keep Real-time protection enabled.
* Avoid executing files from unknown sources.
