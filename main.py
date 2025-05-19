import report_genration
import Email
import os


if __name__ == "__main__":
    report_genration.run()
    Email.send_email_to_contacts()
    print("All reports are sent successfully.")
 

 

# This script generates a summary report from a PDF file and sends it via email to a list of contacts.