# Generated by Django 4.0.3 on 2022-08-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip54app', '0016_userprofile_email_userprofile_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
    ]
