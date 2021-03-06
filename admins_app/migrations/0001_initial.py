# Generated by Django 2.0.2 on 2018-10-26 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceilphone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('salts', models.CharField(max_length=5)),
                ('user_status', models.BooleanField()),
            ],
            options={
                'db_table': 't_user',
            },
        ),
    ]
