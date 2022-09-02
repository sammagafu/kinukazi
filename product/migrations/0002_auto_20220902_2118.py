# Generated by Django 3.2.5 on 2022-09-02 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='Caterpillar', max_length=160, verbose_name='Product Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Daily Renting Price'),
        ),
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=160, verbose_name='Specification')),
                ('value', models.CharField(max_length=120, verbose_name='Specification')),
                ('produtct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='')),
            ],
        ),
    ]