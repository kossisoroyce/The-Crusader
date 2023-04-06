#!/usr/bin/env python

import os
import subprocess
import smtplib
import requests
from twilio.rest import Client

# Enter your email credentials
email_address = "your_email_address"
email_password = "your_email_password"
recipient_email = "recipient_email_address"

# Enter your Twilio account details
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_phone_number = "your_twilio_phone_number"
recipient_phone_number = "recipient_phone_number"

# Enter the URL of the WordPress site to scan
url = input("Enter the URL of the WordPress site to scan: ")

# Check if the URL is valid
try:
    response = requests.get(url)
    if response.status_code != 200:
        print("Invalid URL!")
        exit()
except:
    print("Invalid URL!")
    exit()

# Enter the path to the wp-content directory
wp_content_path = input("Enter the path to the wp-content directory: ")

# Check if the wp-content directory exists
if not os.path.exists(wp_content_path):
    print("Invalid path!")
    exit()

# Define the command to scan the wp-content directory for malware
clamscan_command = 'clamscan -r -i %s' % wp_content_path

# Run the clamscan command and capture the output
process = subprocess.Popen(clamscan_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# Send email and text message with the scan results
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, email_password)
message = "Subject: ClamAV Scan Results for %s\n\nThe ClamAV scan on %s found the following:\n\n%s" % (url, url, str(output))
server.sendmail(email_address, recipient_email, message)
server.quit()

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="ClamAV scan results for %s sent to %s" % (url, recipient_email),
    from_=twilio_phone_number,
    to=recipient_phone_number
)
