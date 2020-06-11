# Generated by Django 3.0.5 on 2020-06-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=40)),
                ('sobrenome', models.CharField(max_length=60)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('nacionalidade', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_cartao', models.CharField(max_length=16)),
                ('titular_cartao', models.CharField(max_length=60)),
                ('validade_cartao', models.DateField()),
                ('codigo_seguranca', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
    ]
