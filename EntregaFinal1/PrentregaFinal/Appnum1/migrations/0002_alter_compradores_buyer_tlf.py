# Generated by Django 4.1 on 2022-09-26 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appnum1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compradores',
            name='buyer_tlf',
            field=models.IntegerField(),
        ),
    ]