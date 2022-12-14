# Generated by Django 3.2.5 on 2022-12-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='is_bussness',
            field=models.BooleanField(default=False, verbose_name='Business Account'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='Normal Account'),
        ),
    ]
