# Generated by Django 5.0.1 on 2024-02-21 21:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_postmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
