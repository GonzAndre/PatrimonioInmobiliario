# Generated by Django 2.0.4 on 2019-04-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Propiedades', '0006_auto_20190416_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_use',
            field=models.CharField(choices=[('IGL', 'Iglesia'), ('GRU', 'Grupo'), ('COL', 'Colegio'), ('HAB', 'Habitacional'), ('Otro', 'Otro')], max_length=15),
        ),
    ]
