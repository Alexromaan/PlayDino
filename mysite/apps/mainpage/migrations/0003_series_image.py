# Generated by Django 3.1.7 on 2021-05-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20210513_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='image',
            field=models.ImageField(default='static/media/default.png', upload_to='static/media'),
        ),
    ]
