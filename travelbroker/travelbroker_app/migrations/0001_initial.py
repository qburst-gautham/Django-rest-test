# Generated by Django 4.2.8 on 2024-01-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Travel_point', models.CharField(max_length=100)),
            ],
        ),
    ]
