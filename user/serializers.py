from rest_framework import serializers
from user.models import User, UserSuggestion, Profile, UserExtention, Page, Location
from rest_framework_simplejwt.tokens import RefreshToken
from others.serializers import StateSerializer
from functions import get_media_url

class LocationSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField(read_only=True)
    def get_state(self, obj):
        return StateSerializer(obj.state, many=False).data

    class Meta:
        model = Location
        fields = ['state', 'city', 'address', 'location_public']

class UserSerializerWithToken(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'token', 'refresh', 'profile','page' ,'extention', 'location']

    token = serializers.SerializerMethodField(read_only=True)
    def get_token(self, obj):
        access_token = str(RefreshToken.for_user(obj).access_token)
        return access_token
    
    refresh = serializers.SerializerMethodField(read_only=True)
    def get_refresh(self, obj):
        refresh_token = str(RefreshToken.for_user(obj))
        return refresh_token

    location = serializers.SerializerMethodField(read_only=True)
    def get_location(self, obj):
        return LocationSerializer(obj.location).data
    
    profile = serializers.SerializerMethodField(read_only=True)
    def get_profile(self, obj):
        return ProfileSerializerSettingsProfile(obj.profile, many=False).data if not obj.extention.is_page else None
    
    page = serializers.SerializerMethodField(read_only=True)
    def get_page(self, obj):
        return PageSerializerSettingsProfile(obj.page, many=False).data if obj.extention.is_page else None

    extention = serializers.SerializerMethodField(read_only=True)
    def get_extention(self, obj):
        return UserExtentionSerializerSettingsProfile(obj.extention, many=False).data
    
    
class UserExtentionSerializerSettingsProfile(serializers.ModelSerializer):
    class Meta:
        model = UserExtention
        fields = ['image', 'image_150', 'bio','email_verified', 'is_page', 'other_socials', 'linkedin', 'twitter', 'youtube', 'tiktok', 'instagram', 'facebook', 'email_public']
    
    image = serializers.SerializerMethodField(read_only=True)
    def get_image(self, obj):
        return get_media_url(obj.image)
    
    image_150 = serializers.SerializerMethodField(read_only=True)
    def get_image_150(self, obj):
        return get_media_url(obj.image)
    
class AcountInfoUserExtentionSerializerSettingsProfile(serializers.ModelSerializer):
    class Meta:
        model = UserExtention
        fields = ['bio', 'is_page', 'email_public']

class ProfileSerializerSettingsProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['is_male', 'birth_day', 'birth_day_public', 'first_name', 'last_name']
    
    first_name = serializers.SerializerMethodField(read_only=True)
    def get_first_name(self, obj):
        return obj.user.first_name
    
    last_name = serializers.SerializerMethodField(read_only=True)
    def get_last_name(self, obj):
        return obj.user.last_name

class PageSerializerSettingsProfile(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['website', 'name', 'is_verified']


class ProfilePageSerializer(serializers.ModelSerializer):    
    is_admin = serializers.SerializerMethodField(read_only=True)
    def get_is_admin(self, obj):
        return obj.is_staff
    
    image = serializers.SerializerMethodField(read_only=True)
    def get_image(self, obj):
        return get_media_url(obj.extention.image)
    
    bio = serializers.SerializerMethodField(read_only=True)
    def get_bio(self, obj):
        return obj.extention.bio
    
    is_page = serializers.SerializerMethodField(read_only=True)
    def get_is_page(self, obj):
        return obj.extention.is_page

    followers_count = serializers.SerializerMethodField(read_only=True)
    def get_followers_count(self, obj):
        return obj.followers.followers_list.all().count()

    articles_count = serializers.SerializerMethodField(read_only=True)
    def get_articles_count(self, obj):
        return obj.articles.count()
    
    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return {'text' : obj.page.name, 'is_verified': obj.page.is_verified } if obj.extention.is_page else obj.get_full_name()
    
    is_follower = serializers.SerializerMethodField(read_only=True)
    def get_is_follower(self, obj):
        user = self.context.get('user')
        print(user)
        return user in obj.followers.followers_list.all()
    
    
    class Meta:
        model = User
        fields = ['name', 'is_admin', 'username', 'image', 'bio', 'followers', 'articles_count', 'is_follower', 'followers_count', 'id', 'is_page']


class UserCard(serializers.ModelSerializer):
    # first_name, last_name ==> name

    image_150 = serializers.SerializerMethodField(read_only=True)
    def get_image_150(self, obj):
        return get_media_url(obj.extention.image_150)
    
    
    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return obj.page.name if obj.extention.is_page else obj.get_full_name() 
    
    class Meta:
        model = User
        fields = ['id', 'username', 'name' ,'image_150']

class UserSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSuggestion
        fields = ['id', 'text']

class UsernameSuggestionSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField(read_only=True)
    def get_text(self, obj):
        return '@' + obj.username
    class Meta:
        model = User
        fields = ['id', 'text']


##################################################################
####
# class UserSerializer(serializers.ModelSerializer):
#     is_admin = serializers.SerializerMethodField(read_only=True)
#     image = serializers.SerializerMethodField(read_only=True)
#     image_150 = serializers.SerializerMethodField(read_only=True)
#     bio = serializers.SerializerMethodField(read_only=True)
#     state = serializers.SerializerMethodField(read_only=True)
#     city = serializers.SerializerMethodField(read_only=True)


#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_admin', 'image', 'image_150', 'bio', 'state', 'city']

#     def get_is_admin(self, obj):
#         return obj.is_staff
    
#     def get_image(self, obj):
#         return obj.profile.image
    
#     def get_image_150(self, obj):
#         return obj.profile.image_150

#     def get_state(self, obj):
#         return StateSerializer(obj.profile.state, many=False).data
    
#     def get_bio(self, obj):
#         return obj.profile.bio
    
#     def get_city(self, obj):
#         return obj.profile.city
        