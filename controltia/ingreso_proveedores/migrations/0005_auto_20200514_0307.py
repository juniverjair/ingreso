# Generated by Django 2.2 on 2020-05-14 08:07

import datetime
from django.db import migrations, models
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_proveedores', '0004_auto_20200514_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reunion',
            name='correos',
        ),
        migrations.AlterField(
            model_name='historial',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 3, 7, 48, 343130), editable=False),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='correo',
            field=multi_email_field.fields.MultiEmailField(help_text='A esta lista de email se enviara el QR de acceso, separelos mediante ENTER'),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 3, 7, 48, 342134), editable=False),
        ),
    ]