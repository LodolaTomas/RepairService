# Generated by Django 3.2.9 on 2022-01-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceRepairBackEnd', '0004_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tecnico',
            name='foto',
        ),
        migrations.AddField(
            model_name='tecnico',
            name='image',
            field=models.ImageField(default='test', upload_to='imagesTecnico'),
            preserve_default=False,
        ),
    ]