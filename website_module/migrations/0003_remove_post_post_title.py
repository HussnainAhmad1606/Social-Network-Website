# Generated by Django 3.1.4 on 2021-03-26 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_module', '0002_auto_20210326_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_title',
        ),
    ]
