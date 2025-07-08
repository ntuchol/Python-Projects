import poplib
import ssl

def connect_to_pop_server(host, port, username, password, use_ssl=True):
    """
    Connects to a POP server and logs in.

    Args:
        host (str): The POP server hostname or IP address.
        port (int): The POP server port (e.g., 995 for SSL, 110 for non-SSL).
        username (str): The username for the POP account.
        password (str): The password for the POP account.
        use_ssl (bool, optional): Whether to use SSL. Defaults to True.

    Returns:
        poplib.POP3_SSL or poplib.POP3: The POP connection object, or None if connection failed.
    """
    try:
        if use_ssl:
            # Create a default SSL context for security.
            # Consider using CERT_REQUIRED and checking the hostname for added security.
            context = ssl.create_default_context()
            # Connect to the server using SSL.
            mailbox = poplib.POP3_SSL(host, port, context=context)
            print("Connecting to POP3 server using SSL.")
        else:
            # Connect to the server without SSL.
            mailbox = poplib.POP3(host, port)
            print("Connecting to POP3 server.")

        # Log in to the server with username and password.
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
    """
    Lists the emails on the POP server.

    Args:
        mailbox (poplib.POP3_SSL or poplib.POP3): The connected POP connection object.

    Returns:
        list: A list of message information (e.g., message number and size), or None if unable to list messages.
    """
    try:
        # Get a list of messages.
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
    """
    Retrieves a specific email from the server.

    Args:
        mailbox (poplib.POP3_SSL or poplib.POP3): The connected POP connection object.
        message_number (int): The number of the email to retrieve.

    Returns:
        list: A list of lines representing the email message, or None if retrieval failed.
    """
    try:
        # Retrieve the message.
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
    """
    Marks an email for deletion on the server.

    Args:
        mailbox (poplib.POP3_SSL or poplib.POP3): The connected POP connection object.
        message_number (int): The number of the email to delete.

    Returns:
        bool: True if marked for deletion, False otherwise.
    """
    try:
        # Mark the message for deletion.
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
    """
    Disconnects from the POP server.

    Args:
        mailbox (poplib.POP3_SSL or poplib.POP3): The connected POP connection object.
    """
    try:
        # Quit the session, committing changes and unlocking the mailbox.
        mailbox.quit()
        print("Disconnected from POP server.")
    except Exception as e:
        print(f"Error disconnecting: {e}")

if __name__ == "__main__":
    # Replace with your POP server details and credentials
    POP_HOST = "pop.example.com"  # e.g., "pop.gmail.com"
    POP_PORT = 995  # e.g., 995 for SSL
    POP_USERNAME = "your_username"
    POP_PASSWORD = "your_password"

    # Connect to the POP server.
    pop_mailbox = connect_to_pop_server(POP_HOST, POP_PORT, POP_USERNAME, POP_PASSWORD)

    if pop_mailbox:
        # List available emails.
        messages = list_emails(pop_mailbox)

        if messages:
            # Example: Retrieve and print the first email.
            first_message_number = int(messages[0].split()[0])
            email_content = retrieve_email(pop_mailbox, first_message_number)
            if email_content:
                print("\n--- First Email Content ---")
                # Join the lines and decode for readable content.
                print("\n".join(line.decode('utf-8', errors='ignore') for line in email_content))
                print("---------------------------\n")

            # Example: Delete the first email (use with caution).
            # delete_email(pop_mailbox, first_message_number)

        # Disconnect from the server.
        disconnect_from_pop_server(pop_mailbox)