# Generated by Django 2.2.16 on 2022-03-10 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220311_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('id',), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]
