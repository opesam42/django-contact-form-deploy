# Generated by Django 5.1 on 2024-08-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='agree_terms',
            field=models.BooleanField(default=False),
        ),
    ]
