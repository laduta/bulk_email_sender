import smtplib
import pandas as pd
from email.message import EmailMessage

# Load recipient data
df = pd.read_csv("recipients.csv")  # Columns: Name, Email

# Email login
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_16_char_app_password"  # Use Gmail App Password

# Setup SMTP server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


# Load email message template
with open("email_template.txt", "r") as f:
    template = f.read()

# Loop through recipients
for index, row in df.iterrows():
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = row['Email']
    msg['Subject'] = "Your Personalized Update"

    # Fill in the template
    personalized_message = template.replace("{name}", row['Name'])
    msg.set_content(personalized_message)

    try:
        server.send_message(msg)
        print(f"Sent to {row['Name']} at {row['Email']}")
    except Exception as e:
        print(f"Failed to send to {row['Email']}: {e}")

server.quit()
