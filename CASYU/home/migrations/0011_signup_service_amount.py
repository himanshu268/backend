# Generated by Django 4.1 on 2022-10-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_signup_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_service',
            name='amount',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
