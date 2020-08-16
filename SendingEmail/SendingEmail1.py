#! /usr/bin/env python2

import smtplib
from smtplib import SMTPException

#sender = 'sender@test.com'
sender = 'takashi.ichimasa.omajinai@gmail.com'
#receivers = 'receiver@test.com'
receivers = 'takashi.ichimasa.omajinai@gmail.com'

myaddress = 'takashi.ichimasa.omajinai@gmail.com'
mypasswd = 'ichima0609@ichima3'

message = """ From : From Person
To : To PersonSubject : SMTP email test


this is a test email message. """

try:
    smtpObj = smtplib.SMTP(host='takashi.ichimasa.omajinai@gmail.com', port=1026)
    smtpObj.starttls()
    smtpObj.login(myaddres, mypasswd)

    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except SMTPException:
    print "Error : unbale to send email"
