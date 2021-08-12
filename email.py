import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from password import password

port=587
sender_address="sender_email@gmail.com"  #sender's email id
receiver_address="receiver_email@gmailcom"   # recever's email id

msg=MIMEMultipart()
msg['From']=sender_address
msg['To']=receiver_address
msg['Subject']="Sending mail using python"  #E-mail Subject
body="Hello. This mail is sent using Python"   #E-mail body

msg.attach(MIMEText(body, 'plain'))

filename="srishti_img.jpg"   #sending images
attachment=open(filename, "rb")

p=MIMEBase('application', 'octet-stream')

p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content=Disposition', "attachment; filename %s " % filename)

#attaching p instace to msg
msg.attach(p)

#creating SMTP session
server=smtplib.SMTP("smtp.gmail.com", port)
server.starttls()
server.login(sender_address, password)


#coverting multi-part message to string
text=msg.as_string()
server.send_message(msg)


server.quit()













