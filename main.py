import smtplib
import ssl
from email.message import EmailMessage

# make sure "Less secure apps is turned on in your google settings"
# does not work if you have 2 factor auth

subject = "Python Email"
body = "This is sent using Python"
sender_email = "sarthakgautam18@gmail.com"
receiver_email = "sarthakgautam18@gmail.com"
password = input("Enter the password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body)  # commented for sending html

html = f'''
<html>
    <body>
        <h3>{subject}</h3>
        <p>{body}</p>
    </body>
</html>
'''
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email")  # testing
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string)
print("Email Sent!")  # testing
