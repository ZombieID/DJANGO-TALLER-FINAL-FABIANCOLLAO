# Generated by Django 4.1.1 on 2022-12-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_alter_inscritos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='fecha_insc',
            field=models.DateField(verbose_name='Fecha de Inscripción'),
        ),
        migrations.AlterField(
            model_name='inscritos',
            name='hora_insc',
            field=models.TimeField(verbose_name='Hora de Inscripción'),
        ),
        migrations.AlterField(
            model_name='inscritos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]