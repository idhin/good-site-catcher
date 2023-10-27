import requests
from colorama import Fore, Style, init
import sys

# Inisialisasi colorama
init()

def check_website(url):
    if not url.startswith('https://'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"{Fore.GREEN}{url} - Active{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}{url} - Inactive{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.YELLOW}{url} - Error: {str(e)}{Style.RESET_ALL}"

def main(input_file):
    with open(input_file, 'r') as file:
        websites = file.read().splitlines()

    with open('live.txt', 'w') as live_file:
        for i, website in enumerate(websites, start=1):
            result = check_website(website)
            print(f"Progress: {i}/{len(websites)}", end='\r')
            sys.stdout.flush()
            print(result)
            live_file.write(result + '\n')

if __name__ == '__main__':
    input_file = input("Masukkan nama file dengan daftar website: ")
    main(input_file)
    print("\nProses selesai. Hasil disimpan dalam file live.txt.")
