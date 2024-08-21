import smtplib, ssl

port = 2525  # For SSL
smtp_server = "smtp.elasticemail.com"
sender_email = "abhijeetsasmal74@gmail.com"  # Enter your address
receiver_email = "abhijeetsasmal74@gmail.com"  # Enter receiver address
password = '6112376BD659748F3E42E62407D92A5D3398'

def send(msg,receiver_email):
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)


message = """\
Subject: Forgot Password

Pls click on this link to reset localhost:8000/forgot?id=1"""

send(message, "abhijeetsasmal74@gmail.com")