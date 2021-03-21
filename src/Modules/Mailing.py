from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def email(username, password):
    host = "smtp.gmail.com"
    port = 587
    connection = smtplib.SMTP(host, port)
    connection.ehlo()
    connection.starttls()
    connection.login(username, password)
    tmessage = MIMEMultipart("alternate")
    tmessage["Subject"] = "Steam Item found at a lower price!"
    tmessage["From"] = username
    tmessage["To"] = username

    html_message = """
    <html>
        <body>
            <h3>MESSAGE FROM STEAM_WEBSCRAPPER : </h3>
            <p>Hey! We found your Steam Item at a lower price!</p>
        </body>
    </html>
                    """
    msg = MIMEText(html_message, "html")
    tmessage.attach(msg)
    connection.sendmail(username, username, tmessage.as_string())
    connection.quit()
