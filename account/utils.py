
from django.core.mail import send_mail

from network_api._celery import app


@app.task
def send_activation_code(email, activation_code):

    message = f"""
    Thank you for signing up.
    Please, activate your account.
    Activation link: 
    http://127.0.0.1:3000/api/v1/account/activate/{activation_code}"""
    send_mail(
        'Activate your account',
        message,
        'jannetsayakbaeva@gmail.com',
        [email, ],
        fail_silently=False
    )

@app.task
def send_activation_mail(email, activation_code):
    activation_url = f'http://localhost:3000/api/v1/account/activate/{activation_code}'
    message = f"""
    Use this code to reset {activation_code}
"""

    send_mail('Network password reset', message, 'admin@admin.com', [email, ], fail_silently=False, )