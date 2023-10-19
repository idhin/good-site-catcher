import logging
import sys
import datetime
import certstream
import tldextract

def print_callback(message, context):
    logging.debug("Message -> {}".format(message))

    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']

        if len(all_domains) == 0:
            domain = "NULL"
        else:
            domain = all_domains[0]

        # Mengekstrak tld dari domain
        ext = tldextract.extract(domain)
        tld = f"{ext.domain}.{ext.suffix}"

        # Menyimpan URL yang valid ke dalam results.txt
        with open('results.txt', 'a') as f:
            f.write(tld + '\n')

        sys.stdout.write(u"[{}] {} (SAN: {})\n".format(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S'), domain, ", ".join(message['data']['leaf_cert']['all_domains'][1:])))
        sys.stdout.flush()

logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(message)s', level=logging.INFO)

certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io/')
