from django.apps import AppConfig



class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'

    def ready(self) -> None:
        import article.signals
        return super().ready()