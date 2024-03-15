from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from others.models import State
from user.models import Profile, User, Page
from user.serializers import UserSerializerWithToken, UserExtentionSerializerSettingsProfile, PageSerializerSettingsProfile, ProfileSerializerSettingsProfile, LocationSerializer, AcountInfoUserExtentionSerializerSettingsProfile
from PIL import Image
from ch7almachya.settings import BASE_DIR
import time, os, json
from ch7almachya.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password, check_password
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from ch7almachya.settings import EMAIL_HOST_USER
from django.utils.translation import gettext
from PIL import Image
from user.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from functions import is_valid_email 
from django.utils.translation import gettext as _



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
  try :
      time.sleep(1)
      user = request.user
      profile = Profile.objects.get(user=user)
      data = request.data
      first_name = data['first_name'].strip()
      last_name = data['last_name'].strip()
      birth_day = data['birth_day']
      birth_day_public= data['birth_day_public'] == 'true'
      is_male= data['is_male'] == 'true'

      if first_name == '' :
          message = {'detail': 'First name cannot be empty'}
          return JsonResponse(message, status=400)
      
      elif last_name == '' :
          message = {'detail': 'Last name cannot be empty'}
          return JsonResponse(message, status=400)
      
      user.first_name = first_name
      user.last_name = last_name
      profile.birth_day = birth_day
      profile.birth_day_public = birth_day_public
      profile.is_male = is_male
      user.save()
      profile.save()
      userData = UserSerializerWithToken(user, many=False).data
      return Response(userData)
  except :
      message = {'detail': _('Your profile information was not updated')}
      return JsonResponse(message, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_location(request):
  try :
      time.sleep(1)
      data = request.data
      user = request.user
      location = user.location
      location.city = data.get('city')
      location.street = data.get('street')
      location.state = State.objects.get(code=data.get('state'))
      location.location_public= data['location_public'] == 'true'
      location.save()
      location_serialized = LocationSerializer(location).data
      return Response(location_serialized)
  except :
      message = {'detail': _('Your profile location was not updated')}
      return JsonResponse(message, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_page(request):
    try :
        time.sleep(1)
        user = request.user
        page = Page.objects.get(user=user)
        data = request.data
        website = data.get('website').strip()
        name = data.get('name').strip()

        if name == '' :
            message = {'detail': _('Page name cannot be empty')}
            return JsonResponse(message, status=400)
        
        page.name = name
        page.website = website
        page.save()

        serialized_data = {
          'page' : data
        }
        return JsonResponse(serialized_data, status=200)
    except :
        message = {'detail': _('Your page information was not updated')}
        return JsonResponse(message, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_account(request):
  try :
      time.sleep(1)
      user = request.user
      user_extention = user.extention
      data = request.data
      bio = data['bio'].strip()
      email_public = data['email_public'] == 'true'
      is_page= data['is_page'] == 'true'
      prev_is_page = user_extention.is_page
      user_extention.bio = bio
      user_extention.email_public = email_public
      user_extention.is_page = is_page
      user.save()
     
      response = {}
      if is_page != prev_is_page:
        if is_page:
            page = Page.objects.get_or_create(user=user)[0]
            page.name = f'Page-{user.id}'
            page.save()
            response['page'] = PageSerializerSettingsProfile(page).data
            response['profile'] = None
            user_extention.image = '/static/others/page_icon.png'
            user_extention.image_150 = '/static/others/page_icon_150.png'

        else:
            try:
              user.page.delete() 
            except:
              pass
            user_extention.image = '/static/others/user.png'
            user_extention.image_150 = '/static/others/user_150.png'
            response['profile'] = ProfileSerializerSettingsProfile(user.profile).data
            response['page'] = None
        
      user_extention.save()
      response = AcountInfoUserExtentionSerializerSettingsProfile(user_extention).data
      return Response(response)
  except :
      message = {'detail': _('Your account information was not updated')}
      return JsonResponse(message, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_socials(request):
    try :
        time.sleep(1)
        user = request.user
        user_extention = user.extention
        data = request.data
        facebook = data.get('facebook')
        instagram = data.get('instagram')
        tiktok = data.get('tiktok')
        twitter = data.get('twitter')
        youtube = data.get('youtube')
        linkedin = data.get('linkedin')
        user_extention.facebook = facebook 
        user_extention.instagram = instagram 
        user_extention.tiktok = tiktok 
        user_extention.twitter = twitter 
        user_extention.youtube = youtube
        user_extention.linkedin = linkedin
        user_extention.save()
        data = {
           'facebook' : facebook,
           'instagram' : instagram,
           'tiktok' : tiktok,
           'twitter' : twitter,
           'youtube' : youtube,
           'linkedin' : linkedin
        }
        return JsonResponse(data, status=200)
    except :
        message = {'detail': _('Your socials were not updated')}
        return JsonResponse(message, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_image(request):
    time.sleep(1)
    user = request.user
    user_extention = user.extention
    image = Image.open(request.FILES.get('image'))
    format = image.format
    image = image.convert('RGB')
    if image.width >1080 or image.height > 1080 :
        image.thumbnail((1080, 1080))
    try:
        url_1 = f"media/users/{ user.id }/image.jpeg"
        url_2 = f"media/users/{ user.id }/image_150.jpeg"

        image.save(
            BASE_DIR / url_1,
            format,
            optimize=True,
            )

        image.thumbnail((150, 150))
        image.save(
            BASE_DIR / url_2,
            format,
            optimize=True,
            )
        user_extention.image = '/' + url_1
        user_extention.image_150 = '/' + url_2
        user_extention.image_update_count += 1
        user_extention.save()
        return JsonResponse(
            {'image' : '/' + url_1 + f'?v={user_extention.image_update_count}.0.0',
            'image_150' : '/' + url_2 + f'?v={user_extention.image_update_count}.0.0'},
            safe=True)
    except Exception as e:
        print(e)
        message = {'detail': _('Your profile picture was not updated')}
        return JsonResponse(message, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def remove_profile_image(request):
    time.sleep(1)
    user = request.user
    extention = user.extention
    try:
        url_1, url_2 = ["/static/others/page_icon.png", "/static/others/page_icon_150.png"] if user.extention.is_page else ["/static/others/user.png", "/static/others/user_150.png"]
        extention.image = url_1
        extention.image_150 = url_2
        extention.save()
        os.remove(BASE_DIR / f"media/users/{ user.id }/image.jpeg")
        os.remove(BASE_DIR / f"media/users/{ user.id }/image_150.jpeg")
        return JsonResponse({'image' : url_1, 'image_150' : url_2}, safe=True)
    except Exception as e:
        message = {'detail': _('Your profile picture was not deleted')}
        return JsonResponse(message, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_email(request):
  email = request.POST.get('email').lower().strip()
  email_used = User.objects.filter(email = email, extention__email_verified = True).exists()
  if email_used:
    message = {"detail" : _('This email "{}" is already used, please use another email').format(email)}
    return JsonResponse(message, status=400)
  
  elif is_valid_email(email):
    request.user.email = email
    request.user.save()
    message = {
                "detail" : _('Your email "{}" is set successfully').format(email),
                "email" : email
               }
    return JsonResponse(message, status=200)
  else:
    message = {"detail" : _('This email "{}" has a wrong format').format(email)}
    return JsonResponse(message, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_email(request):
    email = request.POST.get('email').lower().strip()
    email_used = User.objects.filter(email = email, extention__email_verified = True).exists()
    if email_used :
      message = {"detail" : _('This email "{}" is used, please use a another email').format(email)}
      return JsonResponse(message, status=400)
    elif email == request.user.email :
      message = {"detail" : _('New email is the same as the current email')}
      return JsonResponse(message, status=400)
    elif is_valid_email(email):
      prev_email = request.user.email
      request.user.email = email
      request.user.save()
      request.user.extention.email_verified = False
      request.user.extention.save()
      message = {
                  "detail" : _('Your email is updated successfully from "{}" to "{}"').format(prev_email, email),
                  "email" : email
      }
      return JsonResponse(message, status=200)
    else:
      message = {"detail" : f'This email "{email}" has a wrong format'}
      return JsonResponse(message, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def confirm_email(request):
  if request.user.extention.email_verified == False :
    mail_subjet = 'Account activation'
    message = render_to_string(f'settings/activation_link_sent_{request.LANGUAGE_CODE}.html', {
    'user' : request.user,
    'domain' : get_current_site(request),
    'uid' : urlsafe_base64_encode(force_bytes(request.user.id)),
    'token' : default_token_generator.make_token(request.user)
    })
    to_email = request.user.email
    send_email = EmailMessage(subject=mail_subjet, body=message, from_email=EMAIL_HOST_USER, to=[to_email])
    try :
      send_email.send()
      message= {'detail' : _('We sent the activation link to your email "{}"').format(to_email)}
      return JsonResponse(message, status=200)
    except:
      message = {'detail' : _('Email verification failed, please try again. If this problem still occurs please contact our customer service')}
      return JsonResponse(message, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_email(request):
    request.user.email = ''
    request.user.extention.email_verified = False
    request.user.save()
    request.user.extention.save()
    message = {'detail' : _('Email was deleted successfully')}
    return JsonResponse(message, status=200)

  
def confirm_email_activation(request, uidb64, token):
  try:
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User._default_manager.get(pk=uid)

  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None

  if user and default_token_generator.check_token(user, token):
    user.extention.email_verified = True
    user.extention.save()
    return redirect(f'http://localhost:3000/settings/manage-email/?email-verified=true&email={user.email}')
  else:
    return redirect('http://localhost:3000/settings/manage-email/?email-verified=false')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    time.sleep(1)
    current_password = request.POST.get('current_password')
    new_password = request.POST.get('new_password')
    confirm_password = request.POST.get('confirm_password')

    if not check_password(current_password, request.user.password):
      message = {'detail': _('Current password is wrong')}
      return JsonResponse(message, status=400)
    
    if new_password == '':
        message = {'detail': _('New password cannot be empty')}
        return JsonResponse(message, status=400)
    
    elif len(new_password) < 8 :
        message = {'detail': _('New password should have at least 8 characters')}
        return JsonResponse(message, status=400)
    
    elif new_password != confirm_password:
        message = {'detail': _('Passwords Do not match')}
        return JsonResponse(message, status=400)
    else:
        request.user.set_password(new_password)
        request.user.save()
        message = {'detail': _('Your password have been updated successfully')}
        return JsonResponse(message, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_account(request):
  time.sleep(1)
  try:
    request.user.delete()
    message = {'detail': _('Your account was deleted successfully')}
    return JsonResponse(message, status=200)
  except:
    message = {'detail': _('The account you want to delete was not found')}
    return JsonResponse(message, status=400)
  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_username(request):
  time.sleep(1)
  try:
    user = request.user
    new_username = request.POST.get('username').lower().strip()
    if user:
      if new_username =='' :
          message = {'detail': _('Username field cannot be empty')}
          return JsonResponse(message, status=400)
      
      elif User.objects.filter(username__iexact=new_username) :
          message = {'detail': _('This username {} is taken').format(new_username)}
          return JsonResponse(message, status=400)
      
      user.username = new_username
      user.save()
      return JsonResponse(new_username, safe=False, status=200)
    else:
      raise
  except:
    message={'detail' : 'Try a diffrent username'}
    return JsonResponse(message, status=400)