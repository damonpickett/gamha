# Generated by Django 5.0.2 on 2024-02-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_remove_post_subtitle"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="subtitle",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
