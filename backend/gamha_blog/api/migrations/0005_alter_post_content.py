# Generated by Django 5.0.2 on 2024-02-22 02:38

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_post_subtitle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
    ]
