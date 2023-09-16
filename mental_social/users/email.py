from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail

def send_email(subject, message, from_email, recipient_list):
    html_content = message
    msg = EmailMultiAlternatives(subject, '', from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
   

def send_register_email(user):
    subject = "Welcome to Our Website"
    from_email = "commercedjango@gmail.com'"
    html_message = render_to_string('register_email.html', {'user': user})
    recipient_list = [user.email]
    email_message = EmailMultiAlternatives(subject, '', from_email, recipient_list)
    email_message.attach_alternative(html_message, "text/html")
    try:
       # send_mail(subject, message, from_email, recipient_list)
            email_message.send()

    except Exception:
        print("Unable to send") 

def send_dr_email(user):
    subject = "Welcome to Our Website"
    from_email = "commercedjango@gmail.com'"
    html_message = render_to_string('dr_email.html', {'user': user})
    recipient_list = [user.email]
    email_message = EmailMultiAlternatives(subject, '', from_email, recipient_list)
    email_message.attach_alternative(html_message, "text/html")
    try:
       # send_mail(subject, message, from_email, recipient_list)
            email_message.send()

    except Exception:
        print("Unable to send") 