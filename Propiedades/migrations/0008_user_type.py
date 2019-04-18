# Generated by Django 2.0.4 on 2019-04-17 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_users', '0002_userprofile_password'),
        ('Propiedades', '0007_auto_20190416_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadership', models.BooleanField()),
                ('administrator', models.BooleanField()),
                ('digitizer', models.BooleanField()),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth_users.UserProfile')),
            ],
        ),
    ]
