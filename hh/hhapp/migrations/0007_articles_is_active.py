# Generated by Django 3.2.12 on 2022-08-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhapp', '0006_articles_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
