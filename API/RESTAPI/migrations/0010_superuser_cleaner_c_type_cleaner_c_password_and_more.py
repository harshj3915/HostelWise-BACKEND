# Generated by Django 4.1.7 on 2023-06-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RESTAPI', '0009_alter_student_s_secretkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('su_ID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('su_Password', models.CharField(max_length=100)),
                ('su_Name', models.CharField(max_length=100)),
                ('su_Block', models.CharField(max_length=10)),
                ('su_Type', models.CharField(default='SUPERUSER', editable=False, max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='cleaner',
            name='c_Type',
            field=models.CharField(default='CLEANER', editable=False, max_length=10),
        ),
        migrations.AddField(
            model_name='cleaner',
            name='c_password',
            field=models.CharField(default='defaultpw', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='s_Type',
            field=models.CharField(default='STUDENT', editable=False, max_length=10),
        ),
    ]
