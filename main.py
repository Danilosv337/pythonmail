from dotenv import dotenv_values
import smtplib
from email.message import EmailMessage

env = dotenv_values('.env')


class Email:
    def __init__(self):
        self.email_send: str = env['email_send']
        self.email_destiny: str = env['email_destiny']
        self.password: str = env['email_password']

    def send_email(self, assunto: str, mensagem: str) -> None:
        msg = EmailMessage()
        msg['Subject'] = assunto
        msg['From'] = self.email_send
        msg['To'] = self.email_destiny
        msg.set_content(mensagem)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_send, self.password)
            smtp.send_message(msg)


if __name__ == '__main__':
    email = Email()
    email.send_email('teste', 'testando')
