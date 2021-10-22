import smtplib

gmail_user = 'abar.toha@gmail.com'
gmail_password = 'ManIHateThisStuffxxx69xx420'

sent_from = gmail_user
to = ['abar.toha2@gmail.com']
subject = 'TEST'
body = 'IT WORKS\n\n- You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except Exception as e:
    print (e)