# Generated by Django 5.0.6 on 2024-06-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_comments_totalreplies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
