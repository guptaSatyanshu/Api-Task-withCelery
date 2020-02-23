from celery import shared_task
from django.core.mail import send_mass_mail, send_mail
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Task is working!!',
              'The email is verified!',
              'support@satyanshugupta.com',
              [''])
