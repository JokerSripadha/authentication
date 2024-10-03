# Generated by Django 5.1.1 on 2024-10-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_register', '0008_alter_myuser_email_alter_myuser_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='student_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]