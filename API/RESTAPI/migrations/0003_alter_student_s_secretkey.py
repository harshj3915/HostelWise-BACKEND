# Generated by Django 4.1.7 on 2023-06-02 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('RESTAPI', '0002_alter_student_s_secretkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_SECRETKEY',
            field=models.CharField(default=uuid.UUID('f43e2982-d6d5-49dc-b35b-aaa8ce8073c5'), max_length=128, unique=True),
        ),
    ]
