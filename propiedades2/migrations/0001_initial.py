# Generated by Django 2.2 on 2019-08-30 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role_number', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Fotos/')),
                ('acquisition_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('writing_data', models.CharField(choices=[('COM', 'Compraventa'), ('DON', 'Donación'), ('SUB', 'Subdivisión'), ('Otro', 'Otro')], max_length=5)),
                ('number_AASI', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentAc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentBlue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentBuildP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentEs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentEx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentMR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentOther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentPH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentTypeC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], default='TC', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentWR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.FileField(blank=True, upload_to='Documentos/')),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TC', 'Tipo contrato'), ('ES', 'Escritura'), ('DC', 'Certificado de dominio'), ('PR', 'Prohibiciones'), ('SE', 'Expropiación SERVIU'), ('OT', 'Otro'), ('EM', 'Expropiación Municipalidad'), ('CP', 'CIP'), ('NC', 'Número certificado'), ('PL', 'Planos'), ('PE', 'Permiso de edificación'), ('RM', 'Recepción municipal'), ('CA', 'Certificado avalúo'), ('CD', 'Certificado no deuda')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('number', models.PositiveIntegerField()),
                ('commune', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('lot_number', models.PositiveIntegerField(blank=True, null=True)),
                ('plot', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(blank=True, max_length=3, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(blank=True, max_length=3, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('type_user', models.CharField(choices=[('DIG', 'Digitador'), ('ADM', 'Administrador'), ('VIS', 'Visualizador')], max_length=3)),
                ('status', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('username_staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiiRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destiny', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_appraisal', models.PositiveIntegerField(blank=True, null=True)),
                ('owner_name_SII', models.CharField(blank=True, max_length=100, null=True)),
                ('total_debt', models.PositiveIntegerField(blank=True, null=True)),
                ('ex_contributions', models.BooleanField(default=False)),
                ('appraisal_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CerAvaluo', to='propiedades2.DocumentAc')),
                ('debt_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CerNoDeuda', to='propiedades2.DocumentDB')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role_number', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Fotos/')),
                ('ground_surface', models.CharField(blank=True, max_length=100, null=True)),
                ('square_m_build', models.CharField(blank=True, max_length=100, null=True)),
                ('e_construction_m', models.CharField(blank=True, max_length=100, null=True)),
                ('municipal_n', models.PositiveIntegerField(blank=True, null=True)),
                ('n_building_permit', models.PositiveIntegerField(blank=True, null=True)),
                ('value_land', models.CharField(blank=True, max_length=100, null=True)),
                ('value_construction', models.CharField(blank=True, max_length=100, null=True)),
                ('acquiring_name', models.CharField(max_length=100)),
                ('supplier_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.PositiveIntegerField()),
                ('contract_type', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoContratoArriendo', to='propiedades2.DocumentTypeC')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='propiedades2.Location')),
                ('property_use', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades2.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('acquisition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PostAcquisition', to='propiedades2.Acquisition')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='propiedades2.Staff')),
                ('rent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PostRent', to='propiedades2.Rent')),
            ],
        ),
        migrations.CreateModel(
            name='NotaryAcquisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notary', models.CharField(blank=True, max_length=100, null=True)),
                ('writing_year', models.PositiveIntegerField(blank=True, null=True)),
                ('sale_price', models.CharField(blank=True, max_length=100, null=True)),
                ('previous_title', models.CharField(blank=True, max_length=100, null=True)),
                ('current_title', models.CharField(blank=True, max_length=100, null=True)),
                ('domain_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CertificadoDominio', to='propiedades2.DocumentDC')),
                ('expropriation_serviu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Serviu', to='propiedades2.DocumentEs')),
                ('prohibitions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Prohibiciones', to='propiedades2.DocumentPH')),
                ('writing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Escritura', to='propiedades2.DocumentWR')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades2.Region'),
        ),
        migrations.CreateModel(
            name='InternalAccountantsAcq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_land', models.CharField(blank=True, max_length=100, null=True)),
                ('value_construction', models.CharField(blank=True, max_length=100, null=True)),
                ('acquiring_name', models.CharField(blank=True, max_length=100, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TipoContratoAdquisicion', to='propiedades2.DocumentTypeC')),
                ('others', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Otros', to='propiedades2.DocumentOther')),
            ],
        ),
        migrations.CreateModel(
            name='ArchitectureRecordAcq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ground_surface', models.CharField(blank=True, max_length=100, null=True)),
                ('square_m_build', models.CharField(blank=True, max_length=100, null=True)),
                ('e_construction_m', models.CharField(blank=True, max_length=100, null=True)),
                ('municipal_n', models.PositiveIntegerField(blank=True, null=True)),
                ('n_building_permit', models.PositiveIntegerField(blank=True, null=True)),
                ('blueprints', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Planos', to='propiedades2.DocumentBlue')),
                ('building_permit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PerEdificacion', to='propiedades2.DocumentBuildP')),
                ('certified_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='NumCertificado', to='propiedades2.DocumentCn')),
                ('cip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cip', to='propiedades2.DocumentCip')),
                ('expropriation_mun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ExMunicipalidad', to='propiedades2.DocumentEx')),
                ('municipal_reception', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RecMunicipal', to='propiedades2.DocumentMR')),
            ],
        ),
        migrations.AddField(
            model_name='acquisition',
            name='SII',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SII_acq', to='propiedades2.SiiRecord'),
        ),
        migrations.AddField(
            model_name='acquisition',
            name='arquitecture',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arquitecture_acq', to='propiedades2.ArchitectureRecordAcq'),
        ),
        migrations.AddField(
            model_name='acquisition',
            name='internal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_acq', to='propiedades2.InternalAccountantsAcq'),
        ),
        migrations.AddField(
            model_name='acquisition',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='propiedades2.Location'),
        ),
        migrations.AddField(
            model_name='acquisition',
            name='notary',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notary_acq', to='propiedades2.NotaryAcquisition'),
        ),
        migrations.AddField(
            model_name='acquisition',
            name='property_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades2.Property'),
        ),
    ]
