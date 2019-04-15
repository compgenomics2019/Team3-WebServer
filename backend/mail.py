#!/usr/bin/env python3

import argparse
import smtplib
from email.mime.text import MIMEText

EMAIL = "predict2019t3@mailgun.marlin.pub"
PASS  = "DummyPassword"
REPLY = "jialin@gatech.edu"
SMTP_SERVER = "smtp.mailgun.org"

TEMPLATE = """

Hi,

Your submitted job is finished. Please visit using the following link:

http://predict2019t3.biosci.gatech.edu/result/{}

Best,
Jialin Ma
"""

def send(to, res_id):
    msg = MIMEText(TEMPLATE.format(res_id))
    msg['Subject'] = "Your submitted job is finished!"
    msg['From'] = EMAIL
    msg['To'] = to
    msg['Reply-to'] = REPLY
    smtp = smtplib.SMTP(SMTP_SERVER, 587, timeout = 360)
    smtp.login(EMAIL, PASS)
    smtp.send_message(msg)
    smtp.quit()
    return True

def main():
    parser = argparse.ArgumentParser(description = "Send email to user.")
    parser.add_argument("--to", required = True)
    parser.add_argument("--resid", required = True)
    args = parser.parse_args()
    send(args.to, args.resid)

if __name__ == "__main__":
    main()
