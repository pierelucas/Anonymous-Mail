# Anonymous Mail from Anonymouse.org - Send mail over Anonymouse.org
#
# Creation:    04.10.2019
# Last Update: 04.10.2019
#
#
# MIT License
#
# Copyright (c) 2019 by PiereLucas
# https://github.com/pierelucas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#
# Module
#
import requests, sys, subprocess
from colorama import Fore, Style

#
# Global Objects
#
banner_txt = """
 _______ __   _  _____  __   _ __   __ _______  _____  _     _ _______     _______ _______ _____       
 |_____| | \  | |     | | \  |   \_/   |  |  | |     | |     | |______ ___ |  |  | |_____|   |   |     
 |     | |  \_| |_____| |  \_|    |    |  |  | |_____| |_____| ______|     |  |  | |     | __|__ |_____
"""

useragent_txt = """
[1] Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0\n
[2] Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36\n
[3] BrightSign/8.0.69 (XT1143)Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.11.2 Chrome/65.0.3325.230 Safari/537.36\n
[4] Own
"""

#
# Functions
#
def out():

    subprocess.call("clear", shell=True)
    print(Fore.CYAN + banner_txt + Style.RESET_ALL)

def user_agent():

    print(useragent_txt)
    choice = str(input("Choose User-Agent : "))
    if choice == '1':
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
    elif choice == '2':
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    elif choice == '3':
        user_agent = "BrightSign/8.0.69 (XT1143)Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.11.2 Chrome/65.0.3325.230 Safari/537.36"
    else:
        user_agent = str(input("Your User Agent : "))

    return user_agent

def data_():

    print("Mail to : ")
    to = str(input())
    print("Subject : ")
    subject = str(input())
    print("Message : ")
    message = str(input())

    return to, subject, message

def run(to, subject, message, ua):

    user_agent = ua
    url = "http://anonymouse.org/cgi-bin/anon-email.cgi"

    session = requests.Session()
    request = session.post(url, headers={
        "Host": "anonymouse.org",
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	        "Accept-Language": "en-US,en;q=0.5",
	        "Accept-Encoding": "gzip, deflate",
	        "Referer": "http://anonymouse.org/anonemail.html",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type":"application/x-www-form-urlencoded"
    }, data={
        "to": to,
        "subject": subject,
        "message": message
    })

    if "The e-mail has been sent" in request.text:
        print("Sucessfully sended")
    else:
        print("Email not sended")
        sys.exit(0)

#
# TO BE CONTINUED ...
#
out()

ua = user_agent()
to, subject, message = data_()

run(to, subject, message, ua)
