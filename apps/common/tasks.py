from django.core.mail import EmailMessage
from django.conf import settings


def mail_sender(user, message, attachment=None):
    mail = EmailMessage(f'{user.username} recover access request', message, settings.EMAIL_HOST_USER,
                        [user.email])
    if attachment:
        mail.attach_file(attachment)
    mail.send()
