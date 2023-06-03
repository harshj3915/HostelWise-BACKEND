# Generated by Django 4.1.7 on 2023-06-03 22:33

import RESTAPI.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('c_SECRETKEY', models.CharField(default=RESTAPI.models.generate_auto_generated_field_value, max_length=25, unique=True)),
                ('c_Name', models.CharField(max_length=100)),
                ('c_Gender', models.CharField(max_length=10)),
                ('c_Phone', models.CharField(max_length=10, unique=True)),
                ('c_Password', models.CharField(default='defaultpw', max_length=100)),
                ('c_Registration_Number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('c_Block', models.CharField(max_length=1)),
                ('c_Type', models.CharField(default='CLEANER', max_length=10)),
                ('c_RoomsCleaned', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_SECRETKEY', models.CharField(default=RESTAPI.models.generate_auto_generated_field_value, max_length=25, primary_key=True, serialize=False, unique=True)),
                ('s_Name', models.CharField(max_length=100)),
                ('s_Gender', models.CharField(max_length=10)),
                ('s_Email', models.CharField(max_length=100, unique=True)),
                ('s_Password', models.CharField(max_length=100)),
                ('s_Registration_Number', models.CharField(max_length=10, unique=True)),
                ('s_Room_Number', models.CharField(max_length=10)),
                ('s_Block', models.CharField(max_length=1)),
                ('s_Type', models.CharField(default='STUDENT', max_length=10)),
                ('s_Already_Requested_Room_clean', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('su_SECRETKEY', models.CharField(default=RESTAPI.models.generate_auto_generated_field_value, max_length=50, unique=True)),
                ('su_ID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('su_Password', models.CharField(max_length=100)),
                ('su_Name', models.CharField(max_length=100)),
                ('su_Block', models.CharField(max_length=10)),
                ('su_Type', models.CharField(default='SUPERUSER', max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomCleanData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('cleaner_ID', models.CharField(default='', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.CharField(blank=True, max_length=100, null=True)),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RESTAPI.student')),
            ],
        ),
        migrations.CreateModel(
            name='ComplainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=5000)),
                ('completed', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.CharField(blank=True, max_length=100, null=True)),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RESTAPI.student')),
            ],
        ),
    ]
