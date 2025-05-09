# Generated by Django 5.1.3 on 2025-02-27 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_teacher'),
        ('Guest', '0004_tbl_user_user_status'),
        ('User', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_complaint',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_teacher'),
        ),
        migrations.AlterField(
            model_name='tbl_complaint',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user'),
        ),
    ]
