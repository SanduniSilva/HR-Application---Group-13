# Generated by Django 3.2.23 on 2023-11-22 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetail',
            old_name='jounindate',
            new_name='joiningdate',
        ),
    ]
