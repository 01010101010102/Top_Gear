# Generated by Django 4.2.3 on 2023-08-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='nome', max_length=30)),
                ('telefone', models.CharField(db_column='telefone', max_length=15)),
                ('rua', models.CharField(db_column='rua', max_length=50, null=True)),
                ('numero', models.PositiveSmallIntegerField(db_column='numero', null=True)),
                ('cidade', models.CharField(db_column='cidade', default='Imperatriz', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_veiculo', models.CharField(choices=[('CRP', 'Carro de passeio'), ('CMT', 'Camionete'), ('MT', 'Moto')], db_column='tipo_veiculo', default='CRP', max_length=3)),
                ('placa', models.CharField(db_column='placa', max_length=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
