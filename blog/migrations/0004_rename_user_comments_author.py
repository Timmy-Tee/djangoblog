# Generated by Django 5.0.6 on 2024-06-02 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comments_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='author',
        ),
    ]
