# Generated by Django 4.2.5 on 2024-11-03 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0004_employee_role"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee", name="role",),
    ]
