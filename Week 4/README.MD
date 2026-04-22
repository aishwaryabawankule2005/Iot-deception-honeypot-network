# 🔴 Week 4 — Dashboarding and Geolocation Analysis 

##  Objective

To transform raw honeypot log data into meaningful visual insights using charts and an interactive geographic map, enabling clear interpretation of attacker behavior and threat intelligence.

---

##  Implementation Details

### 1. Environment Setup & Dependencies

* Activated the Cowrie virtual environment (`cowrie-env`)
* Installed required Python libraries:

  * `matplotlib` — for chart generation
  * `numpy` — for data handling
  * `requests` — for API calls
  * `folium` — for interactive maps
* Ensured all dependencies were isolated within the virtual environment

---

### 2. Attack Dashboard Development

* Developed `dashboard.py` to process analyzed data from `cowrie.json`
* Generated visual representations:

  * **Bar Chart** — displaying total connections, login attempts, and commands executed
  * **Pie Chart** — illustrating the ratio of successful vs failed login attempts
* Exported visual outputs:

  * `dashboard.png`
  * `pie_chart.png`

---

### 3. Geographic Attack Mapping

* Created `geo_map.py` to visualize attacker locations on a global map
* Implemented:

  * IP-based geolocation using external API (`requests`)
  * Interactive mapping using `folium`
* Due to private lab IPs (192.168.x.x), used a public IP (`8.8.8.8`) for demonstration
* Generated output:

  * `attack_map.html`

---

### 4. Output Verification

* Verified all generated outputs:

  * Charts (`dashboard.png`, `pie_chart.png`) rendered correctly
  * Interactive map (`attack_map.html`) loaded successfully in browser
* Confirmed consistency between visualization outputs and Week 3 analysis results

---

##  Result

* Successfully converted raw attack logs into clear visual insights
* Built an interactive dashboard for analyzing attacker behavior
* Enabled geographic visualization of attack origins
* Improved understanding and presentation of threat intelligence data

---

##  Evidence

* `screenshots/dashboard.png` — Bar chart of attack statistics
* `screenshots/pie_chart.png` — Login success vs failure ratio
* `attack_map.html` — Interactive geographic attack map

---

##  Scripts

* `scripts/dashboard.py` — Generates charts and dashboard visuals
* `scripts/geo_map.py` — Creates interactive geographic attack map

---

## Tools & Technologies Used

* Python 3
* Matplotlib (Data Visualization)
* Folium (Interactive Mapping)
* Requests (Geolocation API Integration)
