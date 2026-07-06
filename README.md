# Conduct-a-Phishing-Simulation🛡️ Cyber Incident Response Plan — Internee.pk
> \\\*\\\*Version 1.0 | June 2025 | Confidential\\\*\\\*
---
📌 Objective
Develop a structured response plan for handling cybersecurity incidents effectively at Internee.pk, covering:
✅ Define procedures for threat detection, mitigation, and recovery
✅ Simulate a ransomware attack and document incident handling steps
✅ Train Internee.pk staff on emergency response protocols
---
📂 Project Structure
```
IRP\\\_Internee/
├── README.md                  # Project overview (this file)
├── IRP\\\_Internee.md            # Full Incident Response Plan (source)
├── IRP\\\_Internee.pdf           # Formatted PDF version of the IRP
└── simulation/
    └── ransomware\\\_sim.md      # Ransomware simulation report
```
---
🔍 Where to Get Data
📖 MITRE ATT&CK Framework — case studies for real-world attack scenarios → attack.mitre.org
📊 Cybersecurity Breach Reports — reference material from Cybersecurity Breaches
---
🚨 Incident Severity Levels
Level	Description	Response Time
🔴 P1 CRITICAL	Ransomware, Data Breach	Immediate (< 1 hour)
🟠 P2 HIGH	Unauthorized Access	4 hours
🔵 P3 MEDIUM	Malware Detection	24 hours
🟢 P4 LOW	Policy Violation	72 hours
---
🔄 Response Phases
Phase	Name	Key Actions
1	Preparation	Asset inventory, EDR deployment, staff training
2	Identification	SIEM alerts, IOC detection
3	Containment	Isolate systems, disable accounts
4	Eradication	Remove malware, patch, reset credentials
5	Recovery	Restore backups, verify integrity
6	Lessons Learned	Document, update controls, retrain staff
---
🦠 Ransomware Simulation Results (June 2025)
Metric	Result
Attack Vector	Phishing email (T1566)
Files Affected	4 test files
Detection Time	Immediate (Wazuh alert)
Containment Time	< 5 minutes
Recovery Time	< 10 minutes
Outcome	✅ All files successfully recovered
---
🛠️ Tools & Technologies
Wazuh — SIEM & EDR for detection and file integrity monitoring
MITRE ATT&CK — Threat mapping framework
Offline Backups — Primary recovery mechanism
---
⏱️ Recovery Time Objectives
System	RTO	RPO
Core Website	4 hours	24 hours
User Database	2 hours	1 hour
Email Systems	8 hours	24 hours
File Servers	6 hours	4 hours
---
👥 Incident Response Team
Role	Responsibility
IR Lead	Overall coordination
Security Analyst	Detection & Analysis
System Admin	Containment & Recovery
Management	Communication & Decisions
Legal / HR	Compliance & Reporting
---
📋 MITRE ATT&CK Mapping
Technique	Description
T1566	Phishing (Initial Access)
T1059	Scripting (Execution)
T1486	Data Encrypted for Impact
T1490	Inhibit System Recovery
T1489	Service Stop
---
> ⚠️ \\\*\\\*CONFIDENTIAL\\\*\\\* — For internal use only. Do not distribute without authorization.
