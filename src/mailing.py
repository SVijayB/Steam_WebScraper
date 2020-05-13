from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def email(item,username,password):
	host = "smtp.gmail.com"
	port = 587
	message = "Hey! We found your Steam Item at a lower price!"
	connection = smtplib.SMTP(host,port)
	connection.ehlo()
	connection.starttls() 
	connection.login(username,password)
	connection.sendmail(username,username,message)
	connection.quit()