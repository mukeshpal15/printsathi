# Generated by Django 2.1.1 on 2020-06-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0019_auto_20200613_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResellerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reseller_ID', models.CharField(max_length=100)),
                ('Reseller_First_Name', models.CharField(max_length=100)),
                ('Reseller_Last_Name', models.CharField(max_length=100)),
                ('Reseller_Gender', models.CharField(max_length=100)),
                ('Reseller_Email', models.CharField(max_length=100)),
                ('Reseller_Phone', models.CharField(max_length=100)),
                ('Reseller_Address', models.CharField(max_length=1000)),
                ('Reseller_City', models.CharField(max_length=100)),
                ('Reseller_State', models.CharField(max_length=100)),
                ('Reseller_GSTIN', models.CharField(max_length=100)),
                ('Reseller_PAN', models.CharField(max_length=100)),
                ('Reseller_Password', models.CharField(max_length=100)),
                ('Reseller_Status', models.CharField(max_length=100)),
                ('Adhaar', models.ImageField(upload_to='reselleradhaar/')),
                ('Profile', models.ImageField(upload_to='resellerprofile/')),
                ('conditions', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ResellerData',
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.CharField(max_length=100)),
                ('User_First_Name', models.CharField(max_length=100)),
                ('User_Last_Name', models.CharField(max_length=100)),
                ('User_Gender', models.CharField(max_length=100)),
                ('User_Email', models.CharField(max_length=100)),
                ('User_Phone', models.CharField(max_length=100)),
                ('User_Address', models.CharField(max_length=1000)),
                ('User_City', models.CharField(max_length=100)),
                ('User_State', models.CharField(max_length=100)),
                ('User_Password', models.CharField(max_length=100)),
                ('conditions', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UserData',
            },
        ),
    ]