# Generated by Django 4.0.5 on 2023-04-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_adminmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmessage',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]