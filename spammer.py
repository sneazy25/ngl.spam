
import pyfiglet
import requests
import os
from colorama import Fore, init
from random import randint

    

init(autoreset=False)

red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE
blue = Fore.BLUE

r = requests.Session()

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + 'Gunakan dengan bijak :)\n')  
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By @ardynvyn__ {red}]\n")

banner("NGL.LINK")
target = input(f"{red}[{white}?{red}] {white}Masukan target : ")
question = input(f"{red}[{white}?{red}] {white}Masukan pertanyaan : ")
start = input(f"{red}[{white}?{red}] {white}Ketik Y/N : ").upper()
def spam():
    questions_count = 0
    url = f"https://ngl.link/{target}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    payload = {
        "question": question
    }
    while True:
        spam = r.post(url, headers=headers, data=payload)
        questions_count += 1
        print(f"\n{Fore.GREEN}{questions_count} {Fore.WHITE}Questions Sent to: {Fore.RED}{target}")
        
if start == "Y":
    spam()
else:
    print("Invalid Response")
    exit()
