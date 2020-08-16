#! /usr/bin/env python2

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content =  ''' Hello,
This is a simple mail . There is only text, no attachment are there The mail is sent using Python SMTP library.
Thank you
'''

#sender = 'sender@test.com'
sender_address = 'takashi.ichimasa.omajinai@gmail.com'
sender_passwd = 'ichima0609@ichima3'
#receivers = 'receiver@test.com'
receivers_address = 'takashi.ichimasa.omajinai@gmail.com'

myaddress = 'takashi.ichimasa.omajinai@gmail.com'
mypasswd = 'ichima0609@ichima3'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receivers_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.' 

#the body and attachments for the mail
message.attach(MIMEText (mail_content, 'plain'))

#Create SMTP session for sending mail
#message = """ From : From Person
#To : To PersonSubject : SMTP email test 
#this is a test email message. """

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(sender_address, sender_passwd)
text = message.as_string()

smtpObj.sendmail(sender_address, receivers_address, text)
smtpObj.quit()
print "Successfully sent email"

