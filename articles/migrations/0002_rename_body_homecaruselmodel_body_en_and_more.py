# Generated by Django 4.0.2 on 2022-02-21 10:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homecaruselmodel',
            old_name='body',
            new_name='body_en',
        ),
        migrations.RenameField(
            model_name='homecaruselmodel',
            old_name='summary',
            new_name='summary_en',
        ),
        migrations.RenameField(
            model_name='homecaruselmodel',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='body',
            new_name='body_en',
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='summary',
            new_name='summary_en',
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='title',
            new_name='summary_ru',
        ),
        migrations.AddField(
            model_name='homecaruselmodel',
            name='body_ru',
            field=ckeditor.fields.RichTextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecaruselmodel',
            name='body_uz',
            field=ckeditor.fields.RichTextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecaruselmodel',
            name='summary_ru',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecaruselmodel',
            name='summary_uz',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecaruselmodel',
            name='title_ru',
            field=models.CharField(default=None, max_length=100, verbose_name='title karusel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecaruselmodel',
            name='title_uz',
            field=models.CharField(default=None, max_length=100, verbose_name='title karusel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='body_ru',
            field=ckeditor.fields.RichTextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='body_uz',
            field=ckeditor.fields.RichTextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='summary_uz',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='title_en',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='title_ru',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='title_uz',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
