# Generated by Django 5.2.1 on 2025-05-26 03:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0006_alter_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsroom.source'),
        ),
    ]
