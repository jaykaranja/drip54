# Generated by Django 4.0.3 on 2022-08-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip54app', '0009_clothtype_product_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(default='Nairobi', max_length=50)),
            ],
        ),
    ]
