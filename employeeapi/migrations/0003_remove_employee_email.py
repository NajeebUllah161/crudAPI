# Generated by Django 3.1.6 on 2021-06-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0002_employee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
    ]
