# Generated by Django 2.2 on 2020-04-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0002_auto_20200404_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
