import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import testGpt as gpt

# Set up credentials (make sure to replace 'credentials.json' with your actual credentials file)
creds = Credentials.from_authorized_user_file('token.json')
service = build('gmail', 'v1', credentials=creds)

def list_unread_emails():
    # Get unread emails
    unread_msgs = service.users().messages().list(userId='me',labelIds=['INBOX'], q='is:unread').execute()
    print(f'unread msgs: {unread_msgs}')
    
    if 'messages' in unread_msgs:
        for msg in unread_msgs['messages']:
            email = service.users().messages().get(userId='me', id=msg['id']).execute()
            msg_data = email['payload']['headers']
            mensagem = email['snippet']
            print(mensagem)
            for item in msg_data:
                if item['name'] == 'Return-Path':
                    subject = item['value']
                    print(f"Subject: {subject}")
                    

def send_email(to, subject, message_text):
    message = create_message(to, 'me', subject, message_text)
    send_message(message)

def create_message(to, sender, subject, message_text):
    message = f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{message_text}"
    b64_bytes = base64.urlsafe_b64encode(message.encode('utf-8'))
    b64_string = b64_bytes.decode('utf-8')
    return {'raw': b64_string}

def send_message(message):
    try:
        message = service.users().messages().send(userId='me', body=message).execute()
        print('Message Id: %s' % message['id'])
    except Exception as e:
        print('An error occurred: %s' % e)

# Example usage:
if __name__ == "__main__":
    # List unread emails
    print("Unread Emails:")
    list_unread_emails()

    # Send email
    #send_email('julia.odonnell95@gmail.com ', '❤️', 'Te amo meu amor! ❤️ </br> This is a test email sent via Gmail API.')
