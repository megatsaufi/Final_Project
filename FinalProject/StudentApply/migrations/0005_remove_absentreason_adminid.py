# Generated by Django 5.0 on 2024-02-22 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApply', '0004_alter_absentreason_adminid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absentreason',
            name='AdminId',
        ),
    ]
