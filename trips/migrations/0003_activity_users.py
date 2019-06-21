# Generated by Django 2.2.2 on 2019-06-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_tripphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('type', models.TextField(blank=True, null=True)),
                ('activity_id', models.AutoField(db_column='Activity_id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('city', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
