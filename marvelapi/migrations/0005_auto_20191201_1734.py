# Generated by Django 2.2.7 on 2019-12-01 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marvelapi', '0004_auto_20191201_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='name',
            new_name='type',
        ),
    ]