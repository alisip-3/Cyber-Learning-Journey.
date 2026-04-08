# 🦈 Network Traffic Analysis: Wireshark Credentials Capture

## 🎯 Project Objective
The goal of this lab is to demonstrate the critical security risks associated with unencrypted protocols (HTTP). By intercepting network traffic, I illustrate how sensitive information like login credentials can be exposed to attackers.

## 📂 Methodology
* **Environment:** Kali Linux (Attacker) capturing traffic from a vulnerable web application.
* **Tool:** Wireshark (Packet Sniffer).
* **Technique:** Filtering for HTTP POST requests and analyzing HTML Form URL Encoded data.

---

## 🔍 Investigation: Packet Analysis
In this scenario, I captured a login attempt on a test environment.

**Key Findings:**
* **Protocol:** HTTP (Non-secure).
* **Data Exposure:** As shown in the capture, the **Username** (`alisi_pa`) and **Password** (`123456`) are transmitted in **Cleartext**.
* **Session Risk:** In addition to credentials, a **User Token** was also intercepted, which could be used for Session Hijacking.

![Wireshark Capture](./VirtualBox_Kali_wireshark_http.jpg)

---

## 💡 Professional Insights
* **Risk Assessment:** This lab proves that without **TLS/SSL (HTTPS)**, data is vulnerable to Man-in-the-Middle (MITM) attacks.
* **Mitigation:** Organizations must enforce HTTPS and use secure flags for cookies and tokens to prevent unauthorized interception.
* **Technical Proficiency:** Demonstrated ability to use Wireshark filters and reconstruct session data from raw packets.

---
*Part of my Cyber Security Professional Portfolio.*
