# Generated by Django 2.1.4 on 2018-12-08 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostApplications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_id', models.IntegerField()),
                ('webserver_ids', models.CharField(max_length=50)),
                ('database_ids', models.CharField(max_length=50)),
            ],
        ),
    ]
