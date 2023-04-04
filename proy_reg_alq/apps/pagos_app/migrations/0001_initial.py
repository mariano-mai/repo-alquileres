# Generated by Django 4.1.7 on 2023-04-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(blank=True, max_length=3, null=True)),
                ('fecha_de_pago', models.DateField(blank=True, null=True)),
                ('periodo_correspondiente', models.CharField(max_length=25)),
                ('importe_alquiler', models.FloatField(max_length=10)),
                ('importe_electricidad', models.FloatField(max_length=10)),
                ('importe_agua', models.FloatField(max_length=10)),
            ],
        ),
    ]