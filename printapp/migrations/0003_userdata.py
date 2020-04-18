# Generated by Django 2.1.9 on 2020-04-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0002_productdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.CharField(max_length=100)),
                ('User_First_Name', models.CharField(max_length=100)),
                ('User_Last_Name', models.CharField(max_length=100)),
                ('User_Email', models.CharField(max_length=100)),
                ('User_Phone', models.CharField(max_length=100)),
                ('User_Address', models.CharField(max_length=1000)),
                ('User_City', models.CharField(max_length=100)),
                ('User_State', models.CharField(max_length=100)),
                ('User_Password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UserData',
            },
        ),
    ]
