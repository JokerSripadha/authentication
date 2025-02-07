# Generated by Django 5.1.1 on 2024-10-02 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_register', '0003_myuser_department_myuser_gender_myuser_nationality_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='student_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
