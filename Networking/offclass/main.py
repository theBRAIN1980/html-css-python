import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

server.login('dragosh_79@yahoo.com', '1234Qwerasdfzxcv,')

msg = MIMEMultipart
msg['From'] = 'Yahoo'
msg['To'] = 'popescu.dragos1980@gmail.com'
msg['Subject'] = 'Just a test'

with open ('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'PinkyAndBrain.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('dragosh_79@yahoo.com', 'popescu.dragos1980@gmail.com', text)
