# Generated by Django 4.2.3 on 2024-07-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='MyProfile',
        ),
    ]
