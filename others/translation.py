from modeltranslation.translator import register, TranslationOptions
from .models import State


@register(State)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)




