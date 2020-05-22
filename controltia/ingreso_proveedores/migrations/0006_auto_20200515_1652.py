# Generated by Django 2.2 on 2020-05-15 21:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_proveedores', '0005_auto_20200514_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('piso', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2020, 5, 15, 16, 51, 57, 744820), editable=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='reunion',
            name='piso',
        ),
        migrations.AlterField(
            model_name='historial',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 16, 51, 57, 745823), editable=False),
        ),
        migrations.AlterField(
            model_name='reunion',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 16, 51, 57, 745823), editable=False),
        ),
        migrations.AddField(
            model_name='reunion',
            name='sala',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ingreso_proveedores.Sala'),
            preserve_default=False,
        ),
    ]
