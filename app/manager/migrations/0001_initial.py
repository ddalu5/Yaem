# Generated by Django 3.0.4 on 2020-03-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('key', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ['key'],
            },
        ),
    ]
