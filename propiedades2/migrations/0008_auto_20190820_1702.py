# Generated by Django 2.2.2 on 2019-08-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0007_auto_20190625_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisition',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rent',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
