# Generated by Django 2.2.16 on 2022-07-05 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0001_initial'),
        ('notificationsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='service',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicesapp.Service'),
        ),
    ]
