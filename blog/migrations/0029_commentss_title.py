# Generated by Django 5.0.6 on 2024-06-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_rename_blog_blogs_rename_comments_commentss_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentss',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
