# Generated by Django 4.2.7 on 2023-12-04 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pais_origen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.pais'),
        ),
    ]
