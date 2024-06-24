from rest_framework import serializers
from .models import Article, Document, GearBox, Fuel, Option, Brand, Color, Comment, SavedArticle, Like, Dislike, ArticleSuggestion, Image, Category
import json
from functions import get_media_url


class ArticleHomeSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    def get_url(self, obj):
        return obj.slug

    brand_name = serializers.SerializerMethodField(read_only=True)
    def get_brand_name(self, obj):
        return  obj.other_brand or obj.brand.name_en
    
    main_image = serializers.SerializerMethodField(read_only=True)
    def get_main_image(self, obj):
        try:
            main_image = obj.main_image and obj.main_image.url
            main_image = get_media_url(main_image)
        except:
            main_image =""
        return main_image
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'year', 'main_image', 'price', 'offered_price', 'views', 'likes_count', 'brand_name', 'url', 'is_used']


class ArticlePageSerializerInfo(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField(read_only=True)
    def get_state_name(self, obj):
        return obj.state.name
    
    brand_name = serializers.SerializerMethodField(read_only=True)
    def get_brand_name(self, obj):
        return obj.other_brand or obj.brand.name_en
    
    category_name = serializers.SerializerMethodField(read_only=True)
    def get_category_name(self, obj):
        return obj.other_category or  obj.category.name
    
    color_name = serializers.SerializerMethodField(read_only=True)
    def get_color_name(self, obj) : 
        return obj.color.name 
     
    document_name = serializers.SerializerMethodField(read_only=True)
    def get_document_name(self, obj) : 
        return obj.document.name
    
    fuel_name = serializers.SerializerMethodField(read_only=True)
    def get_fuel_name(self, obj) : 
        return obj.fuel.name
    
    gear_box_name = serializers.SerializerMethodField(read_only=True)
    def get_gear_box_name(self, obj) : 
        return obj.gear_box.name
    
    class Meta:
        model = Article
        fields = ['brand_name', 'category_name', 'title', 'year', 'price', 'offered_price', 'color_name', 'document_name', 'fuel_name', 'engine', 'is_used', 'exchange', 'mileage', 'gear_box_name', 'is_all_options', 'state_name', 'city']

class ArticlePageSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField(read_only=True)
    def get_creator_name(self, obj):
        creator = obj.creator
        return {'text' :creator.page.name, 'is_verified': creator.page.is_verified } if creator.extention.is_page else creator.get_full_name()
    
    creator_username = serializers.SerializerMethodField(read_only=True)
    def get_creator_username(self, obj):
        return obj.creator.username
    
    creator_image = serializers.SerializerMethodField(read_only=True)
    def get_creator_image(self, obj):
        try: 
            return get_media_url(obj.creator.image.url_150)
        except:
            if obj.creator.extention.is_page:
                return '/static/others/page_icon_150.png'
            else:
                return '/static/others/user_150.png'
    
    creator_id = serializers.SerializerMethodField(read_only=True)
    def get_creator_id(self, obj):
        return obj.creator.id

    phone_numbers_list = serializers.SerializerMethodField(read_only=True)
    def get_phone_numbers_list(self, obj):
        return json.loads(obj.phone_numbers)
    
    images = serializers.SerializerMethodField(read_only=True)
    def get_images(self, obj):
        return ImageSerializer(obj.image_set.all(), many=True).data
    
    info = serializers.SerializerMethodField(read_only=True)
    def get_info(self, obj):
        return ArticlePageSerializerInfo(obj, many=False).data

    options = serializers.SerializerMethodField(read_only=True)
    def get_options(self, obj):
        return list(obj.options.values_list('name', flat=True))
    
    is_saver = serializers.SerializerMethodField(read_only=True)
    def get_is_saver(self, obj):
        user = self.context.get('user')
        return SavedArticle.objects.filter(saver=user, article=obj).exists()

    is_liker = serializers.SerializerMethodField(read_only=True)
    def get_is_liker(self, obj):
        user = self.context.get('user')
        return Like.objects.filter(liker=user, article=obj).exists()
    
    is_disliker = serializers.SerializerMethodField(read_only=True)
    def get_is_disliker(self, obj):
        user = self.context.get('user')
        return Dislike.objects.filter(disliker=user, article=obj).exists()
    
    
    class Meta:
        model = Article
        fields = ['id', 'info', 'likes_count', 'dislikes_count', 'options', 'created_at', 'creator_name', 'creator_username', 'images', 'phone_numbers_list', 'description', 'creator_image', 'creator_id', 'is_saver', 'is_liker', 'is_disliker']

class ArticleCardA(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    def get_url(self, obj):
        return obj.slug
    
    brand_name = serializers.SerializerMethodField(read_only=True)
    def get_brand_name(self, obj):
        return obj.other_brand or obj.brand.name_en

    state_name = serializers.SerializerMethodField(read_only=True)
    def get_state_name(self, obj):
        return obj.state.name
    
    main_image = serializers.SerializerMethodField(read_only=True)
    def get_main_image(self, obj):
        try:
            main_image = obj.main_image and obj.main_image.url
            main_image = get_media_url(main_image)
        except:
            main_image =""
        return main_image
    
    class Meta:
        model = Article
        fields = ['id', 'main_image', 'brand_name', 'title', 'price', 'offered_price', 'state_name', 'city', 'views', 'year', 'likes_count', 'url', 'created_at', 'is_used']

class ArticleCardB(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    def get_url(self, obj):
        return obj.slug
    
    brand_name = serializers.SerializerMethodField(read_only=True)
    def get_brand_name(self, obj):
        return obj.other_brand or obj.brand.name_en

    state_name = serializers.SerializerMethodField(read_only=True)
    def get_state_name(self, obj):
        return obj.state.name
    
    main_image = serializers.SerializerMethodField(read_only=True)
    def get_main_image(self, obj):
        try:
            main_image = obj.main_image and obj.main_image.url
            main_image = get_media_url(main_image)
        except:
            main_image =""
        return main_image
    
    class Meta:
        model = Article
        fields = ['id', 'main_image', 'brand_name', 'title', 'price', 'offered_price', 'state_name', 'city', 'views', 'likes_count', 'url', 'created_at']

class BrandBrowserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return obj.name_en
    
    icon = serializers.SerializerMethodField(read_only=True)
    def get_icon(self, obj):
        return get_media_url(obj.icon.url) if obj.icon else ''
    
    class Meta:
        model = Brand
        fields = ['name', 'icon', 'id', 'order']
    


class CategoryBrowserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'icon', 'id', 'order', 'brands']
    
    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return getattr(obj, self.context['name_lang'])
    
    icon = serializers.SerializerMethodField(read_only=True)
    def get_icon(self, obj):
        return get_media_url(obj.icon.url)

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'id']

    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return getattr(obj, self.context['name_lang'])

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name', 'id']

    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return getattr(obj, self.context['name_lang'])

class GearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearBox
        fields = ['name', 'id']

    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return getattr(obj, self.context['name_lang'])

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['name', 'id']

    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return getattr(obj, self.context['name_lang'])

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['name', 'id']

    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self, obj):
        return getattr(obj, self.context['name_lang'])

class CommentSerializer(serializers.ModelSerializer):
    
    commenter_image = serializers.SerializerMethodField(read_only=True)
    def get_commenter_image(self, obj):
        try :
            return get_media_url(obj.commenter.image.url_150)
        except:
            if obj.commenter.extention.is_page:
                return '/static/others/page_icon_150.png'
            else:
                return '/static/others/user_150.png'
    
    commenter_name = serializers.SerializerMethodField(read_only=True)
    def get_commenter_name(self, obj):
        commenter = obj.commenter
        return {'text' :commenter.page.name, 'is_verified': commenter.page.is_verified } if commenter.extention.is_page else commenter.get_full_name() 
    
    commenter_id = serializers.SerializerMethodField(read_only=True)
    def get_commenter_id(self, obj):
        return obj.commenter.id
    
    commenter_username = serializers.SerializerMethodField(read_only=True)
    def get_commenter_username(self, obj):
        return obj.commenter.username
    
    article_id = serializers.SerializerMethodField(read_only=True)
    def get_article_id(self, obj):
        return obj.article.id
    
    class Meta:
        model = Comment
        fields = ['id', 'commenter_image', 'created_at', 'commenter_name', 'text', 'commenter_id', 'article_id', 'commenter_username']

class ArticleSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSuggestion
        fields = ['id', 'text']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url']
    
    url = serializers.SerializerMethodField(read_only=True)
    def get_url(self, obj):
        return get_media_url(obj.url)
    

class ImageSerializerEditArticle(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url']
    
    url = serializers.SerializerMethodField(read_only=True)
    def get_url(self, obj):
        return obj.url


class EditArticleSerializer(serializers.ModelSerializer):
    state_code = serializers.SerializerMethodField(read_only=True)
    def get_state_code(self, obj):
        return obj.state.code
    
    brand_id = serializers.SerializerMethodField(read_only=True)
    def get_brand_id(self, obj):
        return obj.brand.id
    
    category_id = serializers.SerializerMethodField(read_only=True)
    def get_category_id(self, obj):
        return obj.category.id
    
    color_id = serializers.SerializerMethodField(read_only=True)
    def get_color_id(self, obj):
        return obj.color.id
    
    document_id = serializers.SerializerMethodField(read_only=True)
    def get_document_id(self, obj):
        return obj.document.id
    
    document_id = serializers.SerializerMethodField(read_only=True)
    def get_document_id(self, obj):
        return obj.document.id
    
    fuel_id = serializers.SerializerMethodField(read_only=True)
    def get_fuel_id(self, obj):
        return obj.fuel.id
    
    gear_box_id = serializers.SerializerMethodField(read_only=True)
    def get_gear_box_id(self, obj):
        return obj.gear_box.id
    
    options = serializers.SerializerMethodField(read_only=True)
    def get_options(self, obj):
        return list(obj.options.values_list('id', flat=True))
    
    phone_numbers_list = serializers.SerializerMethodField(read_only=True)
    def get_phone_numbers_list(self, obj):
        return json.loads(obj.phone_numbers)
    
    images_list = serializers.SerializerMethodField(read_only=True)
    def get_images_list(self, obj):
        return  ImageSerializerEditArticle(obj.image_set.all(), many=True).data
    
    main_image_id = serializers.SerializerMethodField(read_only=True)
    def get_main_image_id(self, obj):
        return obj.main_image.image.id
    
    class Meta:
        model = Article
        fields = ['state_code', 'city', 'title', 'brand_id', 'other_brand', 'other_category', 'category_id', 'year', 'color_id', 'document_id', 'engine', 'price', 'offered_price', 'is_used', 'mileage', 'fuel_id', 'gear_box_id', 'exchange', 'is_all_options', 'options', 'description', 'phone_numbers_list', 'images_list', 'main_image_id']



class ArticleCardAOtherOptions(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['options', 'document', 'engine', 'mileage', 'fuel', 'gear_box', 'description', "exchange", 'is_all_options']