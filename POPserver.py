import poplib
import ssl

def connect_to_pop_server(host, port, username, password, use_ssl=True):
    
    try:
        if use_ssl:
            context = ssl.create_default_context()
            mailbox = poplib.POP3_SSL(host, port, context=context)
            print("Connecting to POP3 server using SSL.")
        else:
            mailbox = poplib.POP3(host, port)
            print("Connecting to POP3 server.")

        mailbox.user(username)
        mailbox.pass_(password)

        print("Successfully connected and logged in.")
        return mailbox

    except poplib.error_proto as e:
        print(f"POP error: {e}")
        return None
    except Exception as e:
        print(f"Error connecting or logging in: {e}")
        return None

def list_emails(mailbox):
    
    try:
        response, message_list, octets = mailbox.list()
        if response.startswith(b'+OK'):
            print(f"Number of messages: {len(message_list)}")
            return message_list
        else:
            print(f"Couldn't list messages: status {response}")
            return None
    except Exception as e:
        print(f"Error listing emails: {e}")
        return None

def retrieve_email(mailbox, message_number):
    
    try:
        
        response, message_lines, octets = mailbox.retr(message_number)
        if response.startswith(b'+OK'):
            return message_lines
        else:
            print(f"Couldn't retrieve message {message_number}: status {response}")
            return None
    except Exception as e:
        print(f"Error retrieving email {message_number}: {e}")
        return None

def delete_email(mailbox, message_number):
    
    try:
        response = mailbox.dele(message_number)
        if response.startswith(b'+OK'):
            print(f"Marked message {message_number} for deletion.")
            return True
        else:
            print(f"Couldn't mark message {message_number} for deletion: status {response}")
            return False
    except Exception as e:
        print(f"Error marking email {message_number} for deletion: {e}")
        return False

def disconnect_from_pop_server(mailbox):
    
    try:
        mailbox.quit()
        print("Disconnected from POP server.")
    except Exception as e:
        print(f"Error disconnecting: {e}")

if __name__ == "__main__":
    POP_HOST = "pop.example.com"  # e.g., "pop.gmail.com"
    POP_PORT = 995  # e.g., 995 for SSL
    POP_USERNAME = "your_username"
    POP_PASSWORD = "your_password"

    pop_mailbox = connect_to_pop_server(POP_HOST, POP_PORT, POP_USERNAME, POP_PASSWORD)

    if pop_mailbox:
        messages = list_emails(pop_mailbox)

        if messages:
            first_message_number = int(messages[0].split()[0])
            email_content = retrieve_email(pop_mailbox, first_message_number)
            if email_content:
                print("\n--- First Email Content ---")
                print("\n".join(line.decode('utf-8', errors='ignore') for line in email_content))
                print("---------------------------\n")

            # delete_email(pop_mailbox, first_message_number)

        disconnect_from_pop_server(pop_mailbox)
