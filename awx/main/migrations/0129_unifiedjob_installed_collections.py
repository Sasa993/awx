# Generated by Django 2.2.16 on 2021-02-16 20:27

import awx.main.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0128_organiaztion_read_roles_ee_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='unifiedjob',
            name='installed_collections',
            field=awx.main.fields.JSONBField(blank=True, default=dict, editable=False, help_text='The Collections names and versions installed in the execution environment.'),
        ),
    ]
