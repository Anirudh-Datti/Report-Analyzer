import smtplib
from email.message import EmailMessage
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = '' # Your email address
EMAIL_PASSWORD = '' # Your app password


# List of contacts
contacts = [
    '',
    '',
    # Add more contacts.
]

# Get all files from reports/summary_reports
summary_reports_dir = 'reports/summary_reports'
summary_report_files = [
    os.path.join(summary_reports_dir, f)
    for f in os.listdir(summary_reports_dir)
    if os.path.isfile(os.path.join(summary_reports_dir, f))
]

# Function to send email with attachments
def send_email_with_attachments(to_email, files):
    msg = EmailMessage()
    msg['Subject'] = 'Summary Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content('Please find the attached summary report files.')

    for file_path in files:
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_email_to_contacts():
    for contact in contacts:
        send_email_with_attachments(contact, summary_report_files)
