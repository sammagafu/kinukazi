# Generated by Django 3.2.5 on 2022-12-20 16:04

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsemiindusry',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=90, scale=None, size=[300, 300], upload_to='machine/category', verbose_name='Avatar'),
        ),
        migrations.AddField(
            model_name='prouctindusty',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=90, scale=None, size=[300, 300], upload_to='machine/category', verbose_name='Avatar'),
        ),
    ]
