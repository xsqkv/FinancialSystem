# Generated by Django 4.2.11 on 2024-05-16 03:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finsite', '0007_pricemanagement_supplier_rename_categories_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('gender', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('gender', models.BooleanField()),
                ('salary', models.FloatField(default=12500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='finsite.employee')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='finsite.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(max_length=1500)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='finsite.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplyLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='pricemanagement',
            name='product',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='product',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='building',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='city',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childrens', to='finsite.category'),
        ),
        migrations.AddField(
            model_name='storage',
            name='build',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='storage',
            name='locality',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='storage',
            name='postal_codes',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='storage',
            name='price',
            field=models.FloatField(default=6250),
        ),
        migrations.AddField(
            model_name='storage',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='finsite.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='storage',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='storage',
            name='district',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='storage',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='storage',
            name='region',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='storage',
            name='street',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Keep',
        ),
        migrations.DeleteModel(
            name='PriceManagement',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.AddField(
            model_name='supplyline',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supply_lines', to='finsite.product'),
        ),
        migrations.AddField(
            model_name='supplyline',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supply_lines', to='finsite.provider'),
        ),
        migrations.AddField(
            model_name='supplyline',
            name='supply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supply_lines', to='finsite.supply'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='finsite.product'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='finsite.productpricehistory'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='finsite.product'),
        ),
    ]
