# Generated by Django 4.2.5 on 2024-11-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
