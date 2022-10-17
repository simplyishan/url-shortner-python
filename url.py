import requests
import time
import os
from colorama import Fore
logo = Fore.LIGHTRED_EX + """


        ██╗░░░██╗██████╗░██╗░░░░░  ░██████╗██╗░░██╗░█████╗░██████╗░████████╗███╗░░██╗███████╗██████╗░
        ██║░░░██║██╔══██╗██║░░░░░  ██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██╔════╝██╔══██╗
        ██║░░░██║██████╔╝██║░░░░░  ╚█████╗░███████║██║░░██║██████╔╝░░░██║░░░██╔██╗██║█████╗░░██████╔╝
        ██║░░░██║██╔══██╗██║░░░░░  ░╚═══██╗██╔══██║██║░░██║██╔══██╗░░░██║░░░██║╚████║██╔══╝░░██╔══██╗
        ╚██████╔╝██║░░██║███████╗  ██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░██║░╚███║███████╗██║░░██║
        ░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

                                         BY SIMPLYISHAN
"""
print(logo)
longurl = input(Fore.LIGHTCYAN_EX +
                '> Enter Your Long Url (without spaces)   ' + Fore.WHITE + ': ')
shortenurl = input(Fore.LIGHTCYAN_EX + '> Enter The Shorten Url (without spaces)  ' +
                   Fore.WHITE + ': https://ulvis.net/')
if longurl.startswith('https://' or 'http://'):
    resurl = f'https://ulvis.net/api.php?url={longurl}&custom={shortenurl}&private=1'
    res = requests.get(resurl)
    print(res.text)
    with open('shorturls.txt', 'w') as f:
        f.write(f'Main Url :{longurl} ' + '-' + f'Short Url : {res.text}')
        f.close()
    time.sleep(2)
    print('The Main And Short Is Saved In Txt File ')
    print('Thanks For Using Url Shortner By simplyishan')
    time.sleep(4)
    exit()
elif longurl.startswith('http://'):
    resurl = f'https://ulvis.net/api.php?url={longurl}&custom={shortenurl}&private=1'
    res = requests.get(resurl)
    print(res.text)
    with open('shorturls.txt', 'w') as f:
        f.write(f'Main Url :{longurl} ' + '-' + f'Short Url : {res.text}')
        f.close()
    time.sleep(2)
    print('The Main And Short Is Saved In Txt File ')
    print('Thanks For Using Url Shortner By simplyishan')
    time.sleep(4)
    exit()
else:
    print(Fore.RED + 'use http:// or https:// before the long url ')
    time.sleep(3)
    os.system('cls')
    os.system('python url.py')
