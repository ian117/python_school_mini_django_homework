# Generated by Django 2.2.24 on 2021-09-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('clases', models.ManyToManyField(blank=True, to='clases.Clase')),
            ],
        ),
    ]
