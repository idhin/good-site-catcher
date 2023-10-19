import tldextract

def is_valid_domain(domain):
    extracted = tldextract.extract(domain)
    return bool(extracted.domain) and bool(extracted.suffix)

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        domain = line.strip()
        if '*' in domain:
            domain = domain[2:]  # Menghilangkan dua karakter pertama (bintang dan titik)
        if is_valid_domain(domain):
            print(domain)