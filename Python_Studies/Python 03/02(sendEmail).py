import smtplib

sender = "hentgenp2@gmail.com"
receiver = "testuserr19993@gmail.com"
password = "pr0gr4mm3r4l1f3$"
subject = "Python Email test"
body = "I just made a bot to send email!"


# Header
message = f"""From: SnoopDog{sender}
To: Dr.Dre{receiver}

Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in ...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")