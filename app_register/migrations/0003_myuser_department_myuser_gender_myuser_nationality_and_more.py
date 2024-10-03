# Generated by Django 5.1.1 on 2024-10-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_register', '0002_myuser_is_staff_alter_myuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='Department',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='nationality',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='student_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]