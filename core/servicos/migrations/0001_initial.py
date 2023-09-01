# Generated by Django 4.2.3 on 2023-08-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolha_servico', models.CharField(choices=[('LG', 'Geral'), ('ML', 'Meia_Sola'), ('MTR', 'Motor'), ('DKB', 'Disck_Busca'), ('PTR', 'Pintura'), ('APR', 'Aspiração')], db_column='escolha_servico', default='ML', max_length=3)),
                ('aviso', models.CharField(db_column='aviso', max_length=60, null=True)),
                ('data_inicio', models.DateTimeField()),
                ('valor_total', models.FloatField()),
                ('veiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.veiculo')),
            ],
        ),
    ]