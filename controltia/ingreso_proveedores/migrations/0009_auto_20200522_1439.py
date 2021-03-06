# Generated by Django 2.2 on 2020-05-22 19:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_proveedores', '0008_auto_20200520_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historial',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 14, 39, 41, 237487), editable=False),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='autor',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='cedula',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='correo',
            field=multi_email_field.fields.MultiEmailField(help_text='A esta lista de email se enviará el QR de acceso, sepárelos mediante ENTER'),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 14, 39, 41, 236986), editable=False),
        ),
        migrations.AlterField(
            model_name='sala',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 14, 39, 41, 236485), editable=False),
        ),
    ]
