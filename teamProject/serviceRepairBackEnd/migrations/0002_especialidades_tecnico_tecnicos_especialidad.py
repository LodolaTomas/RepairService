# Generated by Django 3.2.9 on 2022-01-06 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceRepairBackEnd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialidad', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('foto', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnicos_Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceRepairBackEnd.tecnico')),
                ('especialidades_id', models.ManyToManyField(to='serviceRepairBackEnd.Especialidades')),
            ],
        ),
    ]