# Generated by Django 2.2.24 on 2021-09-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='horario_begin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clase',
            name='horario_end',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
