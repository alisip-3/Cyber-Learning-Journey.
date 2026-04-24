# 🦈 Network Traffic Analysis: Credentials Capture

**Objective:** Demonstrating security risks in unencrypted communication (HTTP).

### 🔍 Analysis Findings:
Intercepted raw packets and reconstructed a login session to expose plain text credentials:
* **Username:** `alisi_pa`
* **Password:** `123456`

This confirms the critical importance of enforcing HTTPS to prevent **Man-in-the-Middle (MITM)** attacks.

![Wireshark Credentials Capture](https://github.com/alisip-3/Cyber-Learning-Journey./blob/main/Network-Analysis-Wireshark/VirtualBox_Kali_wireshark_http.png)

> **Key Skills:** Packet Sniffing, Protocol Analysis, Cleartext Detection.
