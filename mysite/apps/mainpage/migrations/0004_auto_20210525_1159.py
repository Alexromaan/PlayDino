# Generated by Django 3.2 on 2021-05-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20210524_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='nota',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='series',
            name='nota',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='films',
            name='image',
            field=models.ImageField(default='default.png', upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DefaultImageDino.png', upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(default='default.png', upload_to='static/media/'),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
