# Generated by Django 4.0.3 on 2022-08-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip54app', '0024_alter_checkout_added_by_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='on_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
