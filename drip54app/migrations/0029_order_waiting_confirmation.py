# Generated by Django 4.0.3 on 2022-08-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip54app', '0028_order_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='waiting_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]
