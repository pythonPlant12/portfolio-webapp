import smtplib, ssl


def send_email():
    host = "smtp.gmail.com"
    port = 465
    username = "testpythonplant@gmail.com"
    password = "rmtztiqhliswezbi"
    receiver = "testpythonplant@gmail.com"
    message = """\
Subject: Hi!
How are you?
Bye!
"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)


send_email()
