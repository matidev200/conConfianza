# Generated by Django 4.2 on 2023-05-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_friend_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maticoffeeuser',
            name='profile_img',
            field=models.ImageField(default='src/profile_images/default.png', upload_to='static/src/profile_images'),
        ),
    ]
