# Generated by Django 4.2.2 on 2023-06-25 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
    ]
