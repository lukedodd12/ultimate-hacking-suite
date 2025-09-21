# Ultimate Hacking Suite

A neat, tidy all-in-one menu wrapper for 200+ pentesting/hacking tools, inspired by [HackingToolkit](https://github.com/CodingRanjith/hackingtoolkit). Organized into clean categories for beginners to pros. Launches tools via subprocess—assumes Kali Linux setup.

## Features
- **12 Main Categories**: Network Scanning, Exploitation, WiFi, Web Testing, etc.
- **200+ Tools**: Nmap, Metasploit, sqlmap, Hydra, Aircrack-ng, and more (see menu).
- **Tidy UI**: Nested menus, error handling, root check.
- **Educational Focus**: For labs like HackTheBox or authorized tests.

## Installation
1. Clone: `git clone https://github.com/YOURUSERNAME/ultimate-hacking-suite.git`
2. `cd ultimate-hacking-suite`
3. Install deps (if needed): `sudo apt update && sudo apt install nmap wireshark metasploit-framework john hydra aircrack-ng sqlmap setoolkit autopsy steghide tor proxychains crunch sherlock xsstrike hping3 ghidra volatility hashcat wget`
4. Run: `sudo python3 main.py`

## Usage
- Launch `main.py` as root.
- Navigate menus: Pick category > sub-tool > It runs (customize commands in code).
- Examples: Nmap scans localhost; sqlmap tests a URL (edit payloads).

## Categories & Tools
- **Network**: Nmap, Wireshark, Host
- **Vuln Scan**: OpenVAS
- **Exploitation**: Metasploit
- **WiFi**: Aircrack, Deauth, Jammer
- **Web**: sqlmap, XSSStrike, wget (crawl)
- **Passwords**: John, Hydra, Hashcat
- **Social Eng**: SET, Sherlock, Hydra (social BF)
- **Stego**: Steghide
- **Forensics**: Autopsy, Volatility
- **Anonymity**: Tor, Proxychains
- **Info Gather**: Crunch (wordlists), Email Verify, IDN
- **Advanced**: hping3 (DDoS), msfvenom (RAT/Payloads), ADB (Android), Ghidra (RE), tmux

## Contributing
PRs welcome! Add tools by editing `main.py` functions.

## License
GNU GPL v3.0 (same as HackingToolkit).

## Disclaimer
**EDUCATIONAL ONLY.** For authorized pentesting/cybersec learning. Author not liable for misuse. Obey laws—don't hack without consent. No illegal activity.
