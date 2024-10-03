# Generated by Django 5.1.1 on 2024-10-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_register', '0006_alter_myuser_groups_alter_myuser_user_permissions'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='student_id',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]