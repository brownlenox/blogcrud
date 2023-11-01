# Generated by Django 4.2.7 on 2023-11-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('body', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('craeted_at', models.TimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
