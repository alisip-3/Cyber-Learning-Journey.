# 🛡️ Windows Post-Exploitation & Meterpreter Lab

## 📌 Project Overview
This laboratory exercise demonstrates a successful penetration testing lifecycle on a Windows environment. The goal was to generate a custom payload, deliver it to a target system, and establish a high-level Meterpreter session to demonstrate post-exploitation capabilities.

---

## 🚀 Step-by-Step Execution

### 1. Payload Generation & Server Setup
The process began by generating a malicious executable (`zoom.exe`) using `msfvenom`. A Python HTTP server was hosted on the attacker's machine to facilitate the file delivery.

![Step 1](01-payload-gen-and-server.png)
> **Insight:** Monitoring the server logs allows the attacker to confirm exactly when the target accesses the file.

---

### 2. Successful Payload Delivery
The target machine successfully downloaded the file from the attacker's hosted server.

![Step 2](02-target-download-success.png)
> **Observation:** In a real-world scenario, this would represent the "Delivery" stage of the Cyber Kill Chain.

---

### 3. Establishing the Initial Shell
Using the `multi/handler` module in Metasploit, I captured the reverse connection. This provided an initial command-line shell on the target system.

![Step 3](03-handler-initial-shell.png)
> **Verification:** Running `whoami` confirms the current user context on the compromised machine.

---

### 4. Upgrading to Meterpreter Session
To gain advanced control (file system access, hardware control, etc.), I upgraded the standard shell to a Meterpreter session.

![Step 4](04-shell-to-meterpreter-upgrade.png)
> **Action:** Transitioning from Session 1 (Shell) to Session 2 (Meterpreter).

---

### 5. Post-Exploitation Evidence
With full Meterpreter access, I demonstrated control by exfiltrating visual evidence from the target, including system screenshots and webcam captures.

![Step 5](05-post-exploitation-evidence.png)
> **Impact:** This proves the ability to monitor the user and steal sensitive data in real-time.

---

## 🛡️ Defensive Mitigations
To prevent such attacks, the following security measures are recommended:
1. **EDR/Antivirus:** Ensure real-time protection is active to catch known malicious signatures (like msfvenom payloads).
2. **User Education:** Avoid downloading and running executable files from untrusted network sources.
3. **Application Whitelisting:** Use policies to ensure only authorized, signed applications can execute.
