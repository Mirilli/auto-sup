import base64
import requests

def send_email(api_key, to, subject, message_text):
    url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    message = create_message(to, 'me', subject, message_text)
    response = requests.post(url, headers=headers, json=message)
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email. Error: {response.text}")

def create_message(to, sender, subject, message_text):
    message = {
        "raw": base64.urlsafe_b64encode(f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{message_text}".encode()).decode()
    }
    return message

# Example usage:
if __name__ == "__main__":
    api_key = "AIzaSyDKDqrbXpoXImI-AFOZ4vsRqgFw6NxCEoc"
    to = "joao.mirilli@gmail.com"
    subject = "Test Email"
    message_text = "This is a test email sent using the Gmail API with an API key."
    send_email(api_key, to, subject, message_text)
