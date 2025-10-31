import random
import smtplib
from email.message import EmailMessage

def generate_otp():
    otp = random.randint(100000,999999)
    return otp

def sending_mail(receiver,sender,password,otp):
    email_msg = EmailMessage()
    email_msg['To'] = receiver
    email_msg['From'] = sender
    email_msg['Subject'] = "Your OTP for verification"
    body = f"Please enter your OTP when asked {otp}"
    email_msg.set_content(body) #used to add the data to the email object(set_content)

    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls() #transport layer security(tls)
    server.login(sender,password)
    server.send_message(email_msg, to_addrs=receiver)
    server.quit()

    print('OTP sent')

def otp_verification(otp):
    votp = int(input('Enter the otp you received: '))
    if otp == votp:
        print('Verification successful')
    else:
        print('verification unsuccessful')

otp = generate_otp()
receiver = input("Please enter receiver mail id: ")
sender = "21jr1a12b6@gmail.com"
password = 'hxnc cssg jyxk gayi' #this is the app passwords,it creates one new 16 digit password for email account,and we must enable 2 step verfication
sending_mail(receiver,sender,password,otp)
otp_verification(otp)


























    


















    
