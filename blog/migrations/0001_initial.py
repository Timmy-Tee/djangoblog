# Generated by Django 5.0.6 on 2024-06-01 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('comments', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('coverImage', models.ImageField(upload_to='Author')),
                ('description', models.TextField()),
                ('likes', models.PositiveBigIntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comments')),
            ],
        ),
    ]