import smtplib
from email.mime.text import MIMEText

# Define to/from
sender = 'focusapp@zohomail.in'
recipient = 'kilikkoottiilaromal@gmail.com'

# Create message
msg = MIMEText("Message text")
msg['Subject'] = "Sent from python"
msg['From'] = sender
msg['To'] = recipient

# Create server object with SSL option
server = smtplib.SMTP_SSL('smtp.zoho.in', 465)

# Perform operations via server
server.login('focusapp@zohomail.in', 'FOCUS@123')
server.sendmail(sender, [recipient], msg.as_string())
server.quit()

print("hello")