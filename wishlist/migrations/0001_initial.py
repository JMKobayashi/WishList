# Generated by Django 3.1.4 on 2021-03-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(blank=True, max_length=2000)),
                ('image_like', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]