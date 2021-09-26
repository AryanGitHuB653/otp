import smtplib
import random
print('*'*15)
k = input('enter email ')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('python.bot75@gmail.com','adyaesziprmhepwg')
otp = random.randint(100000,999999)    
msg = 'Hi , thank you for creating your account , here is your otp-->'+str(otp)
server.sendmail('python.bot75@gmail.com',k,msg)
server.close()
password_input = int(input("Enter the otp sent on your mail for verification"))
if password_input == otp:
    print('YAY!, YOU ARE A MEMBER NOW')
else:
    print('Please try again')
# email_otp()
input()
        
