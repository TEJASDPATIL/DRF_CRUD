# Generated by Django 2.0.1 on 2020-03-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
            ],
        ),
    ]
