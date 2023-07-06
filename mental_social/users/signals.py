from django.db.models.signals import post_save
from django.dispatch import receiver
from .email import send_email
from django.contrib.auth.models import User
from .models import Doctor

@receiver(post_save, sender=Doctor)
def send_post_published_notification(sender, instance, created, **kwargs):
    print('Signal handler function called')
    if instance.user.is_active:
        subject = f'Welcome dr {instance.user.first_name} '
        message =  f'Welcome dr {instance.user.first_name}, You have been verified by admin and now you can log in to our website! '
        from_email = "commercedjango@gmail.com"
        print(instance.user.email)
        recipient_list = [instance.user.email]
        send_email(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Doctor)
def set_user_is_active(sender, instance, created, **kwargs):
    if created:
        instance.user.is_active = False
        print("second called")
        instance.user.save()        