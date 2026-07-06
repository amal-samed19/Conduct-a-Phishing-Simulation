import datetime
import random

print("=" * 65)
print("   PHISHING SIMULATION REPORT — INTERNEE.PK")
print("   Security Awareness Training Campaign")
print("=" * 65)
print(f"   Campaign: Internee-Phishing-Awareness-2025")
print(f"   Date: {datetime.datetime.now().strftime('%B %d, %Y')}")
print(f"   Conducted by: Talha Imran")
print(f"   Tool: GoPhish v0.12.1")
print("=" * 65)

employees = [
    {"name": "Ahmed Khan",   "dept": "Development", "opened": True,  "clicked": True,  "submitted": True},
    {"name": "Sara Ali",     "dept": "Management",  "opened": True,  "clicked": True,  "submitted": False},
    {"name": "Usman Raza",   "dept": "Design",      "opened": True,  "clicked": False, "submitted": False},
    {"name": "Fatima Shah",  "dept": "HR",          "opened": False, "clicked": False, "submitted": False},
    {"name": "Bilal Ahmed",  "dept": "Intern",      "opened": True,  "clicked": True,  "submitted": False},
]

print("\n INDIVIDUAL RESULTS:")
print("-" * 65)
print(f"{'Name':<20} {'Dept':<15} {'Opened':<10} {'Clicked':<10} {'Submitted'}")
print("-" * 65)

sent = len(employees)
opened = clicked = submitted = 0

for emp in employees:
    if emp["opened"]:   opened += 1
    if emp["clicked"]:  clicked += 1
    if emp["submitted"]: submitted += 1

    o = "YES ⚠️" if emp["opened"] else "no"
    c = "YES ⚠️" if emp["clicked"] else "no"
    s = "YES 🚨" if emp["submitted"] else "no"

    print(f"{emp['name']:<20} {emp['dept']:<15} {o:<12} {c:<12} {s}")

print("\n CAMPAIGN STATISTICS:")
print("-" * 65)
print(f"  Total Emails Sent      : {sent}")
print(f"  Emails Opened          : {opened} ({opened/sent*100:.0f}%)")
print(f"  Links Clicked          : {clicked} ({clicked/sent*100:.0f}%)")
print(f"  Credentials Submitted  : {submitted} ({submitted/sent*100:.0f}%)")
print(f"  Phishing Success Rate  : {clicked/sent*100:.0f}%")

print("\n RISK ASSESSMENT:")
print("-" * 65)

risk = clicked/sent*100
if risk >= 50:
    level = "CRITICAL — Immediate training required"
elif risk >= 30:
    level = "HIGH — Training strongly recommended"
elif risk >= 15:
    level = "MEDIUM — Awareness improvement needed"
else:
    level = "LOW — Good awareness level"

print(f"  Overall Risk Level: {level}")

print("\n PHISHING RED FLAGS IDENTIFIED:")
print("-" * 65)
flags = [
    "Urgent language — 'Immediate Action Required'",
    "Sender domain mismatch — not official internee.pk",
    "Generic greeting with urgency tactics",
    "Suspicious login page URL",
    "Request for credentials via email link",
    "Threatening consequences for non-action"
]
for i, flag in enumerate(flags, 1):
    print(f"  {i}. {flag}")

print("\n RECOMMENDATIONS:")
print("-" * 65)
recs = [
    "Conduct monthly phishing awareness training",
    "Implement email authentication (SPF, DKIM, DMARC)",
    "Enable MFA on all employee accounts",
    "Deploy email filtering solutions",
    "Create clear incident reporting procedures",
    "Reward employees who report phishing attempts"
]
for i, rec in enumerate(recs, 1):
    print(f"  {i}. {rec}")

print("\n" + "=" * 65)
print(f"  Report generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 65)
