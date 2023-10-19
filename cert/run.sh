#jangan lupa di chmod +x dulu validate domains nya
certstream --json | jq -r '.data.leaf_cert.all_domains[]' | python3 validate_domains.py | tee -a output.txt