# Generated by Django 2.0.2 on 2018-02-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0004_auto_20180207_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communication',
            name='reminder',
        ),
        migrations.RemoveField(
            model_name='substage',
            name='enable_reminder',
        ),
        migrations.AddField(
            model_name='communication',
            name='medium',
            field=models.CharField(choices=[('Outbound Call', 'Outbound Call'), ('Inbound Call', 'Inbound Call'), ('Inbound Email', 'Inbound Email'), ('Outbound Email', 'Outbound Email'), ('SMS', 'SMS'), ('Meeting', 'Meeting')], default='SMS', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='substage',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='substage',
            name='set_reminder',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Reminder',
        ),
    ]