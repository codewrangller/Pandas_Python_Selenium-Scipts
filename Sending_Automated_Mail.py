import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os
import pandas as pd
import calendar
import getpass

password = getpass.getpass(prompt='Please type in your password:')
email_sender = #'email address'

e = pd.read_excel("Users.xlsx")
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(email_sender, password)

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
calendar = calendar.month_abbr[4]

body = ("""
Hi there,

Please kindly find attached your attachment for the month APR 2021 

Thank you
""")
subject = f"Bank Schedule for {calendar}, {currentYear}"
fromaddr= email_sender

for index, row in e.iterrows():
    print (row["Email"]+row["FilePath"])
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    filename = row["FilePath"]
    toaddr = row["Email"]
    attachment = open(row["FilePath"], "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

print("Emails sent successfully")

server.quit()
