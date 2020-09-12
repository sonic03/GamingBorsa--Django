# Generated by Django 3.0.5 on 2020-09-03 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productCode',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='Ürün Kodu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=300, verbose_name='Price'),
        ),
    ]