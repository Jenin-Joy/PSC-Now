# Generated by Django 5.1.3 on 2025-03-10 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_tbl_complaint_teacher_alter_tbl_complaint_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_complaint',
        ),
    ]
