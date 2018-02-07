# Generated by Django 2.0.2 on 2018-02-07 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0015_auto_20180207_0835'),
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
                ('last_communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.Communication')),
            ],
        ),
        migrations.CreateModel(
            name='LeadPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LeadStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.LeadPost'),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.LeadStage'),
        ),
    ]
