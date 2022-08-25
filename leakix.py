import requests, json
from colorama import Fore,Style
from concurrent.futures import ThreadPoolExecutor
import time
import platform
import os

if platform=='win32':
   system('color')

if os.name == 'nt':
   os.system('cls')
else:
   os.system('clear')

blue = Fore.BLUE
green = Fore.GREEN
red = Fore.RED
stop = Style.RESET_ALL



banners = f"""
"""
print(banners)
choiceusers = input(f"WHAT IS 37 + 13 =  :  {Style.RESET_ALL}")
if choiceusers == "50":

  banners = f"""
Login Sucess
\033[35m
░██████╗██╗░░██╗░█████╗░██████╗░██╗███████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██║██╔════╝
╚█████╗░███████║███████║██████╔╝██║█████╗░░
░╚═══██╗██╔══██║██╔══██║██╔══██╗██║██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░

   Special thanks \033[35m@Srfxdz

{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] LARAVEL IP GRABBING BY LEAKIX
"""
print(banners)
choiceusers = input(f"{Fore.GREEN}°°°°°°{Fore.RED}>  {Style.RESET_ALL}")

if choiceusers == "1":
   def grab(keywords):
       for pages in range(500000):
           print(f"\n{Fore.GREEN}Pages : {pages}{Style.RESET_ALL}")
           vars = 'https://leakix.net/search?page='+str(pages)+'&q='+keywords+'&scope=leak'
           headers = {'api-key': 's', 'Accept': 'application/json'}
           response = requests.get(vars, headers=headers).text
           tojson = json.loads(response)
           for results in tojson:
               lovs = results['ip']
               print(lovs)
               saves = open('LEAKIX.txt','a')
               saves.write(lovs+"\n")
               saves.close()

   keywords = input('\r\r•••••••••••••••> ').split()
   threads = input('\r\r•••••••••••••••>')
   if keywords:
     try:
        with ThreadPoolExecutor(int(threads)) as l:
            l.map(grab,keywords)
     except Exception as w:
        print(w)

elif choiceusers == "2":
	print("ma chuda")
     