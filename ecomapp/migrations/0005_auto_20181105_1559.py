# Generated by Django 2.1.3 on 2018-11-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_auto_20181105_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='model',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='ecomapp.CartItem'),
        ),
    ]