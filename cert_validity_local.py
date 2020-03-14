# Part 1: Check SSL certificate expiry date of local server

import sys
from datetime import datetime
import OpenSSL
import ssl, socket

# ANSI code colour
class style():
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)

# check for valid arg input
if len(sys.argv) < 3:
    print("ERROR: python3 cert_validity_remote.py <hostname> <port>")
    exit(-1)

# initialize host/port
hostname = sys.argv[1]
port = sys.argv[2]

# retrive server ssl expiry
try:
    cert = ssl.get_server_certificate((hostname, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiry_date = x509.get_notAfter().decode('ascii')
except:
    print("ERROR: Server not found")
    exit(-1)

expiry_date = datetime.strptime(expiry_date, "%Y%m%d%H%M%SZ")

# current time
utc_datetime = datetime.utcnow()

# compare current and expiry datetimes
delta = expiry_date-utc_datetime

# print results
print(expiry_date, end = " ")

if (delta.days < 15):
    print(style.RED("CRITICAL"))
elif (delta.days <= 30):
    print(style.YELLOW("WARNING"))
else:
    print(style.GREEN("INFO"))
