# Generated by Django 2.2.16 on 2022-03-04 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('id',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
    ]
