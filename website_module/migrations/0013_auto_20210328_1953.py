# Generated by Django 3.1.5 on 2021-03-28 14:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website_module', '0012_auto_20210328_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_like',
            field=models.ManyToManyField(related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
