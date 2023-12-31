# Generated by Django 3.2.23 on 2023-12-01 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employees', '0004_rename_destination_employeedetail_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1name', models.CharField(max_length=100, null=True)),
                ('company1desig', models.CharField(max_length=100, null=True)),
                ('company1salary', models.CharField(max_length=100, null=True)),
                ('company1duration', models.CharField(max_length=100, null=True)),
                ('company2name', models.CharField(max_length=100, null=True)),
                ('company2desig', models.CharField(max_length=100, null=True)),
                ('company2salary', models.CharField(max_length=100, null=True)),
                ('company2duration', models.CharField(max_length=100, null=True)),
                ('company3name', models.CharField(max_length=100, null=True)),
                ('company3desig', models.CharField(max_length=100, null=True)),
                ('company3salary', models.CharField(max_length=100, null=True)),
                ('company3duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
