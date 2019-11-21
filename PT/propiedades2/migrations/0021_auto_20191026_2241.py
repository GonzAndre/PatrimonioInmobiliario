# Generated by Django 2.2 on 2019-10-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0020_notification_type_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='time_str',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='action',
            field=models.CharField(choices=[('AA', 'Añadir adquisición'), ('AR', 'Añadir renta'), ('EA', 'Editar adquisición'), ('ER', 'Editar renta'), ('SA', 'Estatus Activo'), ('SI', 'Estatus Inactivo'), ('PA', 'Post adquisición'), ('PR', 'Post renta'), ('RA', 'Respuesta adquisición'), ('RR', 'Respuesta renta')], max_length=2),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type_property',
            field=models.CharField(choices=[('AA', 'Añadir adquisición'), ('AR', 'Añadir renta'), ('EA', 'Editar adquisición'), ('ER', 'Editar renta'), ('SA', 'Estatus Activo'), ('SI', 'Estatus Inactivo'), ('PA', 'Post adquisición'), ('PR', 'Post renta'), ('RA', 'Respuesta adquisición'), ('RR', 'Respuesta renta')], max_length=2),
        ),
    ]
