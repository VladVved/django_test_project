# Generated by Django 2.0.1 on 2018-03-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180316_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]