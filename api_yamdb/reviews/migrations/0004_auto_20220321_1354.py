# Generated by Django 2.2.16 on 2022-03-21 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220321_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('role',)},
        ),
    ]