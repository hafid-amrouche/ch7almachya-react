from django.db import models
from user.models import User

# Create your models here.
   
class Category(models.Model):
    name= models.CharField(max_length=50)
    icon =  models.ImageField(null=True, blank=True, upload_to='categories_logos/')
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=1)
    icon = models.ImageField(null=True, blank=True, upload_to='brands_logos/')
    category = models.ManyToManyField(Category, related_name="brands", blank=True)

    def __str__(self):
        return self.name_ar
    
class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name
    

class Option(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Fuel(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class GearBox(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles') 
    title = models.CharField(max_length=255)
    slug = models.TextField()
    price = models.IntegerField(null=True, blank=True) 
    offered_price = models.IntegerField(null=True, blank=True)
    search_price = models.IntegerField(default=0) 
    engine = models.CharField(max_length=50, default="")
    is_used = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    exchange = models.BooleanField(default=False)
    year = models.IntegerField(default=1900)
    is_all_options = models.BooleanField(default=False)
    mileage = models.IntegerField()
    phone_numbers = models.TextField(default="[]")
    state = models.ForeignKey('others.State', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    rating = models.IntegerField(default=50)
    brand = models.ForeignKey(Brand, related_name="articels", on_delete=models.CASCADE, null=True)
    other_brand = models.CharField(max_length=50, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles", null=True)
    other_category = models.CharField(max_length=50, default="")
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    fuel = models.ForeignKey(Fuel, null=True, on_delete=models.SET_NULL)
    gear_box = models.ForeignKey(GearBox, null=True, on_delete=models.SET_NULL)
    options = models.ManyToManyField(Option)
    options_list = models.TextField(default='[]')
    scoore = models.FloatField(default=0)
    like_per = models.FloatField(default=0)

    def __str__(self):
        return f'{self.id} | {self.title}'
    
    class Meta:
        ordering = ['-created_at'] 

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)

class Dislike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    disliker = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.TextField(default='')
    def __str__(self):
        return str(self.article) + " | " + str(self.commenter)
 
class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    url = models.TextField(default="")
    path = models.TextField(default="")

class MainImage(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='main_image')
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.TextField(default="")
    path = models.TextField(default="")

class SavedArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    saver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_articles')
    saved_at = models.DateTimeField(auto_now_add=True)

class ArticleSuggestion(models.Model):
    text = models.CharField(max_length=50)
    times = models.PositiveIntegerField(default=1)