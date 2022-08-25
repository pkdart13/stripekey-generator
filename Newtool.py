import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style


def screen_clear():
    _ = os.system('cls')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

choiceusers = input(f"{Fore.WHITE}[{Fore.WHITE}!{Fore.WHITE}]{Fore.WHITE} What Is 37 {Fore.WHITE} + 13 = {Fore.WHITE} :  {Style.RESET_ALL}")
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

{gr}[{Fore.WHITE}1{gr}] IP RANGER (POWER = LOW )
{gr}[{Fore.WHITE}2{gr}] IP RANGER (POWER = MEDIUM )
{gr}[{Fore.WHITE}3{gr}] IP RANGER (POWER = HIGH )
{gr}[{Fore.WHITE}4{gr}] IP RANGER (POWER = MONSTER )
{gr}[{Fore.WHITE}5{gr}] IP RANGER ( GOD MODE  ) {yl} Caution : Never Use It 


"""
print(banners)
choiceusers = input(f"{gr}[{wh}!{wh}]{wh} Select an option  {wh} From Above {wh} :  {res}")
if choiceusers == "1":
	def ranges(ip):
		try:
			part = ip.split('.')
			a = part[0]
			b = part[1]
			c = part[2]
			d = part[3]
		
			for d in range(1, 256):
				ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
				print(ip_result)
				open('low_ranged.txt','a').write(ip_result+"\n") 
				
		except:
				     print("Error")
                   
elif choiceusers =="2":
	def ranges(ip):
	    try:
	        part = ip.split('.')
	        a = part[0]
	        b = part[1]
	        c = part[2]
	        d = part[3]
	        for c in range(1, 256):
	            ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
	            print(ip_result)
	            open('mid_ranged.txt','a').write(ip_result+"\n") 
				
				
	    except:
	        print("Error")
	        
elif choiceusers == "3":
	def ranges(ip):
	    try:
	        part = ip.split('.')
	        a = part[0]
	        b = part[1]
	        c = part[2]
	        d = part[3]
	        for c in range(1, 256):
	            for d in range(1, 256):
	                ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
	                print(ip_result)
	                open('high_ranged.txt','a').write(ip_result+"\n") 
				
				
	    except:
	        print("Error")
	

elif choiceusers == "4":
	def ranges(ip):
	    try:
	        part = ip.split('.')
	        a = part[0]
	        b = part[1]
	        c = part[2]
	        d = part[3]
	
	        for b in range(1, 256):
	            for c in range(1, 256):
	                 for d in range(1, 256):
	                     ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
	                     print(ip_result)
	                     open('monster_ranged.txt','a').write(ip_result+"\n") 
				
				
	    except:
	        print("Error")
	           
elif choiceusers == "5":
	def ranges(ip):
	    try:
	        part = ip.split('.')
	        a = part[0]
	        b = part[1]
	        c = part[2]
	        d = part[3]
	
	        for a in range(1, 256):
	            for b in range(1, 256):
	                 for c in range(1, 256):
	                     for d in range(1, 256):
	                         ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
	                         print(ip_result)
	                         
	                         open('god_mod_ranged.txt','a').write(ip_result+"\n")
				
				
	    except:
	        print("Error")	                      
ip = open(input(f"{bl} IP file Path ={gr}  "), 'r').read().split("\n")
thread = input(f"{bl} Threads Speed = {gr}")
if ip:
       try:
          
          with ThreadPoolExecutor(int(thread)) as pq:
              pq.map(ranges,ip)
              
       except:
                  
                 print("EoorRrrr")
          
