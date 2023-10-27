import requests
import threading

def check_website(url):
    if not url.startswith('https://'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return url, True
    except Exception as e:
        pass

    return url, False

def main(input_file):
    with open(input_file, 'r') as file:
        websites = file.read().splitlines()

    def check_and_write(website):
        url, active = check_website(website)
        if active:
            with lock:
                live_file.write(url + '\n')
                print(f"ℹ️ {url} - Active")
        else:
            print(f"⚠️ {url} - Inactive or Error")

    with open('live.txt', 'w') as live_file:
        lock = threading.Lock()
        threads = []

        for website in websites:
            thread = threading.Thread(target=check_and_write, args=(website,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == '__main__':
    input_file = input("Masukkan nama file dengan daftar website: ")
    main(input_file)
    print("\nProses selesai. Hasil disimpan dalam file live.txt.")
