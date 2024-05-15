# Generated by Django 4.2.11 on 2024-05-14 00:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finsite', '0006_rename_id_product_keeping_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_change', models.DateField(default=datetime.datetime(2024, 5, 14, 9, 16, 13, 469700), verbose_name='Дата изменения цены')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_change', models.DateField(default=datetime.datetime(2024, 5, 14, 9, 16, 13, 469976), verbose_name='Дата поставки')),
                ('amount', models.IntegerField(default=0, verbose_name='Количество')),
            ],
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Keeping',
            new_name='Keep',
        ),
        migrations.RenameModel(
            old_name='Storages',
            new_name='Storage',
        ),
        migrations.RemoveField(
            model_name='supplies',
            name='product',
        ),
        migrations.RemoveField(
            model_name='supplies',
            name='provider',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Providers',
            new_name='Provider',
        ),
        migrations.DeleteModel(
            name='PriceManagments',
        ),
        migrations.DeleteModel(
            name='Supplies',
        ),
        migrations.AddField(
            model_name='supplier',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finsite.product', verbose_name='Номер товара'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finsite.provider', verbose_name='Номер поставщика'),
        ),
        migrations.AddField(
            model_name='pricemanagement',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finsite.product', verbose_name='Номер товара'),
        ),
    ]