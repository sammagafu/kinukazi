# Generated by Django 3.2.5 on 2022-12-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221220_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_verified_account',
            field=models.BooleanField(default=False, verbose_name='verified users'),
        ),
    ]
