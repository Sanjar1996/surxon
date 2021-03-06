# Generated by Django 4.0.2 on 2022-02-15 11:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sub_title', models.CharField(max_length=250)),
                ('body', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutMaydon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maydon', models.FloatField()),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FutureModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.TextField()),
                ('plan', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='HodimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=250)),
                ('lavozim', models.CharField(max_length=250)),
                ('birth_day', models.DateField()),
                ('tg_joyi', models.CharField(max_length=150)),
                ('oqigan_joyi', models.CharField(blank=True, max_length=150)),
                ('ilmiy_darajasi', models.CharField(blank=True, max_length=150)),
                ('ish_tajribasi', models.SmallIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeCaruselModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title karusel')),
                ('summary', models.CharField(max_length=250)),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='MainSiteModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField()),
                ('youtube_silka', models.CharField(blank=True, max_length=100)),
                ('video', models.FileField(blank=True, upload_to='upload/')),
                ('icon', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Newsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=250)),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsPrise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('tarif', models.CharField(blank=True, max_length=50)),
                ('plan', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenuModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('descriptions', models.CharField(blank=True, max_length=250)),
                ('web_address', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
