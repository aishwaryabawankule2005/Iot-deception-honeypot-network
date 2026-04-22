# 🟢 Week 1 — Environment Setup & Device Simulation

##  Objective

To establish a secure and isolated lab environment and deploy a honeypot that simulates a real-world healthcare IoT device for capturing attacker interactions.

---

##  Implementation Details

### 1. Virtual Machine Setup

* Created two virtual machines using VirtualBox:

  * **Kali Linux** — used as the attacker machine for penetration testing
  * **Ubuntu Server** — configured as the target system hosting the honeypot

---

### 2. Network Configuration

* Configured a **Host-Only Network** to ensure an isolated and controlled environment
* Assigned static IP addresses:

  * Ubuntu Server: `192.168.56.102`
  * Kali Linux: `192.168.56.101`
* Enabled communication between attacker and target systems without exposing the lab to external networks

---

### 3. Honeypot Deployment (Cowrie)

* Installed and configured **Cowrie SSH Honeypot** on the Ubuntu Server
* Cowrie simulates a vulnerable SSH service:

  * Accepts login attempts (including brute-force attacks)
  * Logs all attacker activities such as commands, credentials, and sessions
* Configured to run on **port 2222**

---

### 4. IoT Device Simulation

* Modified system identity to mimic a real healthcare device
* Set hostname to: `vitals-monitor-04`
* Created a realistic environment to deceive attackers into believing it is a legitimate medical device

---

##  Result

* Successfully deployed a fully functional honeypot environment
* The system is actively listening on port **2222**
* The simulated healthcare IoT device is ready to capture and log attacker behavior in a controlled lab setup

---

##  Tools & Technologies Used

* VirtualBox (Virtualization)
* Ubuntu Server (Honeypot Host)
* Kali Linux (Attack Simulation)
* Cowrie SSH Honeypot
* Python 3
