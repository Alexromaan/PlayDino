# Generated by Django 3.1.7 on 2021-05-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DefaultImageDino.png', upload_to='static/media'),
        ),
    ]
