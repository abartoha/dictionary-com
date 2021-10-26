import smtplib
from os import environ
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from json import dumps

def mail_it(obj, count):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(environ['EMAIL'], environ['PASS'])
        print('logged in')
        # email content
        subject = f"Dictionary Words {count}"
        body = f"Here are the words objects for dictionaries {count-25000} to {count}"
        msg = MIMEMultipart()
        msg['From'] = environ['EMAIL']
        msg['To'] = COMMASPACE.join('abar.toha2@gmail.com')
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(body))
        print('main body written')
        # email attachment (binary)
        part = MIMEApplication(dumps(obj).encode('utf-8'), Name=f"dictionary-{count}.json")
        part['Content-Disposition'] = f'attachment; filename="dictionary-{count}.json"'
        msg.attach(part)
        print('attachment done')
        #send
        smtp.sendmail(environ['EMAIL'], 'abar.toha2@gmail.com', msg.as_string())
        print('sent')

if __name__=="__main__":
    mail_it({'name':'AlRazi'}, 25000)