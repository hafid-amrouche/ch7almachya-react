import shutil
import re
from geopy.geocoders import Nominatim
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from ch7almachya.settings import EMAIL_HOST_USER
from django.utils.translation import gettext as _



from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse


def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents have been successfully deleted.")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_valid_email(email):
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(email_regex, email))

def get_location(longitude, latitude):
    geolocator = Nominatim(user_agent="ch7al-machya")
    location = geolocator.reverse((latitude, longitude))
    return location.address


def send_email(email, title, message, logo):
    mail_subjet = _('Message from ch7al machya')
    html_message = render_to_string(f'general/email.html', {
        'message' : message,
        'logo': logo,
        'title' : title,
    })
    plain_message = strip_tags(html_message)
    to_email = email
    email_message = EmailMultiAlternatives(subject=mail_subjet, body=plain_message, from_email=EMAIL_HOST_USER, to=[to_email])
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()