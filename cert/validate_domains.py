import tldextract

def is_valid_domain(domain):
    extracted = tldextract.extract(domain)
    if bool(extracted.domain) and bool(extracted.suffix):
        # Tambahkan aturan untuk memeriksa kata kunci yang tidak diinginkan
        unwanted_keywords = ['azure', 'cpanel', 'cloudflare', 'aws.dev', 'git', 'mongodb']
        if not any(keyword in domain.lower() for keyword in unwanted_keywords):
            return True
    return False

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        domain = line.strip()
        if '*' in domain:
            domain = domain[2:]  # Menghilangkan dua karakter pertama (bintang dan titik)
        if is_valid_domain(domain):
            print(domain)
