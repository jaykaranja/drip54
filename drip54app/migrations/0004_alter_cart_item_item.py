# Generated by Django 4.0.3 on 2022-08-08 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drip54app', '0003_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item', to='drip54app.product', unique=True),
        ),
    ]
