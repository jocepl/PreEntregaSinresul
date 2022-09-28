# Generated by Django 4.1 on 2022-09-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appnum1', '0005_remove_compradores_b_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_nombre', models.CharField(max_length=40)),
                ('b_apellido', models.CharField(max_length=40)),
                ('b_email', models.EmailField(max_length=254)),
                ('b_direccion', models.CharField(max_length=70)),
                ('b_tlf', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='compradores',
        ),
    ]
