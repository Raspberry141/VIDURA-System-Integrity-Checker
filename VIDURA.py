from pyfiglet import figlet_format
from colorama import Fore, Style
import platform, hashlib, os

print(Fore.GREEN + figlet_format("VIDURA"))
print(Fore.RED + "[*] Created by Vizz\n" + Style.RESET_ALL)

print(Fore.CYAN + str(platform.uname()) + Style.RESET_ALL)

def check_integrity(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    sha = hashlib.sha256(data).hexdigest()
    print(Fore.YELLOW + f"[+] SHA256({file_path}) = {sha}" + Style.RESET_ALL)

check_integrity("suspicious.exe")