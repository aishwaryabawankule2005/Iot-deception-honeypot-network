
# 🔵 Week 3 — Log Parsing & Threat Intelligence Extraction

##  Objective

To develop Python-based log analysis scripts that parse raw honeypot logs and extract meaningful **Indicators of Compromise (IoCs)** for understanding attacker behavior.

---

##  Implementation Details

### 1. Analysis of Raw Logs

* Examined log files generated during Week 2:

  * `cowrie.log` (text-based logs)
  * `cowrie.json` (structured JSON logs)
* Identified multiple event types within the logs
* Key events observed include:

  * `cowrie.login.success`
  * `cowrie.login.failed`
  * `cowrie.command.input`
  * `cowrie.session.connect`
* Understood the structure and flow of attacker interactions within the honeypot

---

### 2. Development of Python Log Parser

* Created a custom Python script to process JSON log data
* Implemented:

  * `json.loads()` to parse each log entry
  * `entry.get()` for safe data extraction
  * Conditional logic (`if/elif`) to classify event types
* Designed the parser to efficiently handle large volumes of log data

---

### 3. Extraction of Indicators of Compromise (IoCs)

Extracted key security indicators from the logs:

* Attacker IP addresses
* Timestamps of activity
* Username and password attempts
* Commands executed by the attacker

These IoCs provide critical insights into attack patterns and behavior.

---

### 4. Summary Statistics

Generated structured summary of attack activity:

* Total Connections: **7**
* Failed Login Attempts: **3**
* Successful Logins: **5**
* Commands Executed: **9**

---

##  Result

* Successfully transformed unstructured log data into meaningful security insights
* Generated a clear timeline of attacker actions
* Enabled easier interpretation of attack behavior and patterns

---

##  Scripts

* `scripts/analyzer.py` — Main log parsing and analysis script

---

##  Tools & Technologies Used

* Python 3
* JSON Library
