import os
import dhooks
from dhooks import Webhook
import time
import requests, os
import colorama
from colorama import Fore
colorama.init()
from pystyle import Colors
from pystyle import Write
from discord.utils import get

os.system("title Skidhook ✗ ┃ Dev: atx ~ Main")
os.system("cls")

def menu():
    os.system("title Skidhook ✗ ┃ Dev: atx ~ Main")
    print(f"""{Fore.CYAN}
.▄▄ · ▄ •▄ ▪  ·▄▄▄▄   ▄ .▄            ▄ •▄ 
▐█ ▀. █▌▄▌▪██ ██▪ ██ ██▪▐█▪     ▪     █▌▄▌▪
▄▀▀▀█▄▐▀▀▄·▐█·▐█· ▐█▌██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·
▐█▄▪▐█▐█.█▌▐█▌██. ██ ██▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌
 ▀▀▀▀ ·▀  ▀▀▀▀▀▀▀▀▀• ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀
{Fore.BLUE}╚═► {Fore.BLUE}Github: @passedout
{Fore.BLUE}╚═► {Fore.CYAN}Telegram: @boobjob {Fore.RESET}
""")
    print(f"{Fore.BLUE}╔═══════════════════╗\n║{Fore.CYAN}[1] Delete Webhook {Fore.BLUE}║")
    print(f"{Fore.BLUE}║{Fore.CYAN}[2] Spam Webhook   {Fore.BLUE}║")
    print(f"{Fore.BLUE}║{Fore.CYAN}[3] Check Webhook  {Fore.BLUE}║")
    print(f"{Fore.BLUE}║{Fore.CYAN}[4] Credits        {Fore.BLUE}║")
    print(f"{Fore.BLUE}║{Fore.CYAN}[0] Quit           {Fore.BLUE}║\n╚═══════════════════╝")


menu()
option = int(input(f"{Fore.CYAN}╔══{Fore.BLUE}[{Fore.CYAN}Choose your option{Fore.BLUE}]{Fore.CYAN}{Fore.CYAN}\n╚══►{Fore.BLUE} "))

while option !=0:
    if option ==1:
        os.system("title Skidout ✗ ┃ Dev: exte ~ Delete Webhook")
        webhook = input(f"{Fore.CYAN}╔══{Fore.BLUE}[{Fore.CYAN}Enter the webhook you want to delete{Fore.BLUE}]{Fore.CYAN}{Fore.CYAN}\n╚══►{Fore.BLUE} ")
        checkkl = requests.get(webhook)
        if checkkl.status_code == 200:
            print(f"\n {Fore.BLUE}[{Fore.WHITE}System{Fore.BLUE}] {Fore.CYAN}Deleted {Fore.GREEN}{webhook}{Fore.MAGENTA}")
            requests.delete(webhook)
            os.system("pause >nul")
            os.system("cls")
        elif checkkl.status_code == 404:
            Write.Print(f"\n [System] ", Colors.green, interval=0.000001), print(f"{Fore.MAGENTA}Webhook is {Fore.RED}Invalid")
            os.system("pause >nul")
            os.system("cls")

    elif option ==2:
        os.system("title Skidhook ✗ ┃ Dev: atx ~ Spam Webhook")
        webhookurl = Webhook(input(f"{Fore.CYAN}╔══{Fore.BLUE}[{Fore.CYAN}Enter webhook{Fore.BLUE}]{Fore.CYAN}{Fore.CYAN}\n╚══►{Fore.BLUE} "))
        message = input(f"{Fore.CYAN}╔══{Fore.BLUE}[{Fore.CYAN}What do you want to spam{Fore.BLUE}]{Fore.CYAN}{Fore.CYAN}\n╚══►{Fore.BLUE} ")

        while True:
            time.sleep(0)
            webhookurl.send(message + " | https://discord.gg/rtx 卍**CringeHook**卐", avatar_url="https://cdn.discordapp.com/attachments/958414220926533703/985556711978963004/bleed_transparent.png", username="Skidbot | Github: @passedout")
            print(f"{Fore.CYAN}╚══►{Fore.GREEN}Message Sent.")
            time.sleep(0)
            print(f"{Fore.CYAN}╔══{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.BLUE}: {Fore.YELLOW}\"ctrl + c\" {Fore.BLUE}AT ANY TIME TO STOP!!")

    elif option ==3:
        os.system("title Skidhook ✗ ┃ Dev: atx ~ Check Webhook")
        webhook = input(f"{Fore.CYAN}╔══{Fore.BLUE}[{Fore.CYAN}Enter the webhook you want to check{Fore.BLUE}]{Fore.CYAN}{Fore.CYAN}\n╚══►{Fore.BLUE} ")
        check = requests.get(webhook)
        if check.status_code == 404:
            Write.Print(f"\n [System] ", Colors.green, interval=0.000001), print(f"{Fore.MAGENTA}Webhook is {Fore.RED}Invalid")
            os.system("pause >nul")
            os.system("cls")

        elif check.status_code == 200:
            Write.Print(f"\n [System] ", Colors.green, interval=0.000001), print(f"{Fore.MAGENTA}Webhook is {Fore.GREEN}Valid")
            os.system("pause >nul")
            os.system("cls")
            
    elif option ==4:
        os.system("title Skidhook ✗ ┃ Dev: atx ~ Credits")
        os.system("cls")
        Write.Print("Github: @passedout\nClippy: @sex\nT.me: @boobjob\nCurrent Dc Server: .gg/rtx\n\n[Hit \"Enter\" To Return]", Colors.white, interval=0.000001)
        os.system("pause >nul")
        os.system("cls")
    else:
        print(f"{Fore.RED}Invalid Option")
        os.system("pause >nul")
        os.system("cls")
        
    print()
    menu()
    option = int(input(f"{Fore.CYAN}╔══{Fore.BLUE}[{Fore.CYAN}Choose your option{Fore.BLUE}]{Fore.CYAN}{Fore.CYAN}\n╚══►{Fore.BLUE} "))

os.system("title Skidhook ✗ ┃ Dev: atx ~ Byebye :(")
os.system("cls")
Write.Print("Thx for using SkidHook, Goodbye!\n\n[Hit \"Enter\" To exit]", Colors.white, interval=0.000001)
os.system("pause >nul")
os.system("cls")
