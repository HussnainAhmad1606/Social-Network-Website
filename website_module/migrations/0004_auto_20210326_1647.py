# Generated by Django 3.1.5 on 2021-03-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_module', '0003_remove_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]