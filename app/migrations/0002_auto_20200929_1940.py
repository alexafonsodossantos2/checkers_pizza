# Generated by Django 3.1.1 on 2020-09-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
