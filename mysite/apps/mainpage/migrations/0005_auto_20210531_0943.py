# Generated by Django 3.1.7 on 2021-05-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20210526_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.png', upload_to='static/media/profile'),
        ),
    ]
