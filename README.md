***PYTHON SCRIPTS***
                                                    
Author: Crashwire 

**Python-Scripts** is a collection of Python programs designed for Red Team and Pentesting use-cases. Each script is tailored for specific offensive security needs, from crafting reverse shells to data exfiltration and vulnerability mapping. Whether you're a pentester looking to automate tasks or a red teamer needing specialized tools, this repo has something for you!

---

## ⚙️ Current Scripts

1. **`Reverse_snake.py`** 🐍  
   A simple reverse shell that connects back to a remote server, giving you access to a target machine's command line.

2. **`DNS_mole.py`** 🕳️  
   A post-exploitation tool leveraging DNS tunneling to stealthily exfiltrate data out of a compromised network without raising alarms.

3. **`Metamap.py`** 🌐  
   Combines the output of Nmap scans with Metasploit module searches, automatically matching discovered vulnerabilities to available exploits. 

---

## 🚀 Getting Started

Clone the repo and run any script using Python 3:

```bash
git clone https://github.com/yourusername/Python-Scripts.git
cd Python-Scripts
python3 Reverse_snake.py
