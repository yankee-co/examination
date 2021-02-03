# Generated by Django 3.1.4 on 2021-02-03 18:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iban', models.CharField(max_length=29, unique=True)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth', models.DateTimeField()),
                ('idenity_code', models.IntegerField(unique=True)),
                ('passport', models.IntegerField(unique=True)),
                ('client_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 2, 3, 20, 16, 28, 185903))),
                ('description', models.CharField(max_length=255)),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 2, 3, 20, 16, 28, 185903))),
                ('description', models.CharField(max_length=255)),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.account')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.transactiontype')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.client'),
        ),
    ]
