import imaplib
import email
import os
import shutil

EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
IMAP_SERVER = "imap.example.com"
SPAM_FOLDER = "SPAM"  # Or "Junk"
DESTINATION_FOLDER = "Trash"

def move_spam_to_trash():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mail.select(SPAM_FOLDER)

        typ, data = mail.search(None, 'ALL')
        for num in data[0].split():
            typ, msg_data = mail.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    mail.copy(num, DESTINATION_FOLDER)
                    mail.store(num, '+FLAGS', '\\Deleted')  # Mark for deletion

        mail.expunge()

        mail.close()
        mail.logout()

        print(f"Successfully moved messages from {SPAM_FOLDER} to {DESTINATION_FOLDER}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    move_spam_to_trash()
