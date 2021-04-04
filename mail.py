import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = ""
receiver_email = ""
password = ''
subject = "ALERTE!!"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

body = 'Ya du monde à la maiz'
msg.attach(MIMEText(body, 'plain'))

filename = 'philippe.jpg'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

try:
    server.sendmail(sender_email, receiver_email, text)
    print('Mail sent successfully')
except Exception as e:
    print(f'Sorry, there was a problem {e}')
server.quit()
