from modeltranslation.translator import register, TranslationOptions, translator

from app.models import Category, Product


# @register(Blog)
# class BlogTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ('title', 'description')


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslation)
