# Generated by Django 2.2 on 2020-05-14 08:01

import datetime
from django.db import migrations, models
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_proveedores', '0003_auto_20200513_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reunion',
            name='cantidad_personas',
        ),
        migrations.AddField(
            model_name='reunion',
            name='correos',
            field=multi_email_field.fields.MultiEmailField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historial',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 3, 1, 53, 452105), editable=False),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='correo',
            field=models.EmailField(help_text='A esta email se enviara el QR de acceso', max_length=254),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 3, 1, 53, 451102), editable=False),
        ),
    ]
