import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(_from: str, _pass: str, _to: str, html):
    try:
        port = 587  # For starttls
        '''
        Ports 465 and 587 are intended for email client to email server communication - sending out email using SMTP protocol. Port 465 is for smtps (smtp secure). SSL encryption is started automatically before any SMTP level communication. Port 587 is for msa (message submission agent).
        Since, Google doesn't allow less secure apps to send mails, we use port 587 rather than port 465.
        '''
        smtp_server = "smtp.gmail.com"
        sender_email = _from
        receiver_email = _to
        password = _pass

        message = MIMEMultipart('alternative')
        message['Subject'] = "Movie Review Request"
        message['From'] = _from
        message['To'] = _to
        message.attach(MIMEText(html, 'html'))

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        return False
        # main.main()