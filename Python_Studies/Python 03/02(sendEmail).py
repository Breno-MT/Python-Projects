import smtplib

sender = "random@gmail.com"
receiver = "userrandom@gmail.com"
password = "password"
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