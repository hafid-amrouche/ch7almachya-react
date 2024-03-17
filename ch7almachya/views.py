from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import time, json
from user.models import User
from user.serializers import UserSerializerWithToken
from others.models import State, Report, Ad, ContactUs
from others.serializers import StateSerializer, AdSerializer
from article.serializers import ColorSerializer, DocumentSerializer, GearBoxSerializer, FuelSerializer, OptionSerializer, CategoryBrowserSerializer, ArticleHomeSerializer, BrandBrowserSerializer
from article.models import Document, GearBox, Fuel, Option, Color, Category, Article, Brand
from PIL import Image 
from .settings import BASE_DIR
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from ch7almachya.settings import EMAIL_HOST_USER
from django.shortcuts import redirect, render
from rest_framework.response import Response
from django.db.models import Subquery
from django.utils.translation import gettext as _
from .dictionary.ar import dictionary_ar
from .dictionary.fr import dictionary_fr
from .dictionary.en import dictionary_en
from functions import is_valid_email


from django.conf import settings
from django.utils.translation import check_for_language

@api_view(['GET'])
def home(request):
    serialized_data = []
    for category in Category.objects.all():
        serialized_data.append({
            'id' : category.id,
            'icon' : category.icon.url if category.icon else '',
            'name' : category.name,
            'order' : category.order,
            'articles' : ArticleHomeSerializer(Article.objects.filter(category=category)[:12] , many=True).data
        })

    return Response(serialized_data)

@api_view(['GET'])
def get_ads(request):
    ads=AdSerializer(Ad.objects.filter(ad_type='swiper'), many=True).data
    staticAd = AdSerializer(Ad.objects.get(ad_type='static')).data
    return Response([ads, staticAd])

def checkUsername(request):
    username = request.GET.get('username').strip().lower()
    users_exist = User.objects.filter(username=username).exists()
    return JsonResponse([not users_exist, username], safe=False)

def parameters(request, lang=None):
    ColorSerializer, DocumentSerializer, GearBoxSerializer, FuelSerializer, OptionSerializer
    lang = lang if lang else request.LANGUAGE_CODE 
    name_lang = 'name_{}'.format(lang)
    dictionary = dictionary_en
    if lang == 'fr' :
        dictionary = dictionary_fr
    elif lang == 'ar':
        dictionary = dictionary_ar
    browser_data = {
        'language' : lang,
        'states' :  StateSerializer(State.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'brands' : BrandBrowserSerializer(Brand.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'categories' : CategoryBrowserSerializer(Category.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'colors' :  ColorSerializer(Color.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'documents' : DocumentSerializer(Document.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'gear_boxs' : GearBoxSerializer(GearBox.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'fuels' : FuelSerializer(Fuel.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'options' : OptionSerializer(Option.objects.all(), many=True, context={'name_lang' : name_lang}).data,
        'dictionary' : dictionary
    }
    return JsonResponse(browser_data, safe=True)


def setLanguage(request):
    if request.method == "POST":
        lang_code = request.POST.get("language")
        response = parameters(request, lang_code)
        if lang_code and check_for_language(lang_code):
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME,
                lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
                secure=settings.LANGUAGE_COOKIE_SECURE,
                httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
                samesite=settings.LANGUAGE_COOKIE_SAMESITE,
            )
        return response

def send_verfication_token(request):
    email_or_username = request.GET.get('email').strip()
    if not email_or_username:
        return JsonResponse({'detail' : _('No user exists with that email or username')}, status=400)
    
    user = User.objects.filter(Q(email__iexact = email_or_username) | Q(username__iexact = email_or_username))
    user = user.first() if user.exists() else None
    if user:
        print(user)
        email = user.email
        current_site = get_current_site(request)
        mail_subjet = 'Reset Password'
        message = render_to_string(f'general/reset_password_validation_email_{request.LANGUAGE_CODE}.html', {
        'email' : email,
        'user' : user,
        'domain' : current_site,
        'uid' : urlsafe_base64_encode(force_bytes(user.id)),
        'token' : default_token_generator.make_token(user)
        })
        to_email = email
        email_message = EmailMessage(subject=mail_subjet, body=message, from_email=EMAIL_HOST_USER, to=[to_email])
        email_message.send()
        return JsonResponse({'detail' : _('We have sent an email with the verification link to the email of "{}"').format(email_or_username)}, status=200)
    else:
        return JsonResponse({'detail' :  _('No user exists with that email or username')}, status=400)
  
@api_view(['POST'])
def reset_password_validation(request):
  password = request.POST.get('password')
  confirm_password = request.POST.get('confirm_password')
  if len(password)< 8 or password != confirm_password:
    return JsonResponse('Invalid passwords', safe=False, status=400)
  email = request.POST.get('email')
  uidb64 = request.POST.get('uidb64')
  token = request.POST.get('token')
  try:
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(id=uid, email__iexact = email)

  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None

  if user and default_token_generator.check_token(user, token):
    user.extention.email_verified = True
    user.extention.save()
    user.set_password(password)
    user.save()
    return Response({'detail' : _('Password reset successfully'), 'user_data' : UserSerializerWithToken(user).data})
  else:
    return JsonResponse({'detail' : _('Error')}, safe=False, status=400)
  
  

def serve_resized_image(request, width):
    image_path = request.GET.get('path')
    image = Image.open(BASE_DIR / image_path)
    image.thumbnail((width, width))
    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG")
    return response

@api_view(['POST'])
def report(request):
    type = request.POST.get('type')
    query_dict = {}
    if request.user.is_authenticated:
        query_dict={
            'reporter' : request.user,
        }
    else:
        return JsonResponse({'detail' : _('You have to be logged to report this {}').format(_(type))}, status=400)
        
    if type == 'Comment':
        query_dict.update({
            'comment_id' : request.POST.get('comment_id') 
        })

    elif type == 'Article':
        query_dict.update({
            'article_id' : request.POST.get('article_id') 
        })
    elif type == 'User':
        query_dict.update({
            'user' : User.objects.get(username = request.POST.get('user_username') )
        })
    
    print(query_dict)
    report, cond = Report.objects.get_or_create(**query_dict)

    if cond:
        note = request.POST.get('note').strip()
        if note:
            report.note = note
            report.save()
    
    else:
        return JsonResponse({'detail' : _('You have already repoted this {}').format(_(type))}, status=400)
    return JsonResponse({'detail' : _('Your report was submited successfully')}, status=200)

def contact_us(request):
    try:
        email = request.POST.get('email').strip()
        name = request.POST.get('name').strip()
        message = request.POST.get('message').strip()
        if not is_valid_email(email) or not name or not message:
            raise
        ContactUs.objects.create(
            email=email,
            name=name,
            message=message
        )
        return JsonResponse(_('Your message was sent successfully'), safe=False)
    except:
        return JsonResponse({'detail':_('Your message was not sent, please make sure that all field are filled and your email is corret.')}, status=404, safe=False)
