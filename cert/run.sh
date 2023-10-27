# Periksa sertifikat pada aliran sertifikat
certstream --json | jq -r '.data.leaf_cert.all_domains[]' | \

# Validasi domain menggunakan skrip Python
python3 validate_domains.py | \

# Filter hasil dengan blacklist
grep -v -f blacklist.txt | \

# Simpan hasil ke output.txt
tee -a output.txt