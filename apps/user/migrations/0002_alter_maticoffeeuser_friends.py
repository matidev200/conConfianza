# Generated by Django 4.2 on 2023-04-30 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maticoffeeuser',
            name='friends',
            field=models.ManyToManyField(blank=True, to='user.friend'),
        ),
    ]
