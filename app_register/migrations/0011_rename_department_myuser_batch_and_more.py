# Generated by Django 5.1.1 on 2024-10-03 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_register', '0010_alter_myuser_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='department',
            new_name='Batch',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='gender',
            new_name='branch',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='nationality',
        ),
    ]
