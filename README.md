This is an ambitious and highly rewarding path. As of **January 2026**, the industry has shifted significantly toward "Infrastructure as Code," and Cisco has updated its blueprints (CCNA 200-301 v1.1+) to lean more heavily into automation.

Below is your comprehensive 2026 master plan, combining classical networking with modern DevOps.

---

## Stage 1: The Foundation (Networking + Python)

**Goal:** Master the "How" of networking and the "How" of scripting simultaneously.

### The Gold Standard Courses (2026)

| Subject | Course Name | Primary Instructor/Platform | Why it's the Gold Standard |
| --- | --- | --- | --- |
| **Networking** | **CCNA 200-301 Gold Bootcamp** | Neil Anderson (Flackbox/Udemy) | Updated for 2026 v1.1 topics; best mix of theory and practical labs. |
| **Networking** | **Free CCNA 200-301 Course** | Jeremy’s IT Lab (YouTube) | The best free resource with high-quality Anki flashcards and Packet Tracer labs. |
| **Python** | **Python for Network Engineers** | Kirk Byers (https://www.google.com/search?q=PythonForNetworkEngineers.com) | The industry benchmark for applying Python specifically to Netmiko, NAPALM, and Nornir. |
| **Python** | **Python Network Programming for Experts** | David Bombal (Udemy/YouTube) | Excellent for practical "build-a-script" learners. |

### The Simultaneous Study Strategy

Don't alternate days; alternate **modes of thinking**.

* **Mornings (90 min): CCNA Theory.** Focus on routing, switching, and IP services.
* **Evenings (60 min): Python Practice.** Focus on syntax and basic automation (Netmiko).
* **Weekends:** Integration. Use a Python script to automate a lab you built in CCNA.

---

## Stage 1a: Git Control (The DevOps Engine)

**Goal:** Learn how to version-control your scripts and collaborate.

### The Gold Standard Course (2026)

* **Primary Pick:** **"Introduction to Git and GitHub" (Google on Coursera).** * This is part of the Google IT Automation Professional Certificate. It covers exactly what a NetDevOps engineer needs: branching, merging, and remote repositories, without getting lost in software developer-only complexities.
* **Alternative:** **"Version Control with Git" (Atlassian on Coursera).**
* Since Atlassian owns Bitbucket, they provide a very enterprise-centric view of Git.



> **Key Focus for 2026:** Master the "Git Flow" (main, dev, and feature branches). In 2026, network outages are often caused by bad script versions; knowing how to `git revert` is a survival skill.

---

## Stage 2: CCNP Automation (Enterprise & Data Center)

**Goal:** Professional-level automation across diverse environments.

### 2.1 Enterprise Automation (ENAUTO 300-435)

This focuses on **Cisco Catalyst Center (DNA Center)**, **SD-WAN**, and **Meraki APIs**.

* **Gold Standard:** **PyNet Labs - CCNP ENAUTO.** * They provide access to real sandboxes for SD-WAN and DNA Center, which are nearly impossible to lab at home.
* **Self-Paced:** **Nick Russo’s "ENAUTO Study Track" (Pluralsight).**
* Nick is famous for "minimalist" teaching—getting you the info you need for the exam and the job without the fluff.



### 2.2 Data Center Automation (DCAUTO 300-635)

This focuses on **Cisco ACI**, **NX-OS**, and **Intersight**.

* **Gold Standard:** **Cisco Digital Learning (Official).**
* Cisco’s own "DCAUI" course is expensive but is the only one that reliably grants access to the ACI and Nexus Dashboards.


* **Alternative:** **Orhan Ergun’s DCAUTO Training.**
* Excellent for deep-dive architectural understanding of how automation fits into a spine-leaf Data Center fabric.



---

### Implementation Timeline

| Month | Phase | Focus |
| --- | --- | --- |
| **1-3** | **Stage 1** | CCNA (Fundamentals) + Python (Basic Syntax). Use Jeremy’s Anki cards daily. |
| **4** | **Stage 1a** | Git. Move all your Python scripts into a private GitHub repository. |
| **5-7** | **Stage 2 (Enterprise)** | ENAUTO. Focus on Catalyst Center APIs and Ansible playbooks for IOS-XE. |
| **8-10** | **Stage 2 (Data Center)** | DCAUTO. Focus on ACI (Cobra SDK) and Nexus Dashboard automation. |

---

### Next Step: Hardware & Tools

To start Stage 1 today, you need your environment ready.

**Would you like me to provide a list of the specific Python libraries you should prioritize learning for Stage 1?**