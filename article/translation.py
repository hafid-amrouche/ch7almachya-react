from modeltranslation.translator import register, TranslationOptions
from .models import Category, Option, Fuel, GearBox, Color, Document, Brand


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Fuel)
class FuelTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(GearBox)
class GearBoxTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ("name",)
    
@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ("name",)




