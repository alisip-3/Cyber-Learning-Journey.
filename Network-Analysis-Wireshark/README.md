# 🔍 Wireshark Lab: Analyzing Unencrypted Traffic (HTTP)

## 📌 Project Goal
I wanted to see for myself why HTTPS is so important. In this lab, I captured network traffic to see how easy it is to intercept sensitive information like usernames and passwords when a website uses unencrypted HTTP.

---

## 🛠️ Step-by-Step Analysis

### 1. Capturing the Traffic
I started Wireshark on my interface and filtered for `http` traffic. I then simulated a login on a test website. 

### 2. Finding the Payload
Among all the packets, I looked for the **POST** request, which is usually where login data is sent.

### 3. Reconstructing the Session
The coolest part was using the **"Follow TCP Stream"** feature. It allowed me to see the entire conversation in plain text, just like a chat log.

---

## 📊 What I Found (The Leak)
By analyzing the reconstructed stream, I was able to find the exact login credentials sent by the user:

* **Intercepted Username:** `alisi_pa`
* **Intercepted Password:** `123456`


![Wireshark Credentials Capture](https://github.com/alisip-3/Cyber-Learning-Journey./blob/main/Network-Analysis-Wireshark/VirtualBox_Kali_wireshark_http.png)
---

## 💡 Key Takeaways
* **Packet Inspection:** I practiced how to use Wireshark filters to cut through the noise and find specific data.
* **MITM Risk:** This lab is a perfect example of how a Man-in-the-Middle (MITM) attack works. Anyone on the same network could have seen this.
* **HTTP vs HTTPS:** It’s one thing to hear that HTTP is "insecure," but seeing my own password in a packet capture made it very real.

## 🛡️ How to Stay Safe
1.  **Enforce HTTPS:** Always use SSL/TLS certificates (HTTPS) so that even if packets are intercepted, they are unreadable.
2.  **HSTS:** Websites should use HSTS (HTTP Strict Transport Security) to force browsers to always use secure connections..

> **Key Skills:** Packet Sniffing, Protocol Analysis, Cleartext Detection.
