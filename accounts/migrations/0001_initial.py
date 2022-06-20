# Generated by Django 3.2.9 on 2022-06-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=30)),
                ('student_name', models.CharField(max_length=30)),
                ('student_department', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_mobile', models.IntegerField()),
                ('student_address', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'student_list',
            },
        ),
    ]
