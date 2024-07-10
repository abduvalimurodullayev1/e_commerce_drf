from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product, User
from django.contrib import admin


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)

admin.site.register([
    User,
    # BlogImage,
    Category,
    Product
])
