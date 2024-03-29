from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import json, os
from django.http import JsonResponse
from django.utils.text import slugify
from others.models import State, Notification
from article.models import Article, Image, Option, ArticleSuggestion, MainImage, Brand, Category
from PIL import Image as IM
from ch7almachya.settings import BASE_DIR
from article.serializers import ArticleCardB, EditArticleSerializer
from rest_framework.response import Response
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone
from user.models import User


current_year = datetime.now().year

# Create your views here.

admin = User.objects.get(username='ch7almachya')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    try:
        user = request.user
        if user.articles.count()>= 20:
            message ={'detail' : _('You cannot create more than 20 articles in the basic plan')}
            return JsonResponse(message, status=400, safe=False)
        data = request.POST
        title = data['title'].strip()
        if title == '':
            message ={'detail' : _('Title cannot be empty') }
            return JsonResponse(message, status=400, safe=False)
        price = int(data['price'])
        offered_price = int(data['offered_price'])
        search_price = price or offered_price
        engine = data['engine']
        is_used = data['car_condition'] == 'Used'
        exchange = data['exchange'] == 'true'
        year = int(data['year'])
        all_options_car = data['all_options_car'] == 'true'
        if all_options_car:
            options_list = []
        else:
            options_list = data.getlist('car_options[]')

        mileage = int(data['mileage'])
        state = State.objects.get(code=data['state'])
        city = data['city'].strip()
        description = data['description'].strip() 

        phone_number_1 = request.POST.get('phone_number_1').strip()
        phone_number_2 = request.POST.get('phone_number_2').strip()
        phone_number_3 = request.POST.get('phone_number_3').strip()

        phone_numbers = []
        if 9 <= len(phone_number_1) <= 13 :
            phone_numbers.append(phone_number_1)
        if 9 <= len(phone_number_2) <= 13  :
            phone_numbers.append(phone_number_2)
        if 9 <= len(phone_number_3) <= 13  :
            phone_numbers.append(phone_number_3)
        
        phone_numbers = json.dumps(phone_numbers)

        brand = Brand.objects.get(id=data['brand'])
        other_brand = data['other_brand'] if data['brand'] == '93' else ''
        category = Category.objects.get(id=data['category'])
        other_category = data['other_category'] if data['category'] == '10' else ''

        if not(brand in category.brands.all()):
            message ={'detail' : 'Category and Brand do not match'}
            return JsonResponse(message, status=400, safe=False)

        article = Article.objects.create(
            creator=user,
            title = title,
            brand = brand,
            category = category,
            other_category = other_category, 
            other_brand = other_brand,
            price = price,
            offered_price = offered_price,
            search_price = search_price,
            engine = engine,
            is_used = is_used,
            exchange = exchange,
            year = year,
            color_id = data['color'],
            document_id = data['document'],
            fuel_id = data['fuel'],
            gear_box_id = data['gear_box'],
            is_all_options = all_options_car,
            mileage = mileage,
            state = state,
            city = city,
            description = description,
            phone_numbers = phone_numbers,
        )
        article.slug =  f'/@{user.username}/{slugify(f"{other_brand or brand.name} {title} {article.id}")}/'

        if not all_options_car:
            article.options.set(Option.objects.filter(id__in = options_list))
        
        os.mkdir(BASE_DIR / f'media/users/{user.id}/articles/{article.id}')
        images = request.FILES.getlist('images[]')
        if len(images) == 0 :
            article.delete()
            message= { 'detail' : _('The images you sent were not recognized please try again')}
            return JsonResponse(message, status=400, safe=False)
        images_count = 0
        for image in images :
            try:
                image = IM.open(image)
                image = image.convert('RGB')
                if image.width > 2024 or image.height > 2024 :  # manipulated in client side
                    image.thumbnail((2024, 2024))
                    imageObject = Image.objects.create(article=article)
                    url = f"/media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    path = BASE_DIR / f"media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    imageObject.path = path
                    imageObject.url = url
                    imageObject.save()
                    image.save(
                        path,
                        "JPEG",
                        optimize=True,
                        quality=80
                    )
                    
                else:
                    imageObject = Image.objects.create(article=article)
                    url = f"/media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    path = BASE_DIR / f"media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    imageObject.path = path
                    imageObject.url = url
                    imageObject.save()
                    image.save(path,"JPEG")
                if images_count == 0 :
                    image.thumbnail((400, 400))
                    main_url = f"/media/users/{ user.id }/articles/{article.id}/main.jpeg"
                    main_path = BASE_DIR / f"media/users/{ user.id }/articles/{article.id}/main.jpeg"
                    image.save(main_path,"JPEG")
                    MainImage.objects.create(
                        article = article,
                        image = imageObject,
                        url = main_url,
                        path= main_path
                    )
                images_count +=1
            except Exception as e:
                pass
            if images_count == 20:
                break
            
        if images_count == 0 :
            article.delete()
            message = {'detail': _('Your images were not accepted please use other images and try again')}
            return JsonResponse(message, status=400, safe=False)

        article.save()

        article_suggestion, cond = ArticleSuggestion.objects.get_or_create(text = f'{article.brand.name} {title}')
        if not cond:
            article_suggestion.times += 1
            article_suggestion.save()

        message= {  
            'detail' : {
                'url' : article.slug
            }
        }
        Notification.objects.create(
            notification_type = 'article_created',
            notifier=admin,
            notified=request.user,
            article=article,
            text = _('Your artcile was created successfully')
        )
        return JsonResponse(message, safe=False)
    except Exception as e:
        try:
            article.delete()
        except:
            pass
        message = {'detail':str(e)}
        return JsonResponse(message, status=400, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_article(request):
    try:
        user = request.user
        data = request.POST
        article = Article.objects.get(creator=user, id=request.POST.get('article_id'))
        title = data['title'].strip()
        if title == '':
            message ={ 'detail' : _('Title cannot be empty')}
            return JsonResponse(message, status=400, safe=False)
        price = int(data['price'])
        offered_price = int(data['offered_price'])
        search_price = price or offered_price
        engine = data['engine']
        is_used = data['car_condition'] == 'Used'
        exchange = data['exchange'] == 'true'
        year = int(data['year'])
        all_options_car = data['all_options_car'] == 'true'
        if all_options_car:
            options_list = []
        else:
            options_list = data.getlist('car_options[]')


        mileage = int(data['mileage'])
        state = State.objects.get(code=data['state'])
        city = data['city'].strip()
        description = data['description'].strip() 

        phone_number_1 = request.POST.get('phone_number_1').strip()
        phone_number_2 = request.POST.get('phone_number_2').strip()
        phone_number_3 = request.POST.get('phone_number_3').strip()

        phone_numbers = []
        if 9 <= len(phone_number_1) <= 13 :
            phone_numbers.append(phone_number_1)
        if 9 <= len(phone_number_2) <= 13  :
            phone_numbers.append(phone_number_2)
        if 9 <= len(phone_number_3) <= 13  :
            phone_numbers.append(phone_number_3)
        
        phone_numbers = json.dumps(phone_numbers)

        brand = Brand.objects.get(id=data['brand'])
        other_brand = data['other_brand'] if data['brand'] == '93' else ''
        category = Category.objects.get(id=data['category'])
        other_category = data['other_category'] if data['category'] == '10' else ''
        if not(brand in category.brands.all()):
            message ={'detail' :'Category and Brand do not match'}
            return JsonResponse(message, status=400, safe=False)

        article.title = title
        article.brand = brand
        article.category = category
        article.other_category = other_category
        article.other_brand = other_brand
        article.slug= f'/@{user.username}/{slugify(f"{ other_brand or brand.name} {title} {article.id}")}/'
        article.price = price
        article.offered_price = offered_price
        article.search_price = search_price
        article.engine = engine
        article.is_used = is_used
        article.exchange = exchange
        article.year = year
        article.color_id = data['color']
        article.document_id = data['document']
        article.fuel_id = data['fuel']
        article.gear_box_id = data['gear_box']
        article.is_all_options = all_options_car
        article.mileage = mileage
        article.state = state
        article.city = city
        article.description = description
        article.phone_numbers = phone_numbers
    
        article.options.set(Option.objects.filter(id__in = options_list))

        images = request.FILES.getlist('images[]')       
        images_count = 0
        max_images = 20 - article.image_set.count()
        for image in images :
            try:
                image = IM.open(image)
                image = image.convert('RGB')
                if image.width > 2024 or image.height > 2024 :  # manipulated in client side
                    image.thumbnail((2024, 2024))
                    imageObject = Image.objects.create(article=article)
                    url = f"/media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    path = BASE_DIR / f"media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    imageObject.path = path
                    imageObject.url = url
                    imageObject.save()
                    image.save(
                        path,
                        "JPEG",
                        optimize=True,
                        quality=80
                    )
                    
                else:
                    imageObject = Image.objects.create(article=article)
                    url = f"/media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    path = BASE_DIR / f"media/users/{ user.id }/articles/{article.id}/{imageObject.id}.jpeg"
                    imageObject.path = path
                    imageObject.url = url
                    imageObject.save()
                    image.save(path,"JPEG")
                images_count += 1
            except Exception as e:
                pass
            if images_count == max_images:
                break
        
        article.save()

        article_suggestion, cond = ArticleSuggestion.objects.get_or_create(text = f'{article.brand.name} {title}')
        if not cond:
            article_suggestion.times += 1
            article_suggestion.save()

        try:
            if article.report.acknoleged == True :
                article.report.delete()
        except:
            pass
        
        message= {  
            'detail' : {
                'url' : article.slug
            }
        }
        Notification.objects.create(
            notification_type = 'article_updated',
            notifier=admin,
            notified=request.user,
            article=article,
            text = _('Your artcile was updated successfully')
        )
        return JsonResponse(message, safe=False)
    except Exception as e:
        message = {'detail':str(e)}
        return JsonResponse(message, status=400, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_user_articles(request):
    seen_articles = json.loads(request.POST.get('seen-articles'))
    try:
        articles = Article.objects.filter(creator = request.user).exclude(id__in=seen_articles)
        cond = articles.count() > 20
        articles = articles.order_by('-created_at')[:20]
        articles = ArticleCardB(articles, many=True).data
        return Response([articles, cond])
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_article(request):
    article_id = request.POST.get('article_id')
    try:
        article = Article.objects.get(creator=request.user, id=article_id)
        article_name = article.title
        brand = article.brand
        article.delete()
        message ={'detail' : _('the article "{} - {}" has been deleted successfully').format(brand, article_name)}
        return JsonResponse(message, status=200)
    except :
        message ={'detail' : _('Article was not deleted')}
        return JsonResponse(message, status=400)
 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def saved_articles(request):
    try:
        saved_articles = request.user.saved_articles.all()
        cond = saved_articles.count() > 20
        saved_articles = saved_articles.order_by('-saved_at')[:20]
        articles = Article.objects.filter(id__in=saved_articles.values('article')).order_by('-savedarticle__saved_at')
        articles = ArticleCardB(articles, many=True).data
        return Response([articles, cond])
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)
    

@api_view(['GET'])
def get_article_for_edit(request):
    try:
        article = request.user.articles.get(id=request.GET.get('article-id'))
        return Response(EditArticleSerializer(article).data, status=200)
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_image(request):
    image_id = request.POST.get('article_id')
    article = request.user.articles.get(id=image_id)
    data = None
    if article.image_set.count() > 1 :
        image_id = request.POST.get('image_id')
        image = article.image_set.get(id=image_id)
        main_image_exist = MainImage.objects.filter(article=article, image=image).exists()
        if not main_image_exist:
            data = image_id
            image.delete()

    return JsonResponse(data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_main_image(request):
    article = request.user.articles.get(id=request.POST.get('article_id'))
    data = request.POST.get('image_id')
    image = article.image_set.get(id=data)
    main_image = MainImage.objects.get(article=article)
    main_image.image = image
    main_image.save()
    new_image = IM.open(image.path)
    new_image = new_image.convert('RGB')
    new_image.thumbnail((400, 400))
    main_path = BASE_DIR / f"media/users/{ request.user.id }/articles/{article.id}/main.jpeg"
    new_image.save(main_path,"JPEG")
    return JsonResponse(data, safe=False)