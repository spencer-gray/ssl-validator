# Part 2: Check SSL certificate expiry date of remote server

from urllib.request import Request, urlopen, ssl, socket
from datetime import datetime, date
import sys
import json

# ANSI code colour
class style():
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)

# check for valid arg input
if len(sys.argv) < 2:
    print("ERROR: python3 cert_validity_remote.py www.google.ca")
    exit(-1)

# initialize host/port
hostname = sys.argv[1]
port = '443'

# connect to server and pull ssl info
context = ssl.create_default_context()
try:
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            data = ssock.getpeercert()
except socket.error:
    print("ERROR: Server not found")
    exit(-1)

# current time
utc_datetime = datetime.utcnow()

# expiry datetime
expiry_date = data["notAfter"]
expiry_date = datetime.strptime(expiry_date, "%b %d %H:%M:%S %Y %Z")

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
