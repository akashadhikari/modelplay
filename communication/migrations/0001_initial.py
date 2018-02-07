# Generated by Django 2.0.2 on 2018-02-07 08:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0015_auto_20180207_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
        migrations.CreateModel(
            name='SalesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sales_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.SalesGroup')),
            ],
        ),
        migrations.AddField(
            model_name='communication',
            name='sales_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.SubStage'),
        ),
    ]
