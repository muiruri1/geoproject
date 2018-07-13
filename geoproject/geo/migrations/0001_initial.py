# Generated by Django 2.0.7 on 2018-07-10 10:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
