# Generated by Django 5.0 on 2024-02-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApply', '0002_adminstration_password_mentor_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absentreason',
            name='Status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
