# Generated by Django 4.0.3 on 2022-08-10 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drip54app', '0006_alter_cart_item_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='drip54app.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drip54app.brand'),
        ),
        migrations.CreateModel(
            name='FavoriteItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drip54app.product')),
            ],
        ),
    ]