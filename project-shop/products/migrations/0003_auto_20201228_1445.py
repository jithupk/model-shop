# Generated by Django 3.1.4 on 2020-12-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_list_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_list',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]