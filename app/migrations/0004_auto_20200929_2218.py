# Generated by Django 3.1.1 on 2020-09-30 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200929_2033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizza',
            new_name='model_pizza',
        ),
    ]