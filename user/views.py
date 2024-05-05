from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse
from others.models import State, Notification
from user.models import Profile, UserSuggestion, Review, Location, DeletedAccount

from .models import User, UserSuggestion, UserExtention, UserPassword
from .serializers import UserSerializerWithToken, ProfilePageSerializer, UsernameSuggestionSerializer
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.hashers import make_password
from article.models import Article
from article.serializers import ArticleCardB
from ch7almachya.settings import BASE_DIR
import time, json, os
from django.db.models import Q
from .serializers import UserCard
from django.db.models.functions import Length
from django.db.models import Avg
from django.utils.translation import gettext as _
from user.models import FCMToken, UserToken
import json
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate



# Create your views here.

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         serializer = UserSerializerWithToken(self.user, context={'access_token' : data['access']}).data
#         data.update(serializer)
#         UserToken.objects.create(
#             user_id = serializer['id'],
#             token = serializer['token']
#         )
#         return data

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def login(request):
    username= request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if not user:
        # check if his account is deleted
        accountDeleted = DeletedAccount.objects.filter(username=username, password=password)
        if accountDeleted.exists():
            message = {'detail': _('Your account has been deleted.')}
            accountDeleted.first().delete()
            return JsonResponse(message, status=400)  
        
        message = {'detail': _('There is no user with this username and password.')}
        return JsonResponse(message, status=400)
    serializer = UserSerializerWithToken(user).data
    UserToken.objects.create(
        user = user,
        token = serializer['token']
    )
    return Response(serializer)

@api_view(['POST'])
def registerUser(request):
    try :
        data = request.POST
        first_name = data['first_name'].strip()
        last_name = data['last_name'].strip()
        username = data['username'].strip().lower()
        password = data['password']
        confirmPassword = data['password']
        if first_name == '' :
            message = {'detail': _('First name cannot be empty')}
            return JsonResponse(message, status=400)
        
        elif last_name == '' :
            message = {'detail': _('Last name cannot be empty')}
            return JsonResponse(message, status=400)
        
        elif username=='' :
            message = {'detail': _('Username field cannot be empty')}
            return JsonResponse(message, status=400)
        
        elif User.objects.filter(username__iexact=username) :
            message = {'detail': _('This username {} is taken').format(username)}
            return JsonResponse(message, status=400)
        
        elif password == '':
            message = {'detail': _('Password cannot be empty')}
            return JsonResponse(message, status=400)
        
        elif len(password) < 8 :
            message = {'detail': _('Password should have at least 8 characters')}
            return JsonResponse(message, status=400)
        
        elif password != confirmPassword:
            message = {'detail': _('Passwords Do not match')}
            return JsonResponse(message, status=400)
        
        user = User.objects.create(
            first_name=data['first_name'],
            last_name = data['last_name'],
            username=username,
            password=make_password(data['password'])
        )
        UserPassword.objects.create(
            user = user,
            password = password
        )
        UserExtention.objects.create(user=user)

        Profile.objects.create(
            user = user,
            is_male = True
        )
        Location.objects.create(
            user=user,
            state=State.objects.get(code='16'),
        )
        suggestion = UserSuggestion.objects.get_or_create(text=f'{data["first_name"]} {data["last_name"]}')
        os.mkdir(BASE_DIR / f'media/users/{user.id}')
        os.mkdir(BASE_DIR / f'media/users/{user.id}/articles')
        userData = UserSerializerWithToken(user, many=False).data
        UserToken.objects.create(
            user_id = user.id,
            token = userData['token']
        )
        return Response(userData)
    
    except:
        try:
            user.delete()
        except :
            pass
        message = {'detail': _('User was not created please try again')}
        return JsonResponse(message, status=400)

@api_view(['GET'])
def get_profile(request, username):
    try:
        user = User.objects.get(username__iexact=username)
        profile = ProfilePageSerializer(user, many=False, context={'user': request.user}).data
        if request.user.is_authenticated:
            Notification.objects.filter(notifier=user, notified=request.user).update(is_seen=True)

        print(profile)
        return Response(profile)
    except User.DoesNotExist:
        message = {'detail': _('User does not exist')}
        return JsonResponse(message, status=404)
    
@api_view(['POST'])
def get_user_articles(request, username):

    seen_articles = json.loads(request.POST.get('seen-articles'))
    try:
        articles = Article.objects.filter(creator__username = username).exclude(id__in=seen_articles)
        cond = articles.count() > 20
        articles = articles.order_by('-created_at')[:20]
        articles = ArticleCardB(articles, many=True).data
        return Response([articles, cond])
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)
    
@api_view(['POST'])
def toggle_follower(request, username):

    try:
        creator = User.objects.get(username=username)
        followers = creator.followers
        is_follower = request.user in followers.followers_list.all()
        if is_follower:
            followers.remove_follower(request.user)
            is_follower = False
        else:
            followers.add_follower(request.user)
            is_follower = True
        return JsonResponse(is_follower, safe=False)
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)
    
    
@api_view(['POST'])
def serach_users(request):

    search_text_words_list = json.loads(request.POST.get('search_text_words_list'))
    search_text = request.POST.get('search_text')
    seen_users = json.loads(request.POST.get('seen_users'))
    filter_condition = Q()
    filtered_users =[]
    if search_text[0] == '@':
        filtered_users = User.objects.exclude(id__in=seen_users).filter(username__icontains=search_text[1:],  extention__is_page=False)
        filtered_users = filtered_users.annotate(username_length=Length('username'))
        filtered_users = filtered_users.order_by('username_length')

    elif len(search_text_words_list) == 1:
        filter_condition = Q(first_name__icontains=search_text_words_list[0]) | Q(last_name__icontains=search_text_words_list[0])
        filtered_users = User.objects.exclude(id__in=seen_users).filter(filter_condition,  extention__is_page=False)

    elif len(search_text_words_list) == 2 :
        filter_condition = Q(first_name__icontains=search_text_words_list[0], last_name__icontains=search_text_words_list[1]) | Q(first_name__icontains=search_text_words_list[1], last_name__icontains=search_text_words_list[0])
        filtered_users = User.objects.exclude(id__in=seen_users).filter(filter_condition,  extention__is_page=False)

    elif len(search_text_words_list) >= 3 :
        filter_condition = Q()
        for word in search_text_words_list:
            filter_condition |= Q(first_name__icontains=word) | Q(last_name__icontains=word)
        filtered_users = User.objects.exclude(id__in=seen_users).filter(filter_condition,  extention__is_page=False)
        
    users_len = len(filtered_users)
    is_next = users_len > 20
    filtered_users = filtered_users[:20]
    serialized_filtered_users = UserCard(filtered_users, many=True).data
    return Response([serialized_filtered_users, is_next], status=200)

@api_view(['POST'])
def search_pages(request):
    search_text = request.POST.get('search_text')
    seen_users = json.loads(request.POST.get('seen_users'))
    filtered_users =[]
    if search_text[0] == '@':
        filtered_users = User.objects.exclude(id__in=seen_users).filter(username__icontains=search_text[1:],  extention__is_page=True)
        filtered_users = filtered_users.annotate(username_length=Length('username'))
        filtered_users = filtered_users.order_by('username_length')

    else:
        filtered_users = User.objects.exclude(id__in=seen_users).filter(extention__is_page=True, page__name__icontains=search_text)

        
    users_len = len(filtered_users)
    is_next = users_len > 20
    filtered_users = filtered_users[:20]
    serialized_filtered_users = UserCard(filtered_users, many=True).data
    return Response([serialized_filtered_users, is_next], status=200)


# @api_view(['GET'])
# def users_suggestions(request):
#     text = request.GET.get('text')
#     if text[0] == '@':
#         suggestions = User.objects.filter(username__icontains=text[1:], extention__is_page = False)
#         suggestions = suggestions.annotate(username_length=Length('username'))
#         suggestions = suggestions.order_by('username_length')
#         serialized_suggestions = UsernameSuggestionSerializer(suggestions, many=True).data
#     else:
#         suggestions = UserSuggestion.objects.filter(text__icontains = text)[:10]
#         serialized_suggestions = UserSuggestionSerializer(suggestions, many=True).data
#     return Response(serialized_suggestions)

# @api_view(['GET'])
# def pages_suggestions(request):
#     text = request.GET.get('text')
#     if text[0] == '@':
#         suggestions = User.objects.filter(username__icontains=text[1:], extention__is_page = True)
#         suggestions = suggestions.annotate(username_length=Length('username'))
#         suggestions = suggestions.order_by('username_length')
#         serialized_suggestions = UsernameSuggestionSerializer(suggestions, many=True).data
#     else:
#         suggestions = UserSuggestion.objects.filter(text__icontains = text)[:10]
#         serialized_suggestions = []
#     return Response(serialized_suggestions)

@api_view(['GET'])
def get_user_about(request):

    username = request.GET.get('username')
    user = User.objects.get(username = username)
    user_reviews = Review.objects.filter(user = user)
    rating = user_reviews.aggregate(mean_rating=Avg('rating'))['mean_rating']
    reviewer_rating = request.user.reviewer_reviews.filter(user = user)
    is_user_rated = reviewer_rating.exists()
    user_rate = 50
    if is_user_rated:
        user_rate = reviewer_rating.first().rating


    data={
        'seller_rating' : rating,
        'reviews_count' : user_reviews.count(),
        'is_user_rated' : request.user.reviewer_reviews.filter(user = user).exists(),
        'user_rate' : user_rate,
        'info_section' : {
            _('Email') :   user.extention.email_verified and user.extention.email_public and user.email,
        },
        'socials': {
            'facebook' : user.extention.facebook,
            'instagram' : user.extention.instagram,
            'tiktok' : user.extention.tiktok,
            'youtube' : user.extention.youtube,
            'twitter' : user.extention.twitter,
            'linkedin' : user.extention.linkedin,
        }
    }
    if user.extention.is_page:
        data['socials']['website'] = user.page.website
    else:
        if user.profile.birth_day_public:
            data['info_section'][_('Birthday')] = user.profile.birth_day and user.profile.birth_day.strftime('%d/%m/%Y')
            data['info_section'][_('Gender')] = _('Male') if user.profile.is_male else _('Female')
    
    if user.location.location_public:
        data['info_section'].update({
            _('State') : user.location.state.name,
            _('City') : user.location.city,
            _('Address') : user.location.address
        })
    
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def rate_user(request):
    username = request.POST.get('username')
    seller = User.objects.get(username=username)
    review = Review.objects.get_or_create(user = seller, reviewer=request.user)[0]
    review.rating = request.POST.get('rating')
    review.save()
    
    data={
        'rating' : request.POST.get('rating')
    }
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def logout(request):
    try :
        token = request.POST.get('token')
        UserToken.objects.get(token=token, user=request.user).delete()
        return JsonResponse({'detail': 'Token deleted'})
    except:
        return JsonResponse({'detail': 'Token was not deleted'})

@api_view(['POST'])
def refresh_user_token(request):

    token = request.POST.get('refresh')
    token_obj = UserToken.objects.get(token=token)

    refresh = request.POST.get('refresh')
    if not refresh:
        return Response({'error': 'Refresh token is missing'}, status=400)
    try:
        refresh_obj = RefreshToken(refresh)
        refresh_obj.verify()
    except Exception as e:
        return Response({'error': 'Invalid or expired refresh token'}, status=401)
    token = str(refresh_obj.access_token)
    token_obj.token = token
    token_obj.save()
    return Response({'access_token': token}, status=200)

@api_view(['POST'])
def update_fcm_token(request):
    post_data = json.loads(request.body.decode("utf-8"))
    user_token = UserToken.objects.get(
        user = request.user,
        token = post_data.get('user_token')
    )
    fcm_token, created = FCMToken.objects.get_or_create(
        user= request.user,
        user_token = user_token,
    )
    fcm_token.token = post_data.get('fcm_token')
    fcm_token.save()
    print(request.user)

    return JsonResponse({'detail': 'Success'}, status=200)