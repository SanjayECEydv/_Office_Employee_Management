# Generated by Django 4.0.5 on 2022-10-27 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='employee_id',
            new_name='emp_id',
        ),
    ]
