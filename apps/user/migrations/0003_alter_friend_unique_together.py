# Generated by Django 4.2 on 2023-05-01 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_maticoffeeuser_friends'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('user', 'user_to_request')},
        ),
    ]