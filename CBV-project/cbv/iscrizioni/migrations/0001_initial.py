# Generated by Django 5.0.4 on 2024-04-23 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insegnamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Insegnamenti',
            },
        ),
        migrations.CreateModel(
            name='Studente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Studenti',
            },
        ),
        migrations.CreateModel(
            name='Iscrizione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insegnamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.insegnamento')),
                ('studente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.studente')),
            ],
        ),
        migrations.AddField(
            model_name='insegnamento',
            name='studenti',
            field=models.ManyToManyField(default=None, through='iscrizioni.Iscrizione', to='iscrizioni.studente'),
        ),
    ]
