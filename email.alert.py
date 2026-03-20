import smtplib
from email.mime.text import MIMEText

# Email config
smtp_server = 'smtp.gmail.com'
port = 587

sender_email = 'rkahmad987@gmail.com'
receiver_email = 'rkahmad987@gmail.com+'
password = 'yourpassword'   # ⚠️ yaha apna App Password daalo

# Message
message = "sorry"

msg = MIMEText(message)
msg['Subject'] = 'Message'
msg['From'] = sender_email
msg['To'] = receiver_email

# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully ✅")