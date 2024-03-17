from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import time, json, os
from django.http import JsonResponse, HttpResponse
from others.models import State
from .models import Article, Image, Comment, Option, SavedArticle, Like, Dislike, Color, Document, Fuel, GearBox
from PIL import Image as IM
from ch7almachya.settings import MEDIA_ROOT
from .serializers import ArticlePageSerializer, CommentSerializer, ArticleCardA, ArticleSuggestionSerializer, EditArticleSerializer, ArticleCardAOtherOptions
from rest_framework.response import Response
from django.db.models import Q, F, ExpressionWrapper, IntegerField, Sum, Case, When, Count, Subquery, OuterRef, Value
from datetime import datetime
from django.utils import timezone
from .models import ArticleSuggestion
from django.db.models.functions import Concat
from django.db.models import CharField
from django.utils.translation import gettext as _


current_year = str(datetime.now().year)
# Create your views here.

@api_view(['GET'])
def get_article(request):
    try:
        article = Article.objects.get(id=request.GET.get('id'))
        article.notification_set.all().update(is_seen=True, is_acknowledged=True)
        print(request.user)
        articleSerialized = ArticlePageSerializer(article, many=False, context={'user' : request.user.is_authenticated and request.user}).data
        new_views_count =  article.views +1
        article.views = new_views_count
        article.save()
        return Response(articleSerialized)
    except Exception as e:
        return JsonResponse({'detail' : str(e)}, status=400, safe=True)

@api_view(['POST'])
def get_article_comments(request):
    article_id = request.POST.get('article-id')
    seen_comments = json.loads(request.POST.get('seen-comments'))
    comments = Comment.objects.filter(article__id = article_id).exclude(id__in = seen_comments)
    comments_length = len(comments)
    comments = comments.order_by('-created_at')[:10]
    comments = CommentSerializer(comments, many=True).data
    is_next = comments_length > 10
    return Response([comments, is_next])

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request):
    comment_id = request.POST.get('comment-id')
    comment = Comment.objects.get(id = comment_id)
    if request.user.is_authenticated and (comment.commenter == request.user or comment.article.creator == request.user):
       comment.delete()
       return JsonResponse({'detail': 'Done'}, status=200)
    else:
        return JsonResponse({'detail' : 'Illegal action'}, status=400)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    text = request.POST.get('text').strip()
    if text :
        comment = request.user.comments.create(
            article_id = int(request.POST.get('articleId')),
            text = text
        )
        return Response(CommentSerializer(comment, many=False).data)
    else:
        return JsonResponse({'detail' : 'Illegal action'}, status=400)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request):
    article = Article.objects.get(id=request.POST.get('article-id'))
    like, cond = Like.objects.get_or_create(liker=request.user, article=article)
    if not cond:
        like.delete()
    else:
        try:
            Dislike.objects.get(disliker=request.user, article=article).delete()
        except:
            pass

    likes_count = article.like_set.all().count()
    article.likes_count = likes_count
    dislike_count = article.dislike_set.all().count()
    article.dislikes_count = dislike_count
    like_per = likes_count * (dislike_count + likes_count)
    article.like_per = like_per
    article.save()

    return JsonResponse({'detail': 'Done'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_article(request):
    article = Article.objects.get(id=request.POST.get('article-id'))
    dislike, cond = Dislike.objects.get_or_create(disliker=request.user, article=article)
    if not cond:
        dislike.delete()
    else:
        try:
            Like.objects.get(liker=request.user, article=article).delete()
        except:
            pass

    likes_count = article.like_set.all().count()
    article.likes_count = likes_count
    dislike_count = article.dislike_set.all().count()
    article.dislikes_count = dislike_count
    like_per = likes_count *(dislike_count + likes_count)
    article.like_per = like_per
    article.save()

    return JsonResponse({'detail': 'Done'},status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])   
def toggle_save_article(request):
    article = Article.objects.get(id=request.POST.get('article-id'))
    user = request.user
    is_saver = False
    saved_article, cond = SavedArticle.objects.get_or_create(saver=user, article=article)
    if not cond:
        saved_article.delete()
    else:
        is_saver = True
    return JsonResponse(is_saver, status=200, safe=False)

def filter_articles_by_parameter(articles, filter_parameters):
    query_conditions={}
    if filter_parameters.get('states'):
        query_conditions['state__code__in'] = filter_parameters['states']
    
    if filter_parameters.get('colors'):
        query_conditions['color__in'] = filter_parameters['colors']
    
    if filter_parameters.get('documents'):
        query_conditions['document__in'] = filter_parameters['documents']
    
    if filter_parameters.get('fuels'):
        query_conditions['fuel__in'] = filter_parameters['fuels']
    
    if filter_parameters.get('gear_boxs'):
        query_conditions['gear_box__in'] = filter_parameters['gear_boxs']

    if filter_parameters.get('brand'):
        query_conditions['brand'] = filter_parameters['brand']

    if filter_parameters.get('category'):
        query_conditions['category'] = filter_parameters['category']
    
    if filter_parameters.get('exchange_only'):
         query_conditions={
            'exchange' : True,
            **query_conditions,
        }
    
    print(filter_parameters)
    if filter_parameters.get('carConditionNew') == False:
         query_conditions={
            'is_used' : True,
            **query_conditions,
        }
    elif filter_parameters.get('carConditionUsed') == False:
         query_conditions={
            'is_used' : False,
            **query_conditions,
        }

    if filter_parameters.get('min_price') and not filter_parameters.get('max_price') and filter_parameters.get('min_price') > '0' :
        query_conditions['search_price__gte'] = filter_parameters.get('min_price')

    elif filter_parameters.get('max_price') and not filter_parameters.get('min_price') and filter_parameters.get('max_price') > '0' :
        query_conditions['search_price__lte'] = filter_parameters.get('max_price')
    
    elif filter_parameters.get('min_price') and filter_parameters.get('max_price') and filter_parameters.get('max_price') > filter_parameters.get('min_price') > 0:
        query_conditions['search_price__range'] = (filter_parameters.get('min_price'), filter_parameters.get('max_price'))

    if filter_parameters.get('min_year') and not filter_parameters.get('max_year') and '1900' < filter_parameters.get('min_year') < current_year :
        query_conditions['search_year__gte'] = filter_parameters.get('min_year')

    elif filter_parameters.get('max_year') and not filter_parameters.get('min_year')  and '1900' < filter_parameters.get('max_year') < current_year:
        query_conditions['search_year__lte'] = filter_parameters.get('max_year')
    
    elif filter_parameters.get('min_year') and filter_parameters.get('max_year') and '1990' < filter_parameters.get('min_year') < filter_parameters.get('max_year') < current_year:
        query_conditions['search_year__range'] = (filter_parameters.get('min_year'), filter_parameters.get('max_year'))

    if filter_parameters.get('mileage') and filter_parameters.get('mileage') > '0':
        query_conditions['mileage__lte'] = filter_parameters.get('mileage')


    if filter_parameters.get('allOptionOnly'):
        query_conditions['is_all_options'] = True

    elif filter_parameters.get('options'):
        options_id = filter_parameters.get('options')
        # Annotate the count of options for each article
        articles_with_options_count = articles.annotate(options_count=Count('options'))

        # Subquery to get the count of options for the specified options_id
        subquery = Option.objects.filter(
            id__in=options_id,
            article=OuterRef('pk')
        ).values('article').annotate(option_count=Count('id')).values('option_count')[:1]

        # Filter articles based on additional conditions (e.g., is_active=True)
        filtered_articles = articles_with_options_count.filter(**query_conditions, options_count__gte=len(options_id))

        # Filter articles that have all the specified options_id
        filtered_articles = filtered_articles.annotate(
            matching_options_count=Subquery(subquery)
        ).filter(matching_options_count=len(options_id))
        return filtered_articles
    
    print(query_conditions)
    filtered_articles = articles.filter(**query_conditions)
    return filtered_articles

def filter_articles_by_search_text(articles, search_text_words_list):
    title_relevance = Sum(
                Case(
                    *[
                        When(
                            **{
                                f"title__iexact": word,
                                'then': 10,
                            }
                        )
                        for word in search_text_words_list
                    ]
                ),
                default=0,
                output_field=IntegerField()
    )

    brand_relevance = Sum(
        Case(
            *[
                When(
                    **{
                        f"brand__name_en__iexact": word,
                        'then': 5,
                    }
                )
                for word in search_text_words_list
            ]
        ),
        default=0,
        output_field=IntegerField()
    ) +Sum(
        Case(
            *[
                When(
                    **{
                        f"brand__name_ar__iexact": word,
                        'then': 5,
                    }
                )
                for word in search_text_words_list
            ]
        ),
        default=0,
        output_field=IntegerField()
    ) + Sum(
        Case(
            *[
                When(
                    **{
                        f"other_brand__iexact": word,
                        'then': 5,
                    }
                )
                for word in search_text_words_list
            ]
        ),
        default=0,
        output_field=IntegerField()
    )

    description_relevance = Sum(
        Case(
            *[
                When(
                    **{
                        f"description__icontains": word,
                        'then': 1,
                    }
                )
                for word in search_text_words_list
            ]
        ),
        default=0,
        output_field=IntegerField()
    )

    year_relevance = Sum(
        Case(
            *[
                When(
                    **{
                        f"year__iexact": word,
                        'then': 1,
                    }
                )
                for word in search_text_words_list
            ]
        ),
        default=0,
        output_field=IntegerField()
    )

    color_relevance = Sum(
        Case(
            *[
                When(
                    **{
                        f"color__name__iexact": word,
                        'then': 1,
                    }
                )
                for word in search_text_words_list
            ]
        ),
        default=0,
        output_field=IntegerField()
    )
    
    ordered_articles = articles.annotate(
        relevance = title_relevance + brand_relevance + description_relevance + year_relevance + color_relevance
    ).filter(relevance__gte = 5)
    
    
    return ordered_articles


def SA(filter_parameters, seen_articles, search_text_words_list, search_text):
    articles = Article.objects.exclude(id__in = seen_articles)
    filtered_articles_by_parameters = filter_articles_by_parameter(articles,filter_parameters)
    if search_text != '*' :
        filtered_articles = filter_articles_by_search_text(filtered_articles_by_parameters, search_text_words_list).order_by('-relevance', '-created_at')
    else:
        filtered_articles = filtered_articles_by_parameters.order_by('-created_at')

    articles_len = len(filtered_articles)
    is_next = articles_len > 20
    filtered_articles = filtered_articles[:20]
    serialized_filtered_articles = ArticleCardA(filtered_articles, many=True).data
    return Response([serialized_filtered_articles, is_next], status=200)


@api_view(['POST'])
def serach_articles(request): 
    filter_parameters = request.POST.get('filter_parameters')
    filter_parameters = json.loads(filter_parameters)
    seen_articles = json.loads(request.POST.get('seen_articles'))
    search_text_words_list = json.loads(request.POST.get('search_text_words_list'))
    search_text = request.POST.get('search_text')
    return SA(filter_parameters, seen_articles, search_text_words_list, search_text)

@api_view(['GET'])
def get_simular_articles(request):
    search_text = request.GET.get('search_text')
    search_text_words_list = json.loads(request.GET.get('search_text_words_list'))
    article_id = request.GET.get('article_id')
    return SA({}, [article_id], search_text_words_list, search_text)

@api_view(['GET'])
def article_suggestions(request):
    text = request.GET.get('text')
    suggestions = ArticleSuggestion.objects.filter(text__icontains = text).order_by('-times')[:10]
    serialized_suggestions = ArticleSuggestionSerializer(suggestions, many=True).data
    return Response(serialized_suggestions)


@api_view(['GET'])
def article_other_info(request):
    article_id = request.GET.get('article-id') 
    article = Article.objects.get(id =article_id)
    serialized_other_info = ArticleCardAOtherOptions(article, many=False).data
    return Response(serialized_other_info, status=200)